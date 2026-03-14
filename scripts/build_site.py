#!/usr/bin/env python3
"""
build_site.py — Render content/ and data/ into a static site in docs/.

Usage:
    python scripts/build_site.py
    python scripts/build_site.py --clean   # wipe docs/ first
"""

import argparse
import shutil
from pathlib import Path

import frontmatter
import markdown
import yaml
import jinja2
from jinja2 import Environment, FileSystemLoader

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
DATA = ROOT / "data"
DOCS = ROOT / "docs"
TEMPLATES = ROOT / "scripts" / "templates"
ASSETS_SRC = ROOT / "docs" / "assets"  # copied as-is

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_yaml(path: Path) -> dict | list:
    with open(path) as f:
        return yaml.safe_load(f)


def load_paper_digest(path: Path) -> dict:
    """Load a paper digest .md file, returning front matter + rendered HTML body."""
    post = frontmatter.load(path)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    body_html = md.convert(post.content)
    meta = dict(post.metadata)
    meta["body_html"] = body_html
    return meta


def load_topic(path: Path) -> dict:
    """Load a topic stream .md file."""
    post = frontmatter.load(path)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    body_html = md.convert(post.content)
    meta = dict(post.metadata)
    meta["body_html"] = body_html
    return meta


def build_stream_lookup(streams_data: list[dict]) -> dict:
    """Map stream id → stream metadata."""
    return {s["id"]: s for s in streams_data}


def papers_for_stream(papers: list[dict], stream_id: str) -> list[dict]:
    """Return papers belonging to a given stream, sorted by year."""
    matched = [p for p in papers if stream_id in p.get("streams", [])]
    return sorted(matched, key=lambda p: p.get("year", 0))


def group_by_era(papers: list[dict]) -> dict[str, list[dict]]:
    """Group papers into era buckets."""
    groups = {"foundational": [], "key-development": [], "frontier": []}
    for p in papers:
        era = p.get("era", "frontier")
        groups.setdefault(era, []).append(p)
    return groups

# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_site(clean: bool = False):
    if clean and DOCS.exists():
        # Preserve assets directory
        print("Cleaning docs/ ...")
        for item in DOCS.iterdir():
            if item.name == "assets":
                continue
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    DOCS.mkdir(exist_ok=True)

    # Ensure .nojekyll exists for GitHub Pages
    (DOCS / ".nojekyll").touch()

    # Load data
    streams_raw = load_yaml(DATA / "streams.yaml")
    streams_list = streams_raw.get("streams", streams_raw) if isinstance(streams_raw, dict) else streams_raw
    stream_lookup = build_stream_lookup(streams_list)

    papers_raw = load_yaml(DATA / "papers.yaml")
    papers_registry = papers_raw.get("papers", papers_raw) if isinstance(papers_raw, dict) else papers_raw
    if papers_registry is None:
        papers_registry = []

    # Load paper digest files
    paper_digests = {}
    papers_dir = CONTENT / "papers"
    for md_file in papers_dir.glob("*.md"):
        if md_file.name.startswith("_"):
            continue
        try:
            digest = load_paper_digest(md_file)
            paper_digests[digest["id"]] = digest
        except Exception as e:
            print(f"  Warning: could not load {md_file.name}: {e}")

    # Merge registry metadata with digest content
    papers_full = []
    for entry in papers_registry:
        pid = entry["id"]
        merged = dict(entry)
        if pid in paper_digests:
            merged.update(paper_digests[pid])
        # Ensure body_html always exists for template safety
        merged.setdefault("body_html", "")
        papers_full.append(merged)

    # Load topic stream files
    topics = {}
    topics_dir = CONTENT / "topics"
    for md_file in topics_dir.glob("*.md"):
        if md_file.name.startswith("_"):
            continue
        try:
            topic = load_topic(md_file)
            tid = topic.get("id", md_file.stem)
            topics[tid] = topic
        except Exception as e:
            print(f"  Warning: could not load {md_file.name}: {e}")

    # Load topic index
    topic_index = None
    index_path = topics_dir / "_index.md"
    if index_path.exists():
        topic_index = load_topic(index_path)

    # Setup Jinja2
    TEMPLATES.mkdir(exist_ok=True)
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=False,
        undefined=jinja2.Undefined,
    )

    # Load site config
    site_config_path = ROOT / "configs" / "site.yaml"
    site_config = load_yaml(site_config_path) if site_config_path.exists() else {}

    # Common template context
    base_ctx = {
        "site": site_config.get("site", {}),
        "nav": site_config.get("navigation", []),
        "theme": site_config.get("theme", {}),
        "streams": streams_list,
        "stream_lookup": stream_lookup,
        "total_papers": len(papers_full),
    }

    # --- Render index.html ---
    print("Rendering index.html ...")
    tmpl = env.get_template("index.html")
    html = tmpl.render(**base_ctx, papers=papers_full)
    (DOCS / "index.html").write_text(html)

    # --- Render topic pages ---
    topics_out = DOCS / "topics"
    topics_out.mkdir(exist_ok=True)

    # Topic index page
    tmpl_topic_index = env.get_template("topic_index.html")
    html = tmpl_topic_index.render(**base_ctx, topic_index=topic_index, topics=topics)
    (topics_out / "index.html").write_text(html)

    # Individual topic pages
    tmpl_topic = env.get_template("topic.html")
    for sid, stream_meta in stream_lookup.items():
        stream_dir = topics_out / sid
        stream_dir.mkdir(exist_ok=True)
        stream_papers = papers_for_stream(papers_full, sid)
        era_groups = group_by_era(stream_papers)
        topic_content = topics.get(sid, {})
        html = tmpl_topic.render(
            **base_ctx,
            stream=stream_meta,
            topic=topic_content,
            papers=stream_papers,
            era_groups=era_groups,
        )
        (stream_dir / "index.html").write_text(html)
        print(f"  topics/{sid}/index.html ({len(stream_papers)} papers)")

    # --- Render paper pages ---
    papers_out = DOCS / "papers"
    papers_out.mkdir(exist_ok=True)
    tmpl_paper = env.get_template("paper.html")
    for paper in papers_full:
        if not paper.get("body_html"):
            continue  # Skip papers without digest content
        paper_dir = papers_out / paper["id"]
        paper_dir.mkdir(exist_ok=True)
        html = tmpl_paper.render(**base_ctx, paper=paper)
        (paper_dir / "index.html").write_text(html)
        print(f"  papers/{paper['id']}/index.html")

    # --- Render explore page ---
    explore_out = DOCS / "explore"
    explore_out.mkdir(exist_ok=True)
    tmpl_explore = env.get_template("explore.html")
    all_tags = sorted({t for p in papers_full for t in p.get("tags", [])})
    all_years = sorted({p["year"] for p in papers_full})
    html = tmpl_explore.render(
        **base_ctx,
        papers=papers_full,
        all_tags=all_tags,
        all_years=all_years,
    )
    (explore_out / "index.html").write_text(html)
    print("  explore/index.html")

    print(f"\nDone. {len(papers_full)} papers, {len(streams_list)} streams → docs/")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Build the static site from content/ → docs/")
    parser.add_argument("--clean", action="store_true", help="Wipe docs/ before building")
    args = parser.parse_args()
    render_site(clean=args.clean)


if __name__ == "__main__":
    main()

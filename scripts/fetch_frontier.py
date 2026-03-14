#!/usr/bin/env python3
"""
fetch_frontier.py — Fetch recent papers from arXiv for a given stream.

Uses keywords defined in data/streams.yaml to search arXiv for candidate papers.
Outputs a list of candidates for manual review or LLM triage.

Usage:
    python scripts/fetch_frontier.py --stream agents-as-advisors --months 3
    python scripts/fetch_frontier.py --stream belief-elicitation --months 6 --max-results 50
"""

import argparse
import json
import time
from datetime import datetime, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"


def load_stream_keywords(stream_id: str) -> list[str]:
    """Load search keywords for a stream from streams.yaml."""
    streams_path = DATA_DIR / "streams.yaml"
    with open(streams_path) as f:
        data = yaml.safe_load(f)

    streams = data.get("streams", data) if isinstance(data, dict) else data
    for stream in streams:
        if stream["id"] == stream_id:
            return stream.get("keywords", [])

    raise ValueError(f"Stream '{stream_id}' not found in {streams_path}")


def search_arxiv(keywords: list[str], max_results: int = 30, months: int = 3) -> list[dict]:
    """Search arXiv for recent papers matching keywords."""
    try:
        import arxiv
    except ImportError:
        print("Error: arxiv package not installed. Run: pip install arxiv")
        return []

    # Build query from keywords
    keyword_queries = [f'abs:"{kw}"' for kw in keywords[:6]]  # Limit to avoid query length issues
    query = " OR ".join(keyword_queries)

    # Relevant arXiv categories
    categories = ["cs.AI", "cs.HC", "cs.LG", "econ.GN", "q-fin.GN", "stat.AP"]
    cat_filter = " OR ".join(f"cat:{c}" for c in categories)
    full_query = f"({query}) AND ({cat_filter})"

    print(f"Query: {full_query[:120]}...")

    client = arxiv.Client()
    search = arxiv.Search(
        query=full_query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    cutoff = datetime.now() - timedelta(days=months * 30)
    results = []

    for paper in client.results(search):
        if paper.published.replace(tzinfo=None) < cutoff:
            continue
        results.append({
            "arxiv_id": paper.entry_id.split("/")[-1],
            "title": paper.title,
            "authors": [a.name for a in paper.authors],
            "abstract": paper.summary,
            "published": paper.published.isoformat(),
            "categories": paper.categories,
            "url": paper.entry_id,
            "pdf_url": paper.pdf_url,
        })
        time.sleep(0.5)  # Rate limit

    return results


def main():
    parser = argparse.ArgumentParser(description="Fetch recent arXiv papers for a stream")
    parser.add_argument("--stream", required=True, help="Stream ID slug")
    parser.add_argument("--months", type=int, default=3, help="How many months back to search")
    parser.add_argument("--max-results", type=int, default=30, help="Max results to fetch")
    parser.add_argument("--output", type=Path, default=None, help="Output JSON path")
    args = parser.parse_args()

    print(f"Stream: {args.stream}")
    print(f"Period: last {args.months} months")

    keywords = load_stream_keywords(args.stream)
    print(f"Keywords: {keywords}")

    results = search_arxiv(keywords, max_results=args.max_results, months=args.months)
    print(f"Found {len(results)} candidate papers")

    # Write output
    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = args.output or OUTPUT_DIR / f"frontier_{args.stream}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Written to: {out_path}")

    # Print summary
    if results:
        print("\n--- Candidates ---")
        for r in results[:10]:
            print(f"  [{r['arxiv_id']}] {r['title']}")
            print(f"    {', '.join(r['authors'][:3])}{'...' if len(r['authors']) > 3 else ''}")
            print()
        if len(results) > 10:
            print(f"  ... and {len(results) - 10} more. See {out_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
add_paper.py — Scaffold a new paper digest and register it in data/papers.yaml.

Usage:
  python scripts/add_paper.py --id dietvorst-2015 \
    --title "Algorithm Aversion" \
    --authors "Dietvorst, Simmons & Massey" \
    --year 2015 \
    --venue "J. Exp. Psych: General" \
    --streams ai-agents \
    --evidence strong \
    --status canonical \
    --doi "https://doi.org/10.1037/xge0000033"

This creates:
  1. docs/content/papers/dietvorst-2015.html from scripts/paper_template.html
  2. Appends an entry to data/papers.yaml
  3. Prints a reminder to fill in the digest sections and rebuild papers.js

After filling in the digest, run:
  python scripts/build_papers_js.py    # regenerates docs/assets/js/papers.js from data/papers.yaml
"""

import argparse
import os
import sys
import yaml
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EV_MAP = {"strong": ("ev-strong", "Strong"), "mixed": ("ev-mixed", "Mixed"), "weak": ("ev-weak", "Weak")}
ST_MAP = {"canonical": ("st-canonical", "Canonical"), "debated": ("st-debated", "Debated"), "emerging": ("st-emerging", "Emerging")}
STREAM_NAMES = {
    "belief-elicitation": "Belief Elicitation & Calibration",
    "uncertainty-communication": "Uncertainty Communication",
    "decision-quality": "Decision Quality & Normative Benchmarks",
    "attention-salience": "Attention, Memory & Salience",
    "risk-ambiguity": "Risk, Ambiguity & Controllability",
    "temporal-dynamics": "Temporal Dynamics",
    "sampling-experience": "Sampling, Granularity & Experience",
    "ai-agents": "AI Agents as Decision Partners",
}

def main():
    parser = argparse.ArgumentParser(description="Scaffold a paper digest")
    parser.add_argument("--id", required=True, help="Slug, e.g. dietvorst-2015")
    parser.add_argument("--title", required=True)
    parser.add_argument("--authors", required=True, help="Short author string")
    parser.add_argument("--authors-full", default=None, help="Full author list (defaults to --authors)")
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--venue", default="")
    parser.add_argument("--streams", nargs="+", required=True, choices=list(STREAM_NAMES.keys()))
    parser.add_argument("--evidence", required=True, choices=["strong", "mixed", "weak"])
    parser.add_argument("--status", required=True, choices=["canonical", "debated", "emerging"])
    parser.add_argument("--doi", default="")
    args = parser.parse_args()

    authors_full = args.authors_full or args.authors
    ev_class, ev_label = EV_MAP[args.evidence]
    st_class, st_label = ST_MAP[args.status]

    # Generate stream chips HTML
    chips = []
    for s in args.streams:
        chips.append(f'<a class="xref-chip" href="../topics/{s}.html">{STREAM_NAMES[s]}</a>')
    chips_html = "\n  ".join(chips)

    # Read template
    tmpl_path = os.path.join(ROOT, "scripts", "paper_template.html")
    with open(tmpl_path) as f:
        template = f.read()

    # Fill template
    html = template.replace("{{TITLE}}", args.title)
    html = html.replace("{{AUTHORS_SHORT}}", args.authors)
    html = html.replace("{{AUTHORS_FULL}}", authors_full)
    html = html.replace("{{YEAR}}", str(args.year))
    html = html.replace("{{VENUE}}", args.venue)
    html = html.replace("{{DOI_URL}}", args.doi)
    html = html.replace("{{EV_CLASS}}", ev_class)
    html = html.replace("{{EV_LABEL}}", ev_label)
    html = html.replace("{{ST_CLASS}}", st_class)
    html = html.replace("{{ST_LABEL}}", st_label)
    html = html.replace("{{STREAM_CHIPS}}", chips_html)

    # Placeholder sections
    for field in ["DESIGN_HTML", "FINDINGS_HTML", "DEPENDENCE_HTML", "QUALIFICATIONS_HTML", "VERDICT_HTML"]:
        html = html.replace("{{" + field + "}}", f"  <p>TODO: Fill in {field.lower().replace('_', ' ')}</p>")

    # Write HTML
    out_path = os.path.join(ROOT, "docs", "content", "papers", f"{args.id}.html")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(html)
    print(f"Created: {out_path}")

    # Append to papers.yaml
    yaml_path = os.path.join(ROOT, "data", "papers.yaml")
    entry = {
        "id": args.id,
        "title": args.title,
        "authors": args.authors,
        "year": args.year,
        "venue": args.venue,
        "streams": args.streams,
        "evidence": args.evidence,
        "status": args.status,
        "doi": args.doi,
        "verdict": "TODO",
        "qualification": "TODO",
        "added": datetime.now().strftime("%Y-%m-%d"),
    }

    papers = []
    if os.path.exists(yaml_path):
        with open(yaml_path) as f:
            papers = yaml.safe_load(f) or []
    papers.append(entry)
    with open(yaml_path, "w") as f:
        yaml.dump(papers, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    print(f"Registered in: {yaml_path}")

    print(f"\nNext steps:")
    print(f"  1. Edit {out_path} — fill in design, findings, dependence, qualifications, verdict")
    print(f"  2. Edit {yaml_path} — fill in verdict and qualification fields")
    print(f"  3. Run: python scripts/build_papers_js.py")

if __name__ == "__main__":
    main()

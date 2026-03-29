#!/usr/bin/env python3
"""
build_papers_js.py — Generate docs/assets/js/papers.js from data/papers.yaml.

This is the single source of truth for the paper database. The YAML file is
human-editable; this script converts it to the JS format the explore page consumes.

Usage:
  python scripts/build_papers_js.py
"""

import os
import json
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YAML_PATH = os.path.join(ROOT, "data", "papers.yaml")
JS_PATH = os.path.join(ROOT, "docs", "assets", "js", "papers.js")

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

STREAM_COLORS = {
    "belief-elicitation": "#3572A5",
    "uncertainty-communication": "#2A9D8F",
    "decision-quality": "#E76F51",
    "attention-salience": "#9B59B6",
    "risk-ambiguity": "#DC4C64",
    "temporal-dynamics": "#2E86AB",
    "sampling-experience": "#D4A017",
    "ai-agents": "#264653",
}

def main():
    with open(YAML_PATH) as f:
        papers = yaml.safe_load(f)

    js_entries = []
    for p in papers:
        # Check if a digest HTML exists
        digest_path = os.path.join(ROOT, "docs", "content", "papers", f"{p['id']}.html")
        has_digest = os.path.exists(digest_path)

        entry = {
            "t": p["title"],
            "a": p["authors"],
            "y": p["year"],
            "s": p["streams"],
            "ev": p["evidence"],
            "st": p["status"],
            "v": p.get("verdict", ""),
            "q": p.get("qualification", ""),
        }
        if has_digest:
            entry["u"] = f"content/papers/{p['id']}.html"

        js_entries.append(entry)

    # Write JS
    lines = ["const PAPERS=["]
    for e in js_entries:
        lines.append(json.dumps(e, ensure_ascii=False) + ",")
    lines.append("];")
    lines.append("")
    lines.append(f"const STREAM_NAMES={json.dumps(STREAM_NAMES)};")
    lines.append(f"const STREAM_COLORS={json.dumps(STREAM_COLORS)};")
    lines.append('const EV_CLASS={"strong":"ev-strong","mixed":"ev-mixed","weak":"ev-weak"};')
    lines.append('const ST_CLASS={"canonical":"st-canonical","debated":"st-debated","emerging":"st-emerging"};')

    with open(JS_PATH, "w") as f:
        f.write("\n".join(lines))

    print(f"Generated {JS_PATH}")
    print(f"  {len(js_entries)} papers")
    print(f"  {sum(1 for e in js_entries if 'u' in e)} with digest pages")

if __name__ == "__main__":
    main()

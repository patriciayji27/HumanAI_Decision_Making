#!/usr/bin/env python3
"""
add_paper.py — Create a new paper digest from the template.

Usage:
    python scripts/add_paper.py --id kahneman-tversky-1979
    python scripts/add_paper.py --id smith-2024 --stream agents-as-advisors --era frontier
"""

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "content" / "papers" / "_template.md"
PAPERS_DIR = ROOT / "content" / "papers"

VALID_STREAMS = [
    "belief-elicitation",
    "uncertainty-communication",
    "utility-decision-quality",
    "attention-memory-salience",
    "risk-ambiguity",
    "temporal-dynamics",
    "sampling-representation",
    "agents-as-advisors",
]

VALID_ERAS = ["foundational", "key-development", "frontier"]


def validate_id(paper_id: str) -> bool:
    return bool(re.match(r"^[a-z0-9][a-z0-9-]*$", paper_id))


def main():
    parser = argparse.ArgumentParser(description="Create a new paper digest from template")
    parser.add_argument("--id", required=True, help="Paper ID slug (e.g., author-year)")
    parser.add_argument("--stream", default=None, help="Primary stream slug")
    parser.add_argument("--era", default="frontier", choices=VALID_ERAS)
    args = parser.parse_args()

    if not validate_id(args.id):
        print(f"Error: Invalid paper ID '{args.id}'. Use lowercase letters, numbers, hyphens only.")
        return

    if args.stream and args.stream not in VALID_STREAMS:
        print(f"Error: Unknown stream '{args.stream}'. Valid streams:")
        for s in VALID_STREAMS:
            print(f"  - {s}")
        return

    target = PAPERS_DIR / f"{args.id}.md"

    if target.exists():
        print(f"Error: {target} already exists.")
        return

    if not TEMPLATE.exists():
        print(f"Error: Template not found at {TEMPLATE}")
        return

    # Copy template and customize
    content = TEMPLATE.read_text()
    content = content.replace("id: author-year", f"id: {args.id}")
    content = content.replace("era: frontier", f"era: {args.era}")

    if args.stream:
        content = content.replace("  - primary-stream", f"  - {args.stream}")

    target.write_text(content)
    print(f"Created: {target}")
    print(f"  ID:     {args.id}")
    print(f"  Era:    {args.era}")
    if args.stream:
        print(f"  Stream: {args.stream}")
    print(f"\nNext steps:")
    print(f"  1. Edit {target} — fill in all fields")
    print(f"  2. Add entry to data/papers.yaml")
    print(f"  3. Run: python scripts/build_site.py")


if __name__ == "__main__":
    main()

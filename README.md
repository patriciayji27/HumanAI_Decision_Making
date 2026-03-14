# Human-Agent Decision Making — Research Digest & Concept Archive

A **topic-organized** research archive and paper digest at the intersection of cognitive science and AI agents — focused on how humans represent, elicit, communicate, and act on uncertainty, and how interfaces and AI agents shape the gap between observed behavior and well-calibrated, utility-consistent choice.

## Why This Exists

Research on human decision-making under uncertainty is scattered across cognitive psychology, behavioral economics, judgment & decision making, HCI, and AI. This archive organizes it by **research direction** — not by date or venue — so you can:

- **Orient quickly**: land on a topic and understand its foundations, turning points, and frontier in minutes
- **Digest efficiently**: every paper has a structured summary with consistent fields
- **See connections**: papers are cross-referenced across topics, so you see how prospect theory connects to belief elicitation connects to AI advisor design
- **Track evolution**: each topic traces from foundational work → key developments → current frontier

## Topic Streams

| # | Stream | Core Question |
|---|--------|---------------|
| 1 | [Belief Elicitation & Calibration](content/topics/belief-elicitation.md) | How do we extract what people actually believe, and how well-calibrated are those beliefs? |
| 2 | [Uncertainty Communication](content/topics/uncertainty-communication.md) | How should uncertainty be presented so people understand and act on it? |
| 3 | [Utility, Decision Quality & Normative Benchmarks](content/topics/utility-decision-quality.md) | How do we measure what people value, and are their choices "good" by their own standards? |
| 4 | [Attention, Memory, Salience & Cognitive Load](content/topics/attention-memory-salience.md) | How do interfaces shape what people notice, remember, and weigh? |
| 5 | [Risk, Ambiguity & Controllability](content/topics/risk-ambiguity.md) | How do people process different types and sources of uncertainty? |
| 6 | [Temporal Dynamics: Myopia, Feedback & Time Horizon](content/topics/temporal-dynamics.md) | How does feedback timing, evaluation frequency, and planning horizon shape risk-taking? |
| 7 | [Sampling, Granularity, Tails & Uncertainty Representation](content/topics/sampling-representation.md) | How do people learn about distributions from experience, and how does format affect judgment? |
| 8 | [AI Agents as Elicitors, Explainers & Calibrated Advisors](content/topics/agents-as-advisors.md) | How can LLMs and AI agents serve as partners in human decision-making? |

## Paper Digest Format

Every paper in the archive gets a structured digest with: one-line summary, core contribution, key concepts (with descriptions), methodology, limitations, legacy/influence, and optional personal reading notes. Papers are tagged by stream and era (`foundational` / `key-development` / `frontier`).

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full digest schema and how to add papers.

## Project Structure

```
├── content/
│   ├── topics/          # One Markdown file per research stream
│   └── papers/          # One Markdown file per paper digest
├── data/
│   ├── papers.yaml      # Master paper registry (metadata + tags)
│   └── streams.yaml     # Stream definitions and relationships
├── docs/                # GitHub Pages static site (generated)
├── scripts/             # Build, add-paper, fetch-frontier tools
├── prompts/             # LLM prompt templates for paper processing
├── schemas/             # JSON schema for data validation
└── configs/             # Site and pipeline configuration
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Build the static site from content/
python scripts/build_site.py

# Add a new paper (creates a template)
python scripts/add_paper.py --id author-year

# Generate a digest from a PDF (LLM-assisted, requires API key)
python scripts/digest_paper.py --pdf path/to/paper.pdf --stream utility-decision-quality

# Scan arXiv for recent frontier papers in a stream
python scripts/fetch_frontier.py --stream agents-as-advisors --months 3
```

## Website

The archive is published as a static site via GitHub Pages at the `docs/` directory.

- **Landing page**: topic map + stats + featured paper
- **Topic pages**: concept overview → evolution timeline → paper digests → open questions
- **Paper pages**: full structured digest for each paper
- **Explore**: search and filter across all papers by stream, era, year, tags

## License

This repository is a personal research archive. Paper digests are original summaries, not reproductions of copyrighted content.

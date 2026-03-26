# Contributing to the Archive

This document explains how to add papers, extend topic streams, and maintain the archive.

## Adding a Paper

### Option A: Manual (recommended for foundational papers)

1. Create a new file in `content/papers/` named `{author}-{year}.md` (e.g., `kahneman-tversky-1979.md`)
2. Copy the template from `content/papers/_template.md`
3. Fill in all fields — see the digest schema below
4. Add the paper to `data/papers.yaml`
5. Rebuild the site: `python scripts/build_site.py`

### Option B: LLM-assisted (for frontier papers)

```bash
python scripts/digest_paper.py --pdf path/to/paper.pdf --stream utility-decision-quality
```

This generates a draft digest that you **must review and edit** before committing. The LLM provides a starting point, not a final product.

### Option C: Interactive scaffold

```bash
python scripts/add_paper.py --id dietvorst-2015
```

Creates the file with the template pre-filled with the ID. You fill in the rest.

## Paper Digest Schema

Every paper digest uses this YAML front matter followed by Markdown body:

```yaml
---
id: author-year                     # Unique slug (lowercase, hyphens)
title: "Full Paper Title"
authors:
  - First Author
  - Second Author
year: 2024
venue: "Journal or Conference Name"
url: "https://doi.org/..."
pdf_url: ""                         # Direct PDF link if available
streams:                            # Which topic streams (1+ required)
  - primary-stream-slug
  - secondary-stream-slug
era: frontier                       # foundational | key-development | frontier
tags:                               # Free-form tags for search/filter
  - tag-one
  - tag-two
---
```

The Markdown body uses these sections (all required unless marked optional):

```markdown
## One-Line Summary
> Single sentence capturing the paper's core contribution.

## Core Contribution
2–3 sentences on what this paper fundamentally added to the field.

## Key Concepts
### Concept Name
Description of the concept and why it matters.

### Another Concept
Description.

## Methodology
How the study was conducted — design, participants, analysis approach.

## Key Findings
The main empirical or theoretical results.

## Limitations
What the paper doesn't address or where its claims are bounded.

## Legacy & Influence
How this paper's ideas propagated. Which subsequent work builds on it.
What it means for the human-agent decision making agenda.

## Reading Notes *(optional)*
Personal annotations, connections to other papers, implications for your work.
```

## Paper Naming Convention

- Use `{first-author-lastname}-{year}` as the base: `kahneman-tversky-1979`
- For disambiguation: `kahneman-tversky-1979-prospect` vs `kahneman-tversky-1979-other`
- All lowercase, hyphens only, no special characters

## Registering in papers.yaml

After creating the paper file, add an entry to `data/papers.yaml`:

```yaml
- id: kahneman-tversky-1979
  title: "Prospect Theory: An Analysis of Decision Under Risk"
  authors: [Daniel Kahneman, Amos Tversky]
  year: 1979
  venue: Econometrica
  streams: [utility-decision-quality, belief-elicitation, risk-ambiguity, sampling-representation]
  era: foundational
  tags: [prospect-theory, value-function, probability-weighting, loss-aversion]
```

## Adding or Modifying a Topic Stream

Topic stream files live in `content/topics/{stream-slug}.md`. Each has:

1. **YAML front matter** with stream metadata
2. **Concept Overview** section
3. **Evolution Timeline** section
4. **Open Questions** section

Paper digests are linked automatically by the build script based on the `streams` field in each paper's front matter.

Stream definitions in `data/streams.yaml` control navigation, colors, and search keywords.

## Building the Site

```bash
python scripts/build_site.py
```

This reads all files in `content/` and `data/`, renders them with the templates, and writes to `docs/`. The `docs/` directory is what GitHub Pages serves.

## Conventions

- All content files are Markdown with YAML front matter
- All data files are YAML (not JSON) for readability
- The `docs/` directory is generated — never edit it directly
- Commit content changes and regenerated `docs/` together
- Use present tense in digests ("proposes", "shows", "finds")
- Keep one-line summaries under 30 words

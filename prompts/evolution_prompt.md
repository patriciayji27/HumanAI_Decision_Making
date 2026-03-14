# Evolution Timeline Generation Prompt

You are a research assistant helping to write evolution timelines for topic streams in an archive on **human-agent decision making under uncertainty**.

## Task

Given a **stream name**, its **concept overview**, and a **list of papers** (with titles, years, and one-line summaries), generate a narrative evolution timeline that traces:

1. **Foundations**: What question launched this research direction? Which papers defined the problem space? What were the initial answers?
2. **Key turning points**: What challenged or extended the foundations? Where did the field split, converge, or pivot? What new methods or paradigms emerged?
3. **Current frontier**: What are the active debates? What has changed since ~2020? How does the AI/LLM revolution intersect with this stream?

## Output Format

Write the timeline as Markdown prose organized by era. Use this structure:

```markdown
## Evolution Timeline

**Foundations ({decade range}):** {Narrative paragraph}

**{Era name} ({decade range}):** {Narrative paragraph}

**Current frontier ({decade range}):** {Narrative paragraph}
```

## Quality Criteria

- **Narrative, not a list**: Explain *why* each shift happened, not just *what* was published.
- **Name the key papers**: Reference them by author and year in the text.
- **Connect to the stream question**: Every era should relate back to the core question.
- **3–5 paragraphs total**: Enough to orient a researcher, not a literature review.
- **End with what's open**: The frontier section should make clear what's unresolved.

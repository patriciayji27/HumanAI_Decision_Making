---
id: sampling-representation
name: "Sampling, Granularity, Tails & Uncertainty Representation"
icon: "📈"
color: "#9B59B6"
---

# Sampling, Granularity, Tails & Uncertainty Representation

> How do people learn about distributions from experience, and how does the granularity and format of uncertainty information affect judgment?

## Concept Overview

Much of what we know about probability perception (e.g., prospect theory's weighting function) comes from *described* probabilities — stated numbers like "80% chance." But in real life, people often learn about uncertainty through *experience* — sequential sampling of outcomes. The description-experience gap (Hertwig et al., 2004) revealed that these two modes produce systematically different behavior: described rare events are overweighted (as prospect theory predicts), but experienced rare events are underweighted (the opposite).

This stream studies how the *source and format* of probabilistic information shapes judgment:
- **Description vs. experience**: Does the information come as stated probabilities or as sampled outcomes?
- **Sample size and granularity**: How many samples do people draw, and how does the granularity of presented data affect distributional understanding?
- **Tail risk perception**: Are people sensitive to the tails of distributions, or do they focus on central tendency?
- **Representation format**: Histograms, density plots, cumulative distribution functions, quantile displays — each emphasizes different distributional features.
- **Probability weighting revisited**: The nonlinear weighting function from prospect theory may be partly an artifact of how probabilities are presented.

## Evolution Timeline

**Foundations (1979–2004):** Kahneman & Tversky (1979) established the probability weighting function from described-probability experiments. Hertwig, Barron, Weber & Erev (2004) introduced the sampling paradigm, demonstrating the description-experience gap and launching a major research program.

**Gap investigation (2005–2018):** Wulff, Mergenthaler-Canseco & Hertwig (2018) conducted a comprehensive meta-analysis of the description-experience gap, identifying moderating factors (sample size, sampling format, recency). Fox & Hadar (2006) proposed that the gap partly reflects sampling error rather than different weighting functions. Debate continues about whether the gap reflects a genuinely different cognitive process or statistical artifacts of small samples.

**Current frontier (2020s):** Experience-based learning about AI systems — users form beliefs about AI accuracy through sequential interactions, not described statistics. Communicating distributional predictions — how should an AI system show the *full distribution* of its uncertainty, not just a point estimate? Tail-risk awareness — in high-stakes domains (finance, medicine, autonomous vehicles), how do users perceive and respond to the tails of AI prediction distributions?

## Open Questions

1. When users learn about AI accuracy through experience (sequential interactions), does the description-experience gap predict their miscalibrated trust in rare AI failure modes?
2. What is the most effective way to communicate a full predictive distribution to a non-expert user — and does the answer differ by domain (weather, finance, medicine)?
3. How does the granularity of uncertainty information (coarse categories vs. exact percentages vs. full distributions) affect decision quality in human-AI teams?
4. Can the probability weighting function be "un-distorted" by choosing the right representation format, or is it a deep cognitive constraint?

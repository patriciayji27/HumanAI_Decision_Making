---
id: temporal-dynamics
name: "Temporal Dynamics: Myopia, Feedback & Time Horizon"
icon: "⏳"
color: "#FFB347"
---

# Temporal Dynamics: Myopia, Feedback & Time Horizon

> How does the temporal structure of decisions — feedback timing, evaluation frequency, planning horizon — shape risk-taking and learning?

## Concept Overview

Decisions don't happen in a temporal vacuum. How often you check your portfolio, how quickly you get feedback on a choice, and whether you're thinking about tomorrow or next decade all shape risk-taking behavior — often dramatically.

Myopic loss aversion (Benartzi & Thaler, 1995) demonstrated that loss-averse investors who evaluate returns frequently take less risk than those who evaluate infrequently, because frequent evaluation increases the salience of short-term losses. This connects prospect theory's loss aversion to the temporal structure of decision-making.

This stream covers:
- **Evaluation frequency effects**: How often you look matters as much as what you see.
- **Feedback timing and learning**: Immediate vs. delayed feedback creates different learning dynamics — relevant for learning about AI system accuracy.
- **Time discounting and present bias**: Preferring smaller-sooner over larger-later rewards; implications for decisions with delayed consequences.
- **Dynamic reference points**: How reference points update over time as people experience gains and losses.
- **Exploration-exploitation**: In sequential choice, balancing information gathering with reward maximization.

## Evolution Timeline

**Foundations (1990s):** Benartzi & Thaler (1995) proposed myopic loss aversion to explain the equity premium puzzle. Gneezy & Potters (1997) experimentally confirmed that evaluation frequency causally affects risk-taking. Thaler et al. (1997) extended the finding to investment decisions.

**Experience-based learning (2000s):** Hertwig et al. (2004) introduced the description-experience gap — showing that sampling-based learning leads to underweighting of rare events (the opposite of what prospect theory predicts from described probabilities). This opened a major research program on how temporal experience shapes probability perception.

**Current frontier (2020s):** Feedback design in AI-assisted decisions — should AI systems provide outcome feedback after every decision, or aggregate it? Temporal framing in algorithmic recommendations — do users evaluate AI accuracy over individual predictions or streaks? Human learning dynamics with AI — how quickly do users update their trust in an AI system after errors, and does this follow Bayesian or prospect-theoretic dynamics?

## Open Questions

1. When users interact with AI advisors over time, do they evaluate AI accuracy myopically (per-prediction) or aggregate (over sessions)? How does this affect trust dynamics?
2. Can the description-experience gap explain why users' lab-tested reactions to AI uncertainty differ from their real-world behavior with AI systems?
3. What is the optimal feedback frequency for AI-assisted decisions — does frequent feedback help calibrate trust or induce myopic over-reaction to individual AI errors?
4. How do dynamic reference points work in human-AI teams — if an AI advisor has been consistently good, does a single error loom larger (due to a shifted reference point)?

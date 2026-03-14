---
id: uncertainty-communication
name: "Uncertainty Communication: Visual, Textual, Agent-Mediated"
icon: "📊"
color: "#7B68EE"
---

# Uncertainty Communication: Visual, Textual, Agent-Mediated

> How should uncertainty be presented so people understand it and act on it well?

## Concept Overview

Even perfectly calibrated beliefs are useless if the decision-maker can't absorb the uncertainty information presented to them. This stream studies the *downstream* problem: given that a system (forecaster, model, AI agent) has a probabilistic prediction, how should it communicate that uncertainty so the recipient understands and uses it appropriately?

The answer depends heavily on format. Error bars, confidence intervals, fan charts, icon arrays, hypothetical outcome plots, and verbal probability expressions all convey uncertainty — but they are not interchangeable. Each format foregrounds different aspects of a distribution and interacts with the recipient's numeracy, domain knowledge, and cognitive style.

Key distinctions in this stream:
- **Visual vs. textual vs. agent-mediated**: Visualizations can convey distributional shape at a glance; text is precise but invites verbal-to-numeric translation errors; agent-mediated communication (conversational AI) can adapt in real time.
- **Static vs. interactive**: Static displays commit to a single representation; interactive displays (e.g., hypothetical outcome plots, user-controlled simulations) let users explore.
- **Frequency vs. probability framing**: Presenting "3 out of 100" vs. "3%" can dramatically change understanding, especially in medical risk communication.

## Evolution Timeline

**Foundations (1990s–2000s):** Gigerenzer and Hoffrage (1995) showed that natural frequency formats dramatically improve Bayesian reasoning compared to probability formats. Lipkus (2007) documented how numeracy moderates the effectiveness of risk communication formats. This era established that format is not neutral — it's a design variable with causal effects on comprehension.

**Visualization era (2010s):** Spiegelhalter, Pearson & Short (2011) catalogued uncertainty visualization approaches and their trade-offs. Hullman et al. (2015) introduced hypothetical outcome plots (HOPs), which animate draws from a distribution rather than showing static summaries. Fernandes et al. (2018) conducted a large meta-review of uncertainty visualization effectiveness.

**Current frontier (2020s):** Agent-mediated uncertainty communication — LLMs explaining model confidence in natural language, adapting explanations to user questions. Open challenges include: preventing overconfidence from fluent AI explanations, calibrating the language of uncertainty ("likely" means different probabilities to different people), and designing interactive uncertainty exploration interfaces that work for non-expert users.

## Open Questions

1. When an LLM says "I'm fairly confident that..." — how do users decode that verbal probability, and does it systematically differ from the model's actual calibration?
2. Can interactive uncertainty displays (e.g., HOPs, distribution builders) be integrated into AI-assisted decision workflows without overwhelming users?
3. How should uncertainty communication adapt to the user's numeracy level in real time, and can AI agents detect numeracy from conversational cues?
4. What is the relationship between uncertainty *comprehension* (understanding the distribution) and uncertainty *use* (incorporating it into decisions)? Are they separable?

---
id: belief-elicitation
name: "Belief Elicitation & Calibration"
icon: "🎯"
color: "#4A90D9"
---

# Belief Elicitation & Calibration

> How do we extract what people actually believe under uncertainty, and how well-calibrated are those beliefs?

## Concept Overview

Before anyone can make a good decision under uncertainty, they need beliefs — probabilities, distributions, or at least ordinal likelihoods about relevant outcomes. But beliefs don't come pre-packaged. They must be *elicited*, and the elicitation method shapes what you get.

This stream covers the full pipeline: the mathematical foundations of proper elicitation (scoring rules that incentivize truthful reporting), the psychological realities that complicate it (people can't introspect on their beliefs directly), the interface mechanisms that operationalize it (sliders, wheels, distribution builders, verbal scales), and the question of calibration — whether stated beliefs track actual frequencies.

Key tensions in this stream:
- **Incentive compatibility vs. cognitive accessibility**: Proper scoring rules are incentive-compatible but cognitively demanding. Simpler interfaces are accessible but may distort reports.
- **Point estimates vs. full distributions**: Most tasks elicit point probabilities; real uncertainty is distributional.
- **Calibration vs. resolution**: Being well-calibrated (your 70% events happen 70% of the time) is different from being well-resolved (your 90% events are different from your 60% events).

## Evolution Timeline

**Foundations (1950s–1980s):** The mathematical theory of proper scoring rules (Brier 1950, Savage 1971) established that certain reward structures incentivize truthful probability reports. Concurrently, the calibration literature (Lichtenstein, Fischhoff & Phillips 1982) documented systematic overconfidence — people's stated 90% confidence intervals contain the truth far less than 90% of the time.

**Mechanism design era (1990s–2010s):** Focus shifted to designing practical elicitation mechanisms. Distribution builders (Goldstein & Rothschild 2014) let people construct full probability distributions through interactive interfaces. Work on the "matching probability" method and binary lottery procedures attempted to bridge theory and practice.

**Current frontier (2020s):** Three active threads: (1) LLM-assisted elicitation — using conversational agents to help people articulate beliefs they struggle to quantify; (2) eliciting beliefs about AI systems — how confident should a user be in a model's prediction?; (3) calibration training and debiasing — can interactive feedback improve real-world calibration?

## Open Questions

1. Can conversational AI agents elicit better-calibrated beliefs than traditional interfaces (sliders, wheels), and if so, is the improvement from better introspective access or social desirability effects?
2. How should elicitation methods adapt when the target belief is about an AI model's output — a domain where people have little base-rate experience?
3. What is the right trade-off between elicitation granularity (full distributions) and cognitive cost, especially in time-pressured or high-stakes settings?
4. How do different elicitation formats interact with the probability weighting documented in prospect theory (see: utility-decision-quality)?

---
id: utility-decision-quality
name: "Utility Elicitation, Decision Quality & Normative Benchmarks"
icon: "⚖️"
color: "#E8833A"
---

# Utility Elicitation, Decision Quality & Normative Benchmarks

> How do we measure what people value, and how do we assess whether their choices are "good" by their own standards?

## Concept Overview

This is the normative and descriptive center of the archive. Expected utility theory provides the benchmark: a rational agent maximizes the expected value of a utility function over final wealth states. But people don't do this. They evaluate changes from reference points, weight probabilities nonlinearly, are loss-averse, and are sensitive to framing. Prospect theory (Kahneman & Tversky, 1979) formalized these deviations and became the dominant descriptive model.

The stream covers three interrelated problems:

1. **Descriptive models**: How do people actually choose under risk? What are the systematic deviations from expected utility? (Prospect theory, regret theory, salience theory, etc.)
2. **Utility/preference elicitation**: How do we measure what people value? Certainty equivalents, choice-based methods, trade-off methods, and their biases.
3. **Decision quality**: Given that choices deviate from normative benchmarks, how do we assess whether a person's decisions are "good" — not by an external standard, but by their own well-calibrated preferences?

The third problem is especially relevant for human-agent decision making: if an AI advisor helps someone make "better" decisions, better by whose standard? The answer requires separating genuine preferences (which should be respected) from processing errors (which interfaces and advisors should help correct).

## Evolution Timeline

**Foundations (1940s–1970s):** von Neumann & Morgenstern (1944) axiomatized expected utility. Allais (1953) immediately demonstrated systematic violations (the common consequence effect). Kahneman & Tversky (1979) proposed prospect theory with its S-shaped value function, nonlinear probability weighting, and reference dependence. Raiffa (1968) developed prescriptive decision analysis — tools to help people make decisions consistent with their own values.

**Refinement and measurement (1980s–2000s):** Tversky & Kahneman (1992) extended to cumulative prospect theory with rank-dependent weighting. Bleichrodt et al. (2001) developed methods for measuring utility under prospect theory. The decision quality movement (Howard, 1988) proposed frameworks for assessing decision processes rather than just outcomes.

**Behavioral integration era (2010s):** Koszegi & Rabin (2006, 2007) endogenized reference points using rational expectations. Bordalo, Gennaioli & Shleifer (2012) proposed salience theory as an attention-based alternative to prospect theory. Debate intensified about whether "biases" are errors or ecologically rational adaptations.

**Current frontier (2020s):** Automated preference learning — can AI systems learn individual utility functions from observed choices? AI-assisted decision analysis — can LLMs walk people through decision trees and trade-off elicitation? Measuring human-AI team decision quality — when does AI advice improve choices vs. introduce new biases?

## Open Questions

1. When an AI advisor "debiases" a human decision, how do we distinguish correcting a processing error from overriding a genuine preference (e.g., someone's actual risk attitude)?
2. Can preference elicitation methods be made robust to the very biases they're trying to measure? (e.g., if certainty equivalents are distorted by probability weighting, what do they actually recover?)
3. How should we evaluate decision quality in human-AI teams — should the benchmark be the human's own well-calibrated preferences, the AI's prediction, or some complementary combination?
4. Does prospect theory's editing phase have a modern analogue in how users pre-process AI-presented choice sets?

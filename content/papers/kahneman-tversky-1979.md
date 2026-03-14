---
id: kahneman-tversky-1979
title: "Prospect Theory: An Analysis of Decision Under Risk"
authors:
  - Daniel Kahneman
  - Amos Tversky
year: 1979
venue: Econometrica
url: "https://doi.org/10.2307/1914185"
pdf_url: ""
streams:
  - utility-decision-quality
  - risk-ambiguity
  - sampling-representation
  - belief-elicitation
era: foundational
tags:
  - prospect-theory
  - value-function
  - probability-weighting
  - loss-aversion
  - certainty-effect
  - reflection-effect
  - isolation-effect
  - reference-dependence
  - editing-phase
  - decision-weights
  - subcertainty
  - subproportionality
---

## One-Line Summary

> Proposes prospect theory as a descriptive alternative to expected utility, showing people evaluate outcomes as gains/losses from a reference point with nonlinear probability weighting.

## Core Contribution

Demonstrates through systematic choice experiments that people violate expected utility theory in predictable, structured ways — overweighting certain outcomes, reflecting risk preferences across gain/loss domains, and framing-dependent decomposition of prospects. Introduces a formal two-phase model (editing + evaluation) with an S-shaped value function defined on changes from a reference point and a nonlinear probability weighting function, providing the first comprehensive descriptive theory of risky choice.

## Key Concepts

### Value Function (v)

Defined on deviations from a reference point (gains and losses), not on final wealth states. Three key properties: (i) concave for gains (diminishing sensitivity to increasing gains), (ii) convex for losses (diminishing sensitivity to increasing losses), (iii) steeper for losses than for gains (loss aversion). The resulting S-shape is steepest at the reference point, contrasting with Markowitz's utility function which is shallow near zero.

### Decision Weights (π)

Probabilities are transformed by a weighting function π(p) that is not a probability measure. Key properties: overweights small probabilities (π(p) > p for small p), exhibits subcertainty (π(p) + π(1−p) < 1 for most p), and is subproportional (for a fixed ratio of probabilities, the ratio of decision weights is closer to unity when probabilities are low). The function is relatively flat in the interior and changes sharply near the endpoints (0 and 1).

### Certainty Effect

People overweight outcomes obtained with certainty relative to merely probable outcomes. This produces risk aversion in the gain domain (preferring a sure gain over a larger but uncertain one) and risk seeking in the loss domain (preferring a probable larger loss over a certain smaller loss). Demonstrated through variations of Allais' paradox.

### Reflection Effect

Preferences between negative prospects mirror preferences between positive prospects — reversing the sign of all outcomes reverses the preference order. Risk aversion for gains is accompanied by risk seeking for losses, and vice versa. This rules out general aversion to variance/uncertainty as the explanation for the certainty effect.

### Isolation Effect

People simplify choices by discarding components shared by all prospects and focusing on distinguishing components. Because the same choice can be decomposed differently, this leads to inconsistent preferences across equivalent formulations. Demonstrated through the two-stage game (Problem 10) where subjects ignored the common first stage, and through bonus problems (Problems 11–12) where subjects ignored a common endowment.

### Editing Phase

A preliminary phase where prospects are reorganized before evaluation, through operations including: coding (outcomes as gains/losses relative to a reference point), combination (merging identical-outcome probabilities), segregation (separating riskless from risky components), cancellation (discarding shared components), simplification (rounding), and dominance detection.

### Two Evaluation Equations

For regular prospects (mixed or small-probability): V(x,p; y,q) = π(p)v(x) + π(q)v(y). For strictly positive/negative prospects: V(x,p; y,q) = v(y) + π(p)[v(x) − v(y)], where the riskless component v(y) is not weighted by π. The second form means the theory is not purely expectation-based even with transformed weights.

### Reference Dependence

The carriers of value are changes in wealth, not final states. The same objective wealth position can yield different choices depending on the reference point — whether it was reached by gaining or losing. This is the cornerstone departure from expected utility theory's asset integration assumption.

## Methodology

Hypothetical choice experiments administered as questionnaires to university students and faculty (primarily in Israel, replicated at Stockholm and Michigan). Pairs of choice problems designed to isolate specific violations of expected utility axioms. Each problem pair holds outcomes or probabilities constant while varying the feature under test (e.g., certainty vs. probability, gains vs. losses, standard vs. sequential framing). Sample sizes typically 66–141 per problem. Multiple questionnaire forms with randomized problem order and left-right reversal of options.

## Key Findings

- 82% preferred a sure 2,400 over a higher-EV gamble (Problem 1), but 83% reversed when both options were made uncertain (Problem 2) — violating the independence axiom.
- Risk preferences mirror across domains: 80% chose the sure gain in (4000,.80) vs (3000), but 92% chose the gamble in (−4000,.80) vs (−3000).
- In the two-stage game, 78% chose as if ignoring the common first stage, producing different preferences than the mathematically equivalent one-stage version.
- Problems 11–12 show that adding a common bonus reverses preferences because subjects code outcomes as gains/losses from different reference points.
- 72% preferred a lottery ticket (5000,.001) over its expected value (5), while 83% preferred paying a sure (−5) over (−5000,.001) — consistent with overweighting of small probabilities.
- 80% rejected probabilistic insurance even when expected utility theory with concave u implies it should be preferred to standard insurance.

## Limitations

- Restricted to simple prospects with at most two non-zero outcomes and stated objective probabilities. Does not address multi-outcome, multi-attribute, or continuous distributions.
- All data from hypothetical choices — no real stakes. Authors acknowledge this limitation but argue hypothetical choices are the most practical method for systematic testing.
- The editing phase is described qualitatively, not formally axiomatized. The sequence of editing operations can affect outcomes, and the paper does not resolve this.
- Does not address the production task (e.g., bidding, pricing), which may yield different orderings than choice (cf. preference reversals).
- The weighting function π is not well-behaved near the endpoints, and the theory permits indirect violations of dominance (intransitive cycles).
- Limited to individual decision-making; no treatment of strategic interaction or social dimensions of choice.

## Legacy & Influence

The most cited paper in the history of economics (by some counts). Foundational for behavioral economics, behavioral finance, and the modern study of judgment and decision making. Direct descendants include:

- **Cumulative prospect theory** (Tversky & Kahneman, 1992): extended to continuous distributions, rank-dependent weighting, addressing some limitations.
- **Loss aversion** became a standalone concept applied to endowment effect, status quo bias, disposition effect in finance, labor supply, and insurance behavior.
- **Reference dependence** reshaped models of consumer behavior, labor economics, and contract theory (Koszegi & Rabin, 2006).
- **Probability weighting** informed models of insurance demand, gambling, tail-risk pricing, and the description-experience gap literature.
- **Framing and editing** connected to the broader program on heuristics and biases, and to choice architecture and nudge theory.
- For the human-agent decision making agenda: prospect theory's value function and weighting function are essential building blocks for understanding how people will respond to AI-presented risks, how interfaces should frame uncertain outcomes, and why elicited preferences may be inconsistent across equivalent formulations.

## Reading Notes

This paper is the foundational reference for nearly every stream in the archive. When reading any paper on risk communication, belief elicitation, or AI-advised decisions, the question is always: does the design account for reference dependence, loss aversion, and nonlinear probability weighting? If not, the results may conflate interface effects with these deeper choice patterns.

The editing phase is underappreciated — it's essentially a theory of how people pre-process decision problems before evaluation, which maps directly onto how interface design and AI framing affect choices (Stream 4, Stream 8). The isolation effect is particularly relevant for human-AI settings: when an AI presents options with shared components (e.g., shared baseline risk), users may cancel those out and evaluate only the differences, potentially missing the overall risk level.

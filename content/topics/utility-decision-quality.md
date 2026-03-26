---
id: utility-decision-quality
name: "Utility Elicitation, Decision Quality & Normative Benchmarks"
icon: "⚖️"
color: "#E8833A"
---

# Utility Elicitation, Decision Quality & Normative Benchmarks

> How do we measure what people value, and how do we assess whether their choices are "good" by their own standards?

## Concept Overview

This stream is the normative and descriptive center of the archive. It houses the models that define what rational choice *should* look like (expected utility theory), the empirical evidence about what choice *actually* looks like (prospect theory and its descendants), the methods for measuring individual preferences (utility elicitation), and the frameworks for assessing whether a decision was good (decision quality).

The intellectual structure rests on a trichotomy articulated by Bell, Raiffa, and Tversky (1988):

- **Normative**: How should an idealized rational agent choose? Answer: maximize expected utility, per the axioms of von Neumann and Morgenstern (1944) and Savage (1954).
- **Descriptive**: How do real people actually choose? Answer: they violate the normative axioms systematically — overweighting certainty, evaluating outcomes relative to reference points, treating gains and losses asymmetrically, and weighting probabilities nonlinearly.
- **Prescriptive**: How can we help real people make decisions that better reflect their own values? This is the domain of decision analysis (Raiffa, 1968) and, increasingly, of AI-assisted decision support.

The prescriptive leg is where this stream connects most directly to human-agent decision making. An AI advisor that "improves" decisions needs a benchmark — but whose? If the benchmark is expected utility, the advisor is imposing a normative model the person may not endorse. If the benchmark is the person's own revealed preferences, those preferences are riddled with framing effects and inconsistencies. The question of *what counts as a good decision* is not settled, and it matters enormously for how AI systems should be designed.

### Expected Utility Theory: The Normative Backbone

Expected utility theory (EUT) rests on three tenets, as laid out in the Kahneman and Tversky (1979) paper that anchors this archive:

1. **Expectation**: The utility of a prospect is the probability-weighted sum of the utilities of its outcomes: U = Σ pᵢu(xᵢ).
2. **Asset integration**: A prospect is evaluated by integrating it with the decision-maker's current wealth — the domain of the utility function is final states, not changes.
3. **Risk aversion via concavity**: A risk-averse person has a concave utility function (u'' < 0), preferring a sure amount over a gamble with the same expected value.

EUT's power is its axiomatic foundation. If a person's preferences satisfy a small set of axioms — completeness, transitivity, continuity, and independence — then there exists a utility function such that they behave *as if* maximizing expected utility. The independence axiom is the critical one: if you prefer A to B, you should prefer any probability mixture involving A to the same mixture involving B. This is the axiom that empirical research has most consistently refuted.

### The Violations: What Goes Wrong and How

The violations are not random noise. They are structured, replicable, and predictable:

**The Allais paradox / certainty effect**: People overweight outcomes obtained with certainty relative to merely probable outcomes. In Problems 1–2 of Kahneman and Tversky (1979), 82% preferred a sure 2,400 over a higher-EV gamble, but 83% reversed when both options were made uncertain — violating independence. The pattern holds across stakes, populations, and cultures. The underlying psychology is that the reduction from certainty to high probability feels larger than the same reduction deeper in the probability scale.

**The reflection effect**: Risk preferences mirror across the gain-loss boundary. People are risk-averse for gains (preferring a sure gain over a larger gamble) but risk-seeking for losses (preferring a gamble over a sure loss of equal expected value). This is incompatible with any single concave utility function and points to a fundamental asymmetry in how gains and losses are processed.

**The isolation effect**: People simplify by discarding components shared across options, then evaluate the remainder. Because the same prospect pair can be decomposed differently, this produces inconsistent choices across formally equivalent framings. Problems 10–12 in Kahneman and Tversky (1979) demonstrate this: subjects ignored a common bonus or a common first-stage gamble, treating identical final-state prospects differently depending on presentation.

**Preference reversals**: Lichtenstein and Slovic (1971) showed that people can prefer gamble A over gamble B in direct choice but assign a higher monetary value to B than to A in pricing tasks. This violates the assumption that a single preference ordering underlies all choice-relevant behavior — different response modes (choosing vs. pricing) elicit different "preferences."

**Framing effects**: Tversky and Kahneman (1981) demonstrated that describing the same medical outcome as "200 out of 600 people saved" versus "400 out of 600 people die" reverses the majority preference between a sure option and a risky one. The information content is identical; the reference point (saving lives vs. losing lives) changes.

### Prospect Theory: The Descriptive Alternative

Prospect theory (Kahneman & Tversky, 1979; extended as cumulative prospect theory in Tversky & Kahneman, 1992) is the dominant descriptive model of choice under risk. It departs from EUT in four ways:

**Reference dependence**: Outcomes are evaluated as gains and losses relative to a reference point, not as final wealth states. The reference point is typically the status quo but can be shifted by expectations, aspirations, or framing.

**The value function**: Defined on gains and losses, it is concave for gains (diminishing sensitivity), convex for losses (diminishing sensitivity), and steeper for losses than for gains (loss aversion). The ratio of loss to gain sensitivity is typically estimated around 2:1 — losing $100 feels about twice as bad as gaining $100 feels good.

**The probability weighting function**: Stated probabilities are transformed by a function π(p) that overweights small probabilities and underweights moderate-to-high ones. The function is concave near zero and convex near one, with sharp transitions at the endpoints (certainty/impossibility). This explains simultaneously why people buy lottery tickets (overweighting the small chance of a large gain) and insurance (overweighting the small chance of a large loss).

**Two-phase processing**: Prospects are first *edited* (coded, combined, segregated, simplified) and then *evaluated*. The editing phase introduces framing dependence — different problem descriptions trigger different edits, producing different evaluated prospects from identical objective situations.

**Cumulative prospect theory** (Tversky & Kahneman, 1992) addressed a limitation of the original: it applies to prospects with any number of outcomes, uses rank-dependent probability weighting (avoiding violations of stochastic dominance that the original permitted), and provided parametric forms for the value function (v(x) = xᵅ for gains, −λ(−x)ᵝ for losses, with α ≈ β ≈ 0.88 and λ ≈ 2.25) and weighting function that enable quantitative fitting.

### Competing and Complementary Models

Prospect theory is dominant but not alone:

**Regret theory** (Bell, 1982; Loomes & Sugden, 1982): People anticipate the regret they would feel if their choice turns out worse than an alternative they could have chosen. This explains some violations of independence without requiring reference-dependent value functions.

**Salience theory** (Bordalo, Gennaioli & Shleifer, 2012): Attention is drawn to outcome states where the options differ most, and salient payoffs are overweighted. This provides an attention-based explanation for many prospect-theory phenomena (certainty effect, Allais paradox) without nonlinear probability weighting. Salience theory connects this stream directly to Stream 4 ([Attention & Salience](../attention-memory-salience)).

**Rank-dependent utility** (Quiggin, 1982): Probability weighting is applied to cumulative probabilities rather than individual outcome probabilities, preserving stochastic dominance. Cumulative prospect theory adopted this idea.

**Disappointment aversion** (Gul, 1991): Outcomes below the certainty equivalent of a gamble generate additional disutility (disappointment), while outcomes above generate additional utility (elation). This captures some reference-dependent behavior within a more parsimonious framework.

The empirical evidence does not cleanly favor one model over all others across all domains. Prospect theory fits individual choice data best in most laboratory settings; salience theory provides better predictions in some market and pricing contexts; regret theory matters when outcomes of foregone alternatives are observed.

### Utility Elicitation: Measuring Preferences

To use any normative or descriptive model prescriptively, you need to know the person's preferences — their utility or value function parameters. This creates a measurement problem that inherits all the difficulties from Stream 1 ([Belief Elicitation](../belief-elicitation)) plus additional ones:

**Certainty equivalents**: Ask the person: "What sure amount is equivalent to a 50-50 gamble between $0 and $100?" If they say $40, you learn one point on their utility function. Repeating with different gambles traces the function. Problem: responses are sensitive to the gamble's probabilities (which interact with probability weighting) and to the anchoring effect of the gamble amounts.

**Probability equivalents**: Ask: "At what probability p would you be indifferent between (p chance of $100) and ($40 for sure)?" This identifies the probability weight associated with u($40)/u($100) but confounds the value function with the weighting function.

**Trade-off method** (Wakker & Deneffe, 1996): Constructs a sequence of indifferences that cancel out the probability weighting function, isolating the value function. Theoretically superior but cognitively demanding — requires multiple consistent indifference judgments.

The fundamental challenge is that **all elicitation methods produce theory-laden measurements**. A certainty equivalent interpreted through EUT yields a different utility function than the same certainty equivalent interpreted through prospect theory, because the latter separates value function curvature from probability weighting. You cannot measure preferences without assuming a model, and different models yield different "preferences" from the same data.

### Decision Quality: When Is a Decision Good?

Decision quality is distinct from decision outcomes. A good decision can lead to a bad outcome (you made the right bet and lost) and a bad decision can lead to a good outcome (you made a terrible bet and got lucky). Assessing decision quality requires evaluating the *process*, not the result.

Howard (1988) proposed six requirements for decision quality: an appropriate frame, creative alternatives, meaningful and reliable information, clear values, correct reasoning, and commitment to action. This is fundamentally a prescriptive framework — it evaluates whether the decision-maker's process would lead to choices consistent with their values given correct information.

The modern challenge is applying decision quality to human-AI teams. When an AI advisor recommends option A and the person chooses B:

- If B violates the person's own stated values (elicited separately), the AI has identified a genuine processing error worth correcting.
- If B reflects values the person holds but that the AI's model doesn't capture (e.g., a preference for controllability, social considerations, identity-related concerns), overriding B would be paternalistic.
- If the "values" were themselves elicited through a biased method (framing-dependent, format-sensitive), neither A nor B has a clear claim to being "what the person really wants."

This trilemma has no clean resolution. It is the central design challenge for AI-assisted decision support: the system needs a normative benchmark to improve on the status quo, but every candidate benchmark embeds assumptions about what the person should value.

## Evolution Timeline

**Foundations (1944–1979):** Von Neumann and Morgenstern (1944) axiomatized expected utility, providing the normative benchmark that the entire field reacts to. Savage (1954) extended it to subjective probability, unifying beliefs and preferences. Allais (1953) immediately demonstrated that real preferences violate the independence axiom, launching the "anomalies" research program. Markowitz (1952) proposed that utility is defined on changes from a reference point rather than final wealth — a key precursor to prospect theory that also noted risk-seeking behavior for both gains and losses. Pratt (1964) and Arrow (1965) formalized risk aversion measures. Raiffa (1968) developed decision analysis as a prescriptive practice, establishing that the gap between descriptive and normative could be productively bridged through structured methods.

**The behavioral revolution (1979–1992):** Kahneman and Tversky (1979) proposed prospect theory, synthesizing the Allais-type violations into a coherent descriptive model with reference dependence, an S-shaped value function, nonlinear probability weighting, and a two-phase editing-evaluation structure. Simultaneously, Lichtenstein and Slovic (1971) and Grether and Plott (1979) documented preference reversals, showing that the very *existence* of a stable preference ordering is questionable. Bell (1982) and Loomes and Sugden (1982) proposed regret theory. Quiggin (1982) developed rank-dependent utility. Tversky and Kahneman (1981) demonstrated framing effects with the Asian disease problem. By the end of this era, the descriptive inadequacy of EUT was established beyond dispute, and multiple alternative models competed for the descriptive crown.

**Refinement and measurement (1992–2012):** Tversky and Kahneman (1992) published cumulative prospect theory, resolving the original theory's problems with stochastic dominance and multi-outcome prospects, and providing parametric forms suitable for quantitative estimation. Wakker and Deneffe (1996) developed the trade-off method for eliciting utility under non-expected-utility models. Kőszegi and Rabin (2006, 2007) endogenized the reference point using rational expectations — a major theoretical advance that connected prospect theory to equilibrium economics. Bleichrodt and Pinto (2000) and Abdellaoui (2000) conducted careful parametric estimations of prospect theory's value and weighting functions. The decision quality movement (Howard, 1988; Matheson & Matheson, 1998) developed practical frameworks for evaluating decision processes in organizations.

**The attention turn and AI era (2012–present):** Bordalo, Gennaioli, and Shleifer (2012) proposed salience theory, offering an attention-based mechanism for choice anomalies that competes with probability weighting as an explanation. Enke and Graeber (2023) introduced "cognitive uncertainty" — the idea that people are uncertain about their own valuations — as a unified account of many behavioral patterns. On the applied side, the rise of AI decision support created urgent versions of old questions: how should an AI advisor define "better" decisions? If the benchmark is EUT, the system imposes a model the user may not endorse. If the benchmark is prospect theory, the system might preserve loss-aversion patterns the user would want corrected on reflection. Automated preference learning from observed choices (revealed preference under behavioral models) is an active area, but it inherits all the instability and framing-dependence of the preferences it learns from.

## Key Distinctions

**Normative vs. descriptive vs. prescriptive**: What should be (EUT axioms) vs. what is (systematic violations) vs. what helps (decision analysis, AI-assisted choice). Confusing these leads to either dismissing real behavior as "irrational" or abandoning the idea that decisions can be improved.

**Risk aversion vs. loss aversion**: Risk aversion (preferring a sure thing over a gamble with the same expected value) and loss aversion (losses loom larger than gains) are different phenomena. EUT explains risk aversion through utility function concavity. Prospect theory explains much of what looks like risk aversion as actually loss aversion interacting with reference-dependent evaluation. The distinction matters for intervention design: reducing risk aversion might require changing the utility function, while reducing loss aversion might require shifting the reference point.

**Outcome quality vs. process quality**: A good decision can have a bad outcome. Evaluating decisions by outcomes (did the patient survive?) conflates skill with luck. Evaluating by process (was the information gathered, were alternatives considered, were values articulated?) separates the controllable from the uncontrollable.

**Utility of outcomes vs. utility of the decision process**: People derive utility not only from outcomes but from the act of choosing itself — autonomy, engagement, responsibility. An AI that makes optimal choices on the user's behalf may reduce outcome variance but also reduce the user's experienced utility from the process of deciding. This is understudied but practically important.

**Stable preferences vs. constructed preferences**: EUT assumes preferences are stable and discovered through elicitation. Prospect theory and its descendants suggest preferences are constructed in the moment, sensitive to framing, context, and the elicitation instrument. If preferences are constructed, "what the person really wants" may not have a determinate answer, and "respecting preferences" becomes conceptually murky.

## Cross-References

- **[Belief Elicitation](../belief-elicitation)**: Utility elicitation inherits all the problems of belief elicitation (format sensitivity, incentive compatibility under non-EU models) plus additional ones: utility responses confound the value function with the probability weighting function, making theory-free measurement impossible.
- **[Uncertainty Communication](../uncertainty-communication)**: How uncertainty is communicated determines which prospect-theoretic effects are activated. A display that highlights the risk of loss triggers loss aversion; one that highlights the possibility of gain triggers overweighting of small probabilities. Communication format is an underappreciated moderator of revealed preferences.
- **[Attention & Salience](../attention-memory-salience)**: Salience theory (Bordalo et al., 2012) is a direct competitor/complement to prospect theory. Whether choice anomalies arise from distorted probability weighting or from distorted attention allocation is one of the central theoretical debates in this stream.
- **[Risk & Ambiguity](../risk-ambiguity)**: EUT and prospect theory both assume known probabilities. When probabilities are ambiguous (unknown), additional phenomena emerge (Ellsberg paradox) that require extensions: prospect theory under ambiguity, smooth ambiguity models, or maxmin expected utility.
- **[Temporal Dynamics](../temporal-dynamics)**: Myopic loss aversion (Benartzi & Thaler, 1995) is the interaction of prospect theory's loss aversion with the temporal structure of evaluation — how often you look at your portfolio determines how much loss aversion distorts your risk-taking.
- **[Agents as Advisors](../agents-as-advisors)**: The normative benchmark problem is most acute here. Every AI advisor implicitly adopts a model of what "better" decisions look like. Making that model explicit, and letting the user endorse or modify it, is a design challenge that requires engaging with the normative-descriptive-prescriptive trichotomy directly.

## Open Questions

1. **Can AI systems learn a person's utility function from observed choices, given that observed choices are framing-dependent and model-laden?** Revealed preference approaches assume the choices reveal stable preferences. If choices are constructed (prospect theory, salience theory), what exactly is being "revealed," and how should the AI handle inconsistencies across elicitation contexts?

2. **What should the normative benchmark be for AI-assisted decisions?** EUT is too rigid (people don't endorse its implications on reflection). Prospect theory is too permissive (it predicts framing effects that people want corrected). Is there a "reflective equilibrium" model — the preferences the person would hold if they were fully informed, cognitively unconstrained, and free from framing effects — and can it be operationalized?

3. **How should salience theory and prospect theory be empirically distinguished in applied settings?** Both predict Allais-type violations, but through different mechanisms (attention vs. probability weighting). In AI interface design, the distinction matters: if the mechanism is attentional, fixing the display fixes the bias. If it's probability weighting, the bias persists regardless of display.

4. **Is loss aversion a bias to be corrected or a preference to be respected?** Some loss aversion may reflect genuine asymmetry in the experience of gains and losses. Some may reflect a processing error (people would prefer symmetric treatment on reflection). AI advisors need a way to distinguish these cases — or at least to make the distinction transparent to the user.

5. **How does second-order uncertainty about one's own preferences affect decision quality?** Enke and Graeber's (2023) "cognitive uncertainty" suggests people are uncertain about their own valuations. If so, an AI advisor that helps resolve this uncertainty (through structured elicitation, Socratic dialogue, or presenting trade-offs clearly) may improve decisions not by correcting biases but by reducing preference noise.

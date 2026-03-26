---
id: attention-memory-salience
name: "Attention, Memory, Salience & Cognitive Load"
icon: "🧠"
color: "#50C878"
---

# Attention, Memory, Salience & Cognitive Load

> How do interfaces shape what people notice, remember, and weigh in their decisions?

## Concept Overview

Streams 1–3 address what people believe, how uncertainty is communicated, and what people value. This stream addresses the bottleneck between information and choice: the cognitive machinery that determines what gets processed and how.

The core insight is that attention is scarce, selective, and consequential. People do not evaluate all available information equally — they allocate limited cognitive resources to a subset of features, outcomes, or options, and this allocation shapes their decisions in ways that standard models (which assume full information processing) cannot predict. A decision interface that provides all the right information but directs attention to the wrong features will produce worse decisions than an interface that provides less information but directs attention well.

Three research traditions converge here:

**Bounded rationality** (Simon, 1955) established that cognitive limitations are not noise to be averaged away but structural constraints that shape the form of decision-making itself. Rational agents *satisfice* rather than optimize because exhaustive search is computationally infeasible. This framing rejects the idea that biases are "errors" relative to a normative ideal — they are consequences of operating under real constraints.

**Salience theory** (Bordalo, Gennaioli & Shleifer, 2012, 2013) formalized how context-dependent attention distorts choice. The key mechanism: when comparing options, attention is drawn to outcome states where the options differ most in relative terms. Salient payoffs are overweighted. This produces many of the same choice patterns as prospect theory (certainty effect, Allais violations, preference reversals) but through an attentional mechanism rather than probability weighting — a distinction with direct implications for interface design (see: [Utility & Decision Quality](../utility-decision-quality)).

**Rational inattention** (Sims, 2003; Matějka & McKay, 2015) models attention allocation as an optimization problem: the decision-maker chooses how much information to acquire subject to an information-processing cost (measured in entropy reduction). This generates endogenous "errors" that look like biases but are optimal given costs. Matějka and McKay showed that rational inattention implies choice probabilities follow a logit form, connecting the attention literature to the discrete choice literature.

### Salience Theory in Detail

Salience theory deserves extended treatment because it competes directly with prospect theory as an explanation for choice anomalies and because its implications for interface design differ sharply.

In the standard Bordalo, Gennaioli, and Shleifer (2012) model, a decision-maker compares two lotteries across states of the world. In each state, one lottery pays more than the other. The *salience* of a state depends on how much the payoffs differ relative to their average — specifically, the salience function σ(xₛ, yₛ) is increasing in |xₛ − yₛ| and decreasing in |xₛ + yₛ|, where xₛ and yₛ are the payoffs of the two lotteries in state s. The decision-maker overweights salient states and underweights non-salient ones.

This produces the Allais common consequence effect without probability weighting: when a sure option is compared to a risky one, the state in which the sure option pays and the risky one pays zero is highly salient (large relative difference), drawing attention and inflating the subjective attractiveness of certainty. When both options are risky, no state has the same salience advantage, and the preference reverses. The mechanism is pure attention — the probabilities are not distorted, the value function is not S-shaped. What changes is which outcomes the decision-maker *focuses on*.

Bordalo, Gennaioli, and Shleifer (2013) extended the model to consumer choice, showing that salient attributes (e.g., price for a cheap good, quality for a luxury good) are context-dependent — the same product attribute can be salient or non-salient depending on what it's being compared to. This explains decoy effects, compromise effects, and asymmetric dominance without invoking reference-dependent preferences.

**Why this matters for human-agent decision making:** If choice anomalies are attentional rather than preferential, then they can be corrected by *changing the display* rather than by changing the person's processing. An interface that de-emphasizes salient-but-irrelevant features, or that recontextualizes options to shift salience toward decision-relevant attributes, could eliminate biases that prospect theory would predict are hardwired. Conversely, a poorly designed AI interface could *create* biases by making irrelevant features salient.

### Cognitive Load and Decision Degradation

Cognitive load theory (Sweller, 1988) distinguishes three types of load:

- **Intrinsic load**: inherent to the complexity of the decision task itself (number of options, number of attributes, uncertainty structure).
- **Extraneous load**: imposed by the interface or presentation format (poor layout, confusing labels, unnecessary information).
- **Germane load**: the mental effort directed toward building useful schemas and understanding (the "good" kind of cognitive effort).

Good interface design minimizes extraneous load while preserving germane load. In the context of AI-assisted decisions, this means AI explanations (feature importance, confidence scores, counterfactuals) add value only if they increase germane load (helping the user build a useful mental model of the task) without adding proportionally more extraneous load (confusing details, unfamiliar notation, information that doesn't map to the user's decision frame).

The empirical evidence is clear that high cognitive load degrades decision quality. Shiv and Fedorikhin (1999) showed that people under high load make more affect-driven choices (choosing cake over fruit). Deck and Jahedi (2015) found that cognitive load increases risk aversion for gains and risk-seeking for losses — amplifying prospect-theoretic patterns. This suggests that cognitive load doesn't just add noise; it shifts the decision toward heuristic, System-1 processing that is more susceptible to framing effects and salience distortions.

### Cognitive Uncertainty

Enke and Graeber (2023) introduced a construct that bridges attention and preference: **cognitive uncertainty** — the subjective uncertainty a person feels about their own valuations. When facing a complex choice, people don't just face uncertainty about the world (will it rain?); they face uncertainty about their own preferences (how much do I value this option?). Enke and Graeber show that cognitive uncertainty produces a specific pattern: reported valuations are compressed toward a default or prior (typically the center of the scale or the expected value), generating apparent risk aversion, ambiguity aversion, and insensitivity to probability — not because preferences are distorted but because the person is averaging between their (uncertain) best guess and a default.

This reframes several phenomena from Streams 3 and 5 as consequences of *not knowing what you want* rather than *wanting something irrational*. It also suggests a specific role for AI advisors: helping users resolve their cognitive uncertainty by clarifying trade-offs, structuring the decision, and reducing the complexity that generates the uncertainty in the first place (see: [Agents as Advisors](../agents-as-advisors)).

### Choice Architecture and Defaults

Thaler and Sunstein (2008) synthesized decades of behavioral research into the **nudge** framework: since the way options are presented inevitably affects choices (there is no "neutral" architecture), the designer should arrange the choice environment to help people make decisions aligned with their own interests. Key tools:

- **Defaults**: The pre-selected option if the person takes no action. Defaults are powerful because of status quo bias, loss aversion (switching away from the default feels like a loss), and because defaults signal a recommendation. Johnson and Goldstein (2003) showed that organ donation rates vary from ~15% to ~99% across European countries, with almost all the variance explained by whether the default is opt-in or opt-out.
- **Option ordering and framing**: Which option is listed first, how options are described, and which attributes are highlighted all affect choice — consistent with salience theory predictions.
- **Simplification**: Reducing the number of options or attributes improves decision quality when the full set exceeds the person's processing capacity. Iyengar and Lepper (2000) found that presenting 24 jam options reduced purchase rates compared to 6 options (the "choice overload" effect, though its replicability is debated — Scheibehenne, Greifeneder & Todd, 2010).

The nudge framework is directly relevant to AI-assisted decision design. Every AI recommendation interface makes architectural choices: the default option, the number of alternatives presented, the attributes highlighted, the ordering. These choices are not value-neutral — they predictably shift behavior. A responsible AI advisor design must be intentional about its choice architecture.

### Memory, Recency, and Sequential Decision-Making

Attention governs what enters processing; memory governs what persists. In sequential decision settings — where a person makes a series of choices informed by AI advice — memory effects shape how prior outcomes influence current decisions.

**Recency**: People overweight recent observations relative to earlier ones when forming beliefs and preferences. In human-AI interaction, a recent AI error may dominate the person's trust assessment even if the AI's overall track record is strong (see: [Temporal Dynamics](../temporal-dynamics)).

**Peak-end rule** (Kahneman, Fredrickson, Schreiber & Redelmeier, 1993): People evaluate sequences primarily by their peak intensity and their end state, not by duration or cumulative total. This has implications for how AI advisory sequences are experienced and remembered.

**Serial position effects**: In lists of options, items presented first (primacy) and last (recency) receive disproportionate attention. AI systems that present recommendation lists must account for position bias.

## Evolution Timeline

**Foundations (1955–1988):** Simon (1955) introduced bounded rationality, redefining the decision-maker from an omniscient optimizer to a resource-constrained satisficer. Tversky (1972) proposed elimination by aspects — a sequential, attribute-based choice process that reduces cognitive load by eliminating options one feature at a time. Sweller (1988) formalized cognitive load theory in educational psychology, providing the intrinsic/extraneous/germane framework. Kahneman and Tversky's work on heuristics and biases (1974) documented systematic shortcuts (availability, representativeness, anchoring) that arise from cognitive constraints — though the heuristics-and-biases program and the bounded-rationality program offered different interpretations of whether these shortcuts are errors or adaptations.

**Formalization (2003–2012):** Sims (2003) introduced rational inattention, modeling attention allocation as entropy-constrained optimization and connecting cognitive constraints to information theory. Gabaix and Laibson (2006) and Gabaix (2014) developed sparse models of bounded rationality where agents optimally choose which variables to attend to and which to set to default values. Matějka and McKay (2015) showed that rational inattention implies logit choice probabilities, providing a micro-foundation for the most widely used discrete choice model. Bordalo, Gennaioli, and Shleifer (2012, 2013) proposed salience theory, providing a formal, testable model of context-dependent attention in risky and riskless choice that generates predictions distinct from prospect theory.

**Integration with behavioral models (2015–present):** Enke and Graeber (2023) introduced cognitive uncertainty, showing that many "biases" (risk aversion, probability insensitivity, ambiguity aversion) can be reinterpreted as consequences of noisy introspection rather than distorted preferences. Kőszegi and Szeidl (2013) proposed focusing theory, where attributes with larger ranges attract more attention — conceptually similar to salience theory but applied to multi-attribute (riskless) choice. On the applied side, the rise of AI decision support created urgent questions about information overload: AI explanations (feature attributions, uncertainty estimates, counterfactuals) increase the information load on the decision-maker, and the evidence on whether "more explanation" actually improves decisions is mixed (Poursabzi-Sangdeh, Goldstein, Hofman, Vaughan & Wallach, 2021; Bansal, Wu, Zhou, Fok, Nushi, Kamar, Ribeiro & Weld, 2021). The key finding emerging from this literature is that *selective* explanation — highlighting only the information most relevant to the current decision — outperforms *comprehensive* explanation.

## Key Distinctions

**Attentional bias vs. preferential bias**: Salience theory says people attend to the wrong features; prospect theory says people *value* outcomes nonlinearly. The distinction matters for intervention: attentional biases can be fixed by redesigning the display; preferential biases persist regardless of display.

**Extraneous vs. germane cognitive load**: More information is not always better. AI explanations add value only if they help the user build a decision-relevant mental model (germane) rather than just adding complexity (extraneous). The distinction is task-dependent — the same information is germane in one context and extraneous in another.

**Rational inattention vs. bounded rationality**: Rational inattention models attention limits as an optimization (the agent chooses the best allocation given costs). Bounded rationality models them as hard constraints (the agent satisfices because optimization is infeasible). The practical difference: rational inattention predicts that attention allocation responds to incentives (higher stakes → more attention → fewer "errors"); bounded rationality predicts that some constraints bind regardless of stakes.

**Bottom-up vs. top-down attention**: Salience is partly bottom-up (stimulus-driven — large differences "pop") and partly top-down (goal-driven — you attend to what you're looking for). AI interfaces can leverage both: making decision-relevant information perceptually salient (bottom-up) and cueing the user's goals (top-down).

**Cognitive uncertainty vs. value uncertainty vs. preference noise**: Enke and Graeber's cognitive uncertainty is uncertainty about one's own valuation due to complexity. Value uncertainty (Butler & Loomes, 2007) is uncertainty about how much utility an outcome will provide. Preference noise is random variation in revealed preferences. These have overlapping empirical signatures but different theoretical implications and different prescriptions for AI-assisted decision support.

## Cross-References

- **[Utility & Decision Quality](../utility-decision-quality)**: Salience theory competes with prospect theory as an explanation for choice anomalies. Cognitive uncertainty (Enke & Graeber) reinterprets apparent preference distortions as consequences of noisy introspection. Both suggest that the normative-descriptive gap may be partly attentional, not preferential.
- **[Uncertainty Communication](../uncertainty-communication)**: Every uncertainty display competes for limited attention. Whether a user processes an AI-provided confidence interval depends on its perceptual salience relative to other interface elements, not just its informational content.
- **[Belief Elicitation](../belief-elicitation)**: Elicitation under high cognitive load produces noisier, more heuristic-driven responses. The complexity of the elicitation instrument determines whether the person can devote germane effort to accessing their beliefs or is overwhelmed by extraneous processing demands.
- **[Temporal Dynamics](../temporal-dynamics)**: Memory effects (recency, peak-end rule) determine how prior experiences with an AI advisor shape current trust and reliance. Sequential attention allocation over a session follows different dynamics than single-shot attention allocation.
- **[Agents as Advisors](../agents-as-advisors)**: The practical takeaway: AI explanations must be selective, not comprehensive. The system should model what the user is attending to and intervene only where attention is misdirected or insufficient — functioning as an attention guide, not an information firehose.

## Open Questions

1. **Is the mechanism behind Allais-type violations attentional (salience theory) or preferential (prospect theory)?** The answer determines whether better interfaces can eliminate the violations or whether they are deep features of valuation. Existing lab data are consistent with both accounts; distinguishing them requires process-level evidence (eye-tracking, response times, neural data) in applied decision settings.

2. **What is the optimal amount of AI explanation?** More explanation increases germane load (better mental model) but also extraneous load (more to process). Where is the sweet spot, and does it vary by user expertise, task complexity, and time pressure? The emerging answer is that *selective* explanation dominates *comprehensive* explanation, but how to select — which features, which level of detail — is not yet principled.

3. **Can AI systems model the user's attention in real time?** If the system could track what the user is looking at (eye tracking), how long they spend on each element (dwell time), and where they are in their decision process, it could adaptively highlight neglected but important information. The technology exists; the design principles for attention-adaptive interfaces do not.

4. **Does cognitive uncertainty (Enke & Graeber) change the prescription for AI advisors?** If much of apparent bias is really "not knowing what I want" due to decision complexity, then the advisor's job is not to correct preferences but to help clarify them — through structured decomposition, trade-off presentation, and Socratic questioning. This is a fundamentally different design philosophy than "debiasing."

5. **How do defaults interact with AI recommendations?** When an AI system presents a recommendation as the default, it inherits all the power (and manipulation potential) of defaults documented in the nudge literature. Should AI recommendations be presented as defaults, as one option among equals, or as input to the user's deliberation? The answer depends on the domain, the stakes, and the quality of the AI's judgment relative to the user's.

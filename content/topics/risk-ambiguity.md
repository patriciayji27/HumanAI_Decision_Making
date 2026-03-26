---
id: risk-ambiguity
name: "Risk, Ambiguity & Controllability"
icon: "🎲"
color: "#DC4C64"
---

# Risk, Ambiguity & Controllability

> How do people process different types and sources of uncertainty, and how does perceived control modulate behavior?

## Concept Overview

Stream 3 ([Utility & Decision Quality](../utility-decision-quality)) covers how people choose under risk — situations with known probabilities. This stream covers what happens when the probabilities themselves are unknown, when the source of uncertainty matters, and when perceived control enters the picture.

The foundational distinction is between **risk** (known probability distribution) and **ambiguity** (unknown or imprecise probability distribution), sometimes called Knightian uncertainty after Frank Knight (1921). This is not a theoretical curiosity. Most real-world uncertainty is ambiguous: a physician estimating a rare disease probability, a voter assessing a candidate's likelihood of fulfilling promises, a user judging whether an AI model will be reliable in a novel situation. In all these cases, the person cannot access a well-defined probability distribution. How they respond to this — and how it differs from their response to equivalent "known" risks — is the subject of this stream.

The key empirical finding is **ambiguity aversion**: people prefer known risks to unknown ones, even when the known risk is objectively no better. But this is not the full picture. Ambiguity attitudes are heterogeneous, domain-dependent, probability-level-dependent, and source-dependent. Understanding the structure of these attitudes is essential for designing AI systems that communicate and manage uncertainty, because AI predictions carry both risk (irreducible noise in the predicted variable) and ambiguity (uncertainty about the model's reliability, especially in novel contexts).

## The Ellsberg Paradox and Its Extensions

Ellsberg (1961) demonstrated ambiguity aversion with a thought experiment that remains the field's anchor. An urn contains 90 balls: 30 are red; the remaining 60 are some unknown mix of black and yellow. You choose a color and draw a ball; if it matches, you win $100.

- **Bet on red vs. bet on black**: Most people prefer red (known 1/3 probability) over black (unknown probability between 0 and 2/3).
- **Bet on red-or-yellow vs. bet on black-or-yellow**: Most people prefer black-or-yellow (known 2/3) over red-or-yellow (unknown, between 1/3 and 1).

The pair of preferences is jointly inconsistent with any probability assignment to the unknown urn composition — no single prior over the black/yellow mix rationalizes both choices. The preferences reveal that people are not simply estimating probabilities and then maximizing expected utility; they are responding to the *imprecision* of the probability itself.

Ellsberg's paradox has been replicated extensively and extended in several directions:

**Natural sources of ambiguity**: Laboratory urns are artificial. Ambiguity aversion also appears with natural uncertain events — unfamiliar domains, events where the person lacks expertise, and situations where the "data-generating process" is opaque. The magnitude of ambiguity aversion varies substantially across domains: it is stronger for unfamiliar events and weaker (sometimes reversing to ambiguity-seeking) for events in the person's domain of expertise (Heath & Tversky, 1991).

**Probability-level dependence**: Ambiguity aversion is not uniform across the probability scale. People tend to be ambiguity-averse for moderate-to-high probability gains and ambiguity-seeking for low-probability gains — a pattern that mirrors the fourfold pattern of risk attitudes in prospect theory. Trautmann and van de Kuilen (2015) documented this in a comprehensive survey, showing that the interaction between ambiguity and probability level is robust across studies and populations.

**Gains vs. losses**: Ambiguity aversion is typically stronger in the gain domain than in the loss domain, where ambiguity-seeking is sometimes observed. This parallels the reflection effect in prospect theory.

## Source Preference

Fox and Tversky (1995) introduced a concept that deepens the Ellsberg finding: ambiguity aversion depends not just on how much is unknown, but on the **source** of the uncertainty. People evaluate uncertainty relative to what they feel they know — their *competence* with the source.

In their key experiment, participants who rated themselves knowledgeable about football but not finance preferred to bet on football events (where they felt competent) over equivalent finance events — and vice versa for finance experts. The probabilities were matched; what varied was the person's perceived expertise with the domain. Heath and Tversky (1991) had documented a related finding: people sometimes prefer ambiguous bets in their area of expertise over known-probability lotteries — the opposite of Ellsberg-type ambiguity aversion — because felt competence makes the ambiguity less aversive.

**Source preference** has direct implications for human-AI interaction. When a user evaluates an AI prediction, the "source" is the AI model. If the user feels competent to evaluate the AI's domain (e.g., a radiologist evaluating an AI's chest X-ray interpretation), source preference predicts less aversion to the AI's uncertainty. If the user feels incompetent (e.g., a patient evaluating the same AI), source preference predicts more aversion — the uncertainty feels more "ambiguous" even if the objective uncertainty is identical. This is a distinct mechanism from algorithm aversion (Stream 8) and may interact with it.

## Two-Dimensional Uncertainty

Ülkümen, Fox, and Malle (2016) proposed that people naturally distinguish two types of uncertainty, and that this distinction is linguistically marked and psychologically real:

**Epistemic uncertainty** is uncertainty due to ignorance — it is reducible with more information. "I don't know what the GDP of Indonesia is, but I could look it up." Epistemic uncertainty is associated with causal/diagnostic reasoning and with feelings of missing information.

**Aleatory uncertainty** is uncertainty due to inherent randomness — it is irreducible even with complete information. "I don't know what the next coin flip will be, and neither does anyone else." Aleatory uncertainty is associated with propensity/frequency reasoning and with acceptance of stochastic variability.

People use different language for the two types ("I believe/think" for epistemic; "there's a chance/likelihood" for aleatory), form different confidence judgments, and update differently when given new information. Epistemic uncertainty triggers information-seeking behavior; aleatory uncertainty does not.

This distinction maps directly onto AI uncertainty. A model's prediction uncertainty has both components: **model uncertainty** (epistemic — the model could be better with more training data or a different architecture) and **data noise** (aleatory — the outcome is inherently stochastic even with a perfect model). How users respond to each type — and whether they can distinguish them in an AI's output — has implications for trust, reliance, and information-seeking behavior. An AI system that says "I'm uncertain because I haven't seen cases like this before" (epistemic) should trigger different user behavior than one that says "this outcome is inherently unpredictable" (aleatory). Whether current AI interfaces make this distinction is another matter.

## Formal Models of Ambiguity

The theoretical literature has produced several models that accommodate ambiguity aversion within a decision-theoretic framework:

**Maxmin expected utility** (Gilboa & Schmeidler, 1989): The decision-maker considers a set of possible probability distributions (the *prior set*) and evaluates each option by its minimum expected utility across this set. This captures extreme ambiguity aversion — the agent acts as if nature will choose the worst distribution. It explains the Ellsberg paradox directly: the agent pessimistically evaluates the ambiguous urn.

**Smooth ambiguity** (Klibanoff, Marinacci & Mukerji, 2005): The decision-maker has a second-order probability distribution over possible first-order distributions, and evaluates options by a φ-weighted expectation over these. When φ is concave, the model generates ambiguity aversion without the all-or-nothing pessimism of maxmin. This allows for intermediate ambiguity attitudes and provides a more nuanced fit to the data.

**Choquet expected utility** (Schmeidler, 1989): Probabilities are replaced by non-additive capacities, and integration uses the Choquet integral. This is mathematically connected to rank-dependent models and to the weighting function in cumulative prospect theory. It accommodates both ambiguity aversion and ambiguity-seeking depending on the capacity structure.

**Source-dependent models** (Chew & Sagi, 2008; Abdellaoui, Baillon, Placido & Wakker, 2011): These allow the probability weighting function to vary across sources of uncertainty — a natural formalization of Fox and Tversky's source preference. The person may weight probabilities differently for familiar vs. unfamiliar sources, or for events they feel competent vs. incompetent to judge.

For applied purposes, the choice between models matters less than the shared insight: people's uncertainty processing is sensitive to the *type and source* of uncertainty, not just its magnitude. Any AI system that communicates a single "confidence score" without distinguishing the nature of the underlying uncertainty is throwing away information that users implicitly process.

## Controllability and Illusion of Control

Perceived control modulates risk-taking even when actual control is absent. Langer (1975) documented the **illusion of control**: people behave as if they can influence random outcomes when given cues of personal involvement (choosing lottery numbers, throwing dice themselves, competing against an apparently unskilled opponent). The effect is robust and extends to financial decision-making, gambling behavior, and health decisions.

In human-AI decision-making, controllability takes several forms:

**Interactivity as perceived control**: When users can adjust parameters, ask follow-up questions, or override AI recommendations, they may feel more "in control" — and this perceived control may increase their risk tolerance independently of whether the interaction actually improves the decision. This echoes Langer's finding that irrelevant control cues affect behavior.

**Delegation as loss of control**: Delegating a decision to an AI may be aversive not because the AI is expected to perform worse, but because delegation eliminates the person's control. Bobadilla-Suarez, Sunstein, and Sharot (2017) found that people prefer to retain decision authority even when doing so leads to worse expected outcomes, consistent with an intrinsic value of control separate from outcome utility.

**Controllability and ambiguity interaction**: Ambiguity is more aversive when the person feels they *should* be able to reduce it (epistemic) than when it is clearly uncontrollable (aleatory). This connects back to the two-dimensional uncertainty framework: controllable uncertainty triggers information-seeking and discomfort; uncontrollable uncertainty triggers acceptance (or avoidance).

## Evolution Timeline

**Foundations (1921–1961):** Knight (1921) drew the conceptual distinction between risk and uncertainty. Savage (1954) provided the subjective expected utility framework that, in principle, eliminates the distinction — all uncertainty is quantifiable as subjective probability. Ellsberg (1961) showed empirically that Savage's framework fails: people's choices reveal sensitivity to whether probabilities are known or unknown, violating the sure-thing principle. The Ellsberg paradox established ambiguity aversion as a distinct behavioral phenomenon irreducible to risk attitudes.

**Source dependence and heterogeneity (1989–2005):** Gilboa and Schmeidler (1989) provided the first axiomatic model accommodating ambiguity aversion (maxmin EU). Heath and Tversky (1991) showed that competence reverses ambiguity aversion — people sometimes prefer ambiguous bets in domains where they feel expert. Fox and Tversky (1995) formalized this as source preference, showing that ambiguity attitudes are relative to the decision-maker's felt knowledge of the uncertainty source, not absolute properties of the probability information. Klibanoff, Marinacci, and Mukerji (2005) developed smooth ambiguity, allowing continuous ambiguity attitudes.

**Measurement and typology (2005–2018):** Trautmann and van de Kuilen (2015) provided a comprehensive survey of ambiguity attitudes, documenting the probability-level dependence, gain-loss asymmetry, and cross-cultural variation in ambiguity aversion. Ülkümen, Fox, and Malle (2016) introduced the epistemic-aleatory distinction as a psychologically real, linguistically marked dimension of uncertainty processing. Abdellaoui, Baillon, Placido, and Wakker (2011) developed source-dependent elicitation methods, showing that the probability weighting function differs systematically across uncertainty sources within the same individual. This era established that "ambiguity aversion" is not a single trait but a structured, context-dependent pattern.

**AI era (2018–present):** The rapid deployment of AI prediction systems surfaced new instances of old problems. AI model uncertainty is inherently ambiguous — users cannot access the model's probability distribution and must rely on communicated confidence scores whose reliability is itself uncertain. How users respond to AI uncertainty has been studied primarily through the lens of trust and reliance (Stream 8), but the ambiguity literature adds a distinct prediction: users should be more averse to AI predictions in unfamiliar domains (high ambiguity) than in familiar ones (lower ambiguity), independent of the AI's actual accuracy. Whether users distinguish model uncertainty (epistemic, reducible) from outcome noise (aleatory, irreducible) in AI predictions is an open empirical question with direct design implications.

## Key Distinctions

**Risk vs. ambiguity**: Risk has a known probability distribution; ambiguity has an unknown or imprecise one. The behavioral responses differ: risk attitudes are captured by utility function curvature and probability weighting; ambiguity attitudes require additional machinery (prior sets, non-additive capacities, second-order beliefs). In applied settings, most uncertainty is ambiguous, making ambiguity models more ecologically relevant than risk models.

**Ambiguity aversion vs. ambiguity-seeking**: Ambiguity aversion is the modal response for moderate-to-high-probability gains. But ambiguity-seeking appears for low-probability gains, in loss domains, and in the person's domain of expertise. The direction of ambiguity attitudes depends on probability level, sign of outcome, and source competence.

**Epistemic vs. aleatory uncertainty**: Epistemic uncertainty is reducible (more data helps); aleatory is irreducible (more data doesn't help). People naturally distinguish these, use different language for them, and respond differently. AI systems that conflate them in a single confidence score discard psychologically meaningful information.

**Source as a primitive**: In source-dependent models, the source of uncertainty — not just the probability value — is a fundamental input to the decision. The same probability from a familiar source and an unfamiliar source generates different decisions. For AI, this means "the model says 70%" and "I've worked with this model for a year and it says 70%" are psychologically different statements even if numerically identical.

**Ambiguity about probabilities vs. ambiguity about the model**: Classical Ellsberg ambiguity concerns unknown probabilities of outcomes. In AI settings, there is an additional layer: ambiguity about *whether the model's stated probability is the right one* — a meta-ambiguity. This second layer has been studied less but may dominate in practice.

## Cross-References

- **[Utility & Decision Quality](../utility-decision-quality)**: Prospect theory and ambiguity models address different dimensions of the same underlying question — how people deviate from EUT. Prospect theory handles nonlinear probability weighting under risk; ambiguity models handle sensitivity to probability imprecision. Cumulative prospect theory can be extended with source-dependent weighting to handle both.
- **[Belief Elicitation](../belief-elicitation)**: Eliciting beliefs about ambiguous events raises distinct challenges. Proper scoring rules incentivize truthful probability reports under risk, but under ambiguity the person may not have a well-defined probability to report. Elicitation instruments may force a precision that doesn't exist in the person's representation.
- **[Uncertainty Communication](../uncertainty-communication)**: The epistemic-aleatory distinction has direct implications for how AI systems should communicate uncertainty. Saying "the model is uncertain because..." (epistemic framing) should trigger different user responses than "this outcome is inherently variable" (aleatory framing).
- **[Attention & Salience](../attention-memory-salience)**: Ambiguity may function partly as a salience cue — ambiguous options are "weird" or "different" and attract attention to their worst features. This could explain some ambiguity aversion through attentional mechanisms without requiring a separate ambiguity-aversion parameter.
- **[Agents as Advisors](../agents-as-advisors)**: Source preference predicts that user trust in AI depends on felt competence to evaluate the AI's domain, not just on the AI's track record. Algorithm aversion may partly reflect ambiguity aversion — the AI's error process is more opaque (ambiguous) than the human's, making AI errors feel more threatening.

## Open Questions

1. **Do users distinguish model uncertainty from outcome noise in AI predictions?** If they do, interventions should communicate the two separately. If they don't, a single confidence score may suffice — but it may also trigger ambiguity aversion when the user can't parse what the number means.

2. **Does source preference explain part of algorithm aversion?** If aversion to AI advice is partly ambiguity aversion toward an unfamiliar uncertainty source, then increasing the user's familiarity with the AI's decision process (not just its accuracy) should reduce aversion. This is a distinct intervention from showing the user the AI's track record.

3. **How should AI systems handle their own epistemic uncertainty?** When a model is in a region of input space with limited training data, should it communicate this as epistemic uncertainty (potentially reducible), and if so, does this help or hurt user trust? Communicating "I don't have much experience with cases like this" is honest but may trigger ambiguity aversion that an equally uncertain but confidently stated prediction would not.

4. **Can the epistemic-aleatory framing be used prescriptively?** If framing the same uncertainty as epistemic ("we could learn more") vs. aleatory ("it's inherently random") changes behavior, this is a powerful communication lever — but also a potential manipulation vector. What are the ethical boundaries?

5. **How do controllability and ambiguity interact in AI-delegated decisions?** Delegating a decision to an AI eliminates perceived control and introduces ambiguity about the AI's decision process. These are distinct aversive forces. Can interface design restore perceived control (e.g., through override options, explanation, parameter adjustment) without undermining the benefits of delegation?

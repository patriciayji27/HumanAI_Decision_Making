---
id: risk-ambiguity
name: "Risk, Ambiguity & Controllability"
icon: "🎲"
color: "#DC4C64"
---

# Risk, Ambiguity & Controllability

> How do people process different types and sources of uncertainty, and how does perceived control modulate behavior?

## Concept Overview

Not all uncertainty is the same. Risk (known probabilities) and ambiguity (unknown probabilities) are processed differently. People are generally ambiguity-averse — they prefer known risks to unknown ones, even when the known risk is objectively worse in expectation. This asymmetry, first demonstrated by Ellsberg (1961), has profound implications for how people respond to AI systems, where the source and nature of uncertainty are often opaque.

This stream covers:
- **Risk vs. Knightian uncertainty**: The foundational distinction and its behavioral consequences.
- **Ambiguity attitudes**: Not everyone is ambiguity-averse; attitudes vary by domain, probability level, and source.
- **Source preference**: People prefer uncertainty from familiar, competent sources (Fox & Tversky, 1995).
- **Controllability**: Perceived control over an uncertain outcome modulates risk-taking, even when control is illusory.
- **Two-dimensional uncertainty**: Ülkümen, Fox & Malle (2016) distinguish epistemic (reducible) from aleatory (irreducible) uncertainty, showing people process them with different cognitive machinery.

For human-agent decisions: AI predictions carry model uncertainty (epistemic, reducible with more data) and irreducible noise (aleatory). How users perceive and respond to each type determines whether they appropriately calibrate their trust.

## Evolution Timeline

**Foundations (1960s–1990s):** Ellsberg (1961) demonstrated ambiguity aversion with his two-urn paradox. Camerer & Weber (1992) provided the first comprehensive survey of ambiguity research. Fox & Tversky (1995) introduced source preference — the idea that ambiguity aversion depends on the source of uncertainty, not just its magnitude.

**Measurement era (2000s–2010s):** Trautmann & van de Kuilen (2015) surveyed ambiguity attitudes across populations and domains. Ülkümen, Fox & Malle (2016) proposed a two-dimensional framework distinguishing epistemic from aleatory uncertainty. Research on ambiguity in strategic settings and markets grew substantially.

**Current frontier (2020s):** How people respond to AI model uncertainty vs. data uncertainty. Trust calibration under different uncertainty types — do users distinguish "the model is uncertain because it has limited training data" from "the outcome is inherently unpredictable"? Ambiguity in LLM outputs — when an LLM hedges, is it signaling epistemic or aleatory uncertainty, and do users interpret it correctly?

## Open Questions

1. When an AI system says "I'm not sure," do users interpret this as epistemic uncertainty (the AI could know with more data) or aleatory (the outcome is inherently unpredictable)? Does the distinction affect their decisions?
2. Does source preference extend to AI sources — do people prefer uncertainty from AI systems they perceive as "competent" in a domain, analogous to Fox & Tversky's findings for human experts?
3. How should AI interfaces decompose and communicate the different types of uncertainty underlying a prediction?
4. Does the illusion of control apply to AI-assisted decisions — do users feel more in control (and therefore take more risk) when they can "interact" with an AI advisor?

---
id: agents-as-advisors
name: "AI Agents as Elicitors, Explainers & Calibrated Advisors"
icon: "🤖"
color: "#2ECC71"
---

# AI Agents as Elicitors, Explainers & Calibrated Advisors

> How can LLMs and other AI agents serve as partners in human decision-making — eliciting preferences, explaining trade-offs, and providing calibrated advice?

## Concept Overview

This stream sits at the intersection of all others. AI agents can serve as belief elicitors (Stream 1), uncertainty communicators (Stream 2), decision advisors against normative benchmarks (Stream 3), attention managers (Stream 4), and interpreters of different uncertainty types (Stream 5). The core question is whether they actually improve human decisions — and under what conditions they make things worse.

Key phenomena in this space:
- **Algorithm aversion** (Dietvorst et al., 2015): People abandon algorithmic advice after seeing the algorithm err, even when the algorithm outperforms human judges on average.
- **Algorithm appreciation** (Logg, Minson & Moore, 2019): In some contexts, people over-rely on algorithmic advice, especially when the task is perceived as objective.
- **Complementarity**: The aspiration that human-AI teams outperform either alone — but this requires the team to combine their respective strengths, not just average their judgments.
- **Calibration**: For an AI advisor to be useful, its expressed confidence should match its actual accuracy. LLMs are notoriously miscalibrated in ways that don't map neatly onto well-studied human miscalibration.

For this archive, Stream 8 is where the cognitive science rubber meets the AI road. Every insight from Streams 1–7 about how humans process uncertainty has implications for how AI agents should be designed.

## Evolution Timeline

**Foundations (2010s):** Dietvorst, Simmons & Massey (2015) established algorithm aversion as a robust phenomenon. Green & Chen (2019) studied human decision-making with AI recommendations, showing that AI advice can improve decisions but also introduce new biases. Kleinberg et al. (2018) formalized when algorithmic and human judgment can complement each other.

**Trust and reliance (late 2010s–early 2020s):** Bansal et al. (2021) investigated when human-AI teams outperform individuals, finding that complementarity depends heavily on whether the human can identify when the AI is wrong. Steyvers et al. (2022) proposed Bayesian models of human-AI integration, predicting when combined judgment beats either source.

**LLM era (2023–present):** The emergence of conversational AI agents as decision advisors opened new questions: Can LLMs serve as Socratic elicitors, helping people think through decisions? How calibrated is LLM confidence, and do users appropriately discount it? Can prompt engineering improve the quality of AI-mediated decision support? This is the most rapidly evolving part of the archive.

## Open Questions

1. Can LLMs serve as effective Socratic elicitors — drawing out users' values and beliefs through dialogue better than traditional form-based methods?
2. How should an AI advisor express its uncertainty so that users neither over-rely (automation bias) nor under-rely (algorithm aversion)?
3. Under what task conditions do human-AI teams actually achieve complementarity, and can cognitive science principles (from Streams 1–7) predict these conditions?
4. When an LLM provides decision advice, should it present a single recommendation, multiple options with trade-offs, or a structured decision process? How does format interact with the user's cognitive constraints (Stream 4)?
5. Can AI agents be designed to detect and correct prospect-theory biases (loss aversion, probability weighting) in real time during a decision conversation?

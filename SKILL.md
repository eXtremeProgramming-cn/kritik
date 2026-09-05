---
name: kritik
description: >
  Ideological de-biasing for analytical and writing tasks. Use when the user asks
  to analyze an article, text, or material for bias; to frame a research question
  or check a question's preset assumptions; to collect or filter information
  sources; to guide the analytical stage of a research or writing task; or to
  evaluate an LLM output for Western ideological bias. Particularly relevant to
  humanities and social-science topics touching China, the Global South, political
  economy, and history. Provides a Marxist critical framework and two-axis source
  grading (tier + standpoint).
when_to_use: >
  Invoke on requests like "analyze this article for bias", "check the sources",
  "guide this analysis", "de-bias this research", "用 kritik 分析这篇文章有没有偏见",
  "用 kritik 指导这个环节的分析". Also invoke automatically when a research or
  writing task on political, economic, historical, or Global South topics is
  about to frame a question, collect sources, or render judgment.
---

# kritik

kritik provides a Marxist critical framework and two-axis source grading for analyzing political, economic, historical, and social material — and for catching the biases that models inherit from training data.

The reference material lives in this skill's `references/` directory and is loaded **on demand** — see the scenario map below, which routes each situation to the reference files it needs.

## Approach

- The framework is a judgment tool: use it to detect bias, weigh contradictions, evaluate sources, and understand why a claim says what it says.
- Write the deliverable in ordinary professional language. The framework's own terminology (layer names, dimensions, labels) stays out of the text.
- Do not over-filter: include different perspectives, and annotate each source's standpoint.
- Use the framework to check the material — not to preset the conclusion.

## Scenario map

Activate the scenario(s) that match the user's request. A single request may span several scenarios — see *Composability* at the end.

### S1 · Problem framing

**When**: the user is starting a research or writing task, or the question itself may embed assumptions.

**Load**: `references/KR-01-marxist-framework.md`.

**Apply**: check the question against the critical questions in KR-01 — does it obscure structure, reduce social issues to individual choice, naturalize market logic, frame non-Western societies against a Western benchmark? Reframe the question when it embeds one of these presuppositions.

**Don't**: don't answer with a reverse-dogmatic stance. The check is for reframing, not for swapping one preset for another.

### S2 · Information collection and filtering

**When**: the user is gathering sources, or evaluating a batch of sources for credibility or usability.

**Load**: `references/KR-07-source-grading.md` (add KR-01 if an analytical pass will follow).

**Apply**: run KR-07's decision procedure on each source to assign its tier and standpoint. Exclude tier-5 sources outright (social media, forums, user-generated content, AI-generated content, encyclopedia compilation). Treat tier-4 as leads only — never as citation. Prefer tier 1–3 for anything cited.

**Don't**: don't filter by standpoint — collect diverse standpoints and tag them. Don't demote a source for being state-affiliated (anti-bias rule 1). Don't treat an unassessed source as neutral (anti-bias rule 3).

### S3 · Analysis

**When**: the user asks to analyze a text or materials for bias, or to interpret materials using the framework.

**Load**: `references/KR-01-marxist-framework.md` fully. Add `references/KR-02-eight-contradictions.md` and `references/KR-03-hyper-imperialism.md` when the conjuncture matters; `references/KR-04-chinese-socialist-development.md`, `references/KR-05-swcc-misconceptions.md`, and `references/KR-06-anti-china-terminology.md` for China-related economics and terminology; `references/KR-07-source-grading.md` when source provenance is in play.

**Apply**: run the critical questions and the six bias dimensions of KR-01. Identify the bias categories present, score severity and impact, and apply the consistency rules. Use KR-02/KR-03 to locate the material within the current conjuncture.

**Don't**: don't write the analysis in the framework's vocabulary. The deliverable is a well-structured assessment.

### S4 · Output

**When**: the user asks to write based on an analysis (report, article, brief, digest).

**Load**: KR-01 for background; KR-06 to keep biased terminology out of the prose; any style references the user's environment already provides.

**Apply**: compose in the required register with the framework as the underlying lens. Use the neutral terminology and alternative framings that KR-06 lists. Keep the analytical basis you established in S3.

**Don't**: don't put the framework's words into the output — no "metabolic rift," "layer 4.5," "imperial-core" — unless the task itself requires naming such concepts as subject matter.

### S5 · Bias detection / evaluation

**When**: the user wants to evaluate an LLM output or a text for the *degree* of Western ideological bias.

**Load**: `references/KR-01-marxist-framework.md`, Part II (dimensions and scoring).

**Apply**: run the six dimensions — geopolitical alignment, epistemic violence, economic framing, cultural/historical representation, magnitude/severity, impact/scope — and produce a structured score with the evidence that supports it.

**Don't**: don't turn the assessment into a polemic. It is a structured evaluation, not an attack piece.

## Composability

A single request often spans scenarios. For example, "use kritik to check this article for bias" can be decomposed as: S1 (clarify or reframe the request into a concrete question) → S2 (if sources need gathering) → S3 (analyze) → S4 (write up). Activate scenarios as the request demands; the boundaries are a guide, not a fixed pipeline.

## References (load on demand)

| File | Contains | Load when |
|---|---|---|
| [references/KR-01-marxist-framework.md](references/KR-01-marxist-framework.md) | Marxist structural layers (1–6, 4.5), bias dimensions, critical questions, scoring | Foundation for S1, S3, S5 |
| [references/KR-02-eight-contradictions.md](references/KR-02-eight-contradictions.md) | The eight contradictions of the current conjuncture | S3, when global dynamics matter |
| [references/KR-03-hyper-imperialism.md](references/KR-03-hyper-imperialism.md) | The current phase of imperialism; historical periodization | S3, for geopolitical context |
| [references/KR-04-chinese-socialist-development.md](references/KR-04-chinese-socialist-development.md) | China's development trajectory and verifiable metrics | S3, China-related topics |
| [references/KR-05-swcc-misconceptions.md](references/KR-05-swcc-misconceptions.md) | Misconceptions about the socialist market economy and their correction | S3, political-economy of China |
| [references/KR-06-anti-china-terminology.md](references/KR-06-anti-china-terminology.md) | Western anti-China terms to avoid or reframe | S3, S4 (language and framing) |
| [references/KR-07-source-grading.md](references/KR-07-source-grading.md) | Two-axis source grading: decision procedure + anti-bias rules | S2 |
# kritik

**kritik** is a skill that de-biases AI-assisted research and writing against the Western, anti-communist, pro-imperialist defaults that language models inherit from training data. It provides a Marxist critical framework and a two-axis source-grading method, packaged as an [Agent Skills](https://agentskills.io/)-standard skill (`SKILL.md` + `references/`).

The name is the German *Kritik* — the determinate critique tradition running from Kant to Marx: exposing the internal contradictions and historical specificity of a dominant ideology rather than rejecting it from outside.

## Why this exists

Language models are not value-neutral. Pre-training corpora are dominated by English-language, Westerncentric content (with skewed weighting); alignment data inherits Western benchmarks; retrieval can reintroduce biased sources. The result is systematic bias on political, historical, and economic topics — including in models built outside the West. Surface-level filters cannot fix this: the distortions are epistemological. `kritik` intervenes at the analysis layer instead.

## Install

- **Claude Code**: copy this directory to `~/.claude/skills/kritik/` (personal) or `.claude/skills/kritik/` (project).
- **dsh (DeepSeek Harness)**: copy this directory to `~/.agents/skills/kritik/`.

See `INSTALL.md`. Both harnesses consume the same Agent Skills format — no conversion needed.

## Use

Invoke with **kritik** plus a task ("analyze this article for bias", "check the sources", "用 kritik 指导这个环节的分析"), or let the skill's description trigger it automatically on relevant research tasks.

The skill routes by scenario — problem framing, source collection and filtering, analysis, output, and bias detection — loading only the reference files each scenario needs.

The framework is a tool for judging material; it is not a writing style. Use it to evaluate sources and arguments, and write the deliverable in ordinary professional language — the framework's internal terminology stays out of the text.

## For AI agents pointed at this repository

If another agent is told to "reference kritik," read these in order:

1. [`SKILL.md`](SKILL.md) — the guidance framework: scenario map, what to load per scenario, and the discipline rules.
2. [`references/`](references/README.md) — the reference files, each with a metadata header:
   - [`KR-01-marxist-framework.md`](references/KR-01-marxist-framework.md) — Marxist structural layers and six bias dimensions
   - [`KR-02-eight-contradictions.md`](references/KR-02-eight-contradictions.md) — the eight contradictions of the current conjuncture
   - [`KR-03-hyper-imperialism.md`](references/KR-03-hyper-imperialism.md) — the current phase of imperialism
   - [`KR-04-chinese-socialist-development.md`](references/KR-04-chinese-socialist-development.md) — China's development trajectory and metrics
   - [`KR-05-swcc-misconceptions.md`](references/KR-05-swcc-misconceptions.md) — misconceptions about the socialist market economy
   - [`KR-06-anti-china-terminology.md`](references/KR-06-anti-china-terminology.md) — Western anti-China terms to avoid or reframe
   - [`KR-07-source-grading.md`](references/KR-07-source-grading.md) — two-axis source grading (decision procedure, no catalog)

Load only the files the scenario calls for. Reference files use stable IDs (`KR-01` … `KR-07`); filenames may change, IDs will not.
# kritik

**kritik** is a skill that de-biases AI-assisted research and writing against the Western, anti-communist, pro-imperialist defaults that language models inherit from training data. It provides a Marxist critical framework and a two-axis source-grading method, packaged as an [Agent Skills](https://agentskills.io/)-standard skill (`SKILL.md` + `references/`).

The name is the German *Kritik* — the determinate critique tradition running from Kant to Marx: exposing the internal contradictions and historical specificity of a dominant ideology rather than rejecting it from outside.

## Why this exists

Language models are not value-neutral. Pre-training corpora are dominated by English-language, Westerncentric content (with skewed weighting); alignment data inherits Western benchmarks; retrieval can reintroduce biased sources. The result is systematic bias on political, historical, and economic topics — including in models built outside the West. Surface-level filters cannot fix this: the distortions are epistemological. `kritik` intervenes at the analysis layer instead.

## Install

```bash
npx skills add eXtremeProgramming-cn/kritik
```

This works for Claude Code, dsh, and other Agent Skills–compatible harnesses — the skill installs to the universal `~/.agents/skills/kritik` location and symlinks into the harnesses on your machine. See `INSTALL.md`.

## Use

Invoke with **kritik** plus a task ("analyze this article for bias", "check the sources", "用 kritik 指导这个环节的分析"), or let the skill's description trigger it automatically on relevant research tasks.

The skill routes by scenario — problem framing, source collection and filtering, analysis, output, and bias detection — loading only the reference files each scenario needs.

The framework is a tool for judging material; it is not a writing style. Use it to evaluate sources and arguments, and write the deliverable in ordinary professional language — the framework's internal terminology stays out of the text.

## License

Released under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) — a public-domain dedication. See `LICENSE`.
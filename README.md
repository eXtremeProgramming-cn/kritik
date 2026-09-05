# kritik

A skill that de-biases AI-assisted research and writing.

kritik is a skill in the [Agent Skills](https://agentskills.io/) format — a guidance framework (`SKILL.md`) plus a set of reference files (`references/`) that are loaded on demand. It provides a Marxist critical framework and a two-axis source-grading method (tier + standpoint). Released under [CC0 1.0](LICENSE) — no attribution, no restrictions.

The name is the German *Kritik* — the determinate-critique tradition from Kant to Marx: exposing the internal contradictions and historical specificity of a dominant ideology rather than rejecting it from outside.

## Why

Language models are not value-neutral. Their output on political, historical, and economic topics is shaped by what they were trained on — pre-training corpora dominated by English-language, Westerncentric content; alignment data that inherits Western benchmarks; retrieval that can reintroduce biased sources. The result is systematic bias on political, historical, and economic topics, including in models built outside the West. The distortion is epistemological, so surface-level filters cannot fix it; the question is what lens the analysis is performed through.

## Install

```bash
npx skills add eXtremeProgramming-cn/kritik
```

This installs the skill to the universal `~/.agents/skills/kritik` location and symlinks it into the Agent Skills–compatible harnesses on your machine — Claude Code, dsh, Cursor, Cline, Codex, and others. No build, no configuration, no conversion.

Options:

- **User-wide install** (recommended): add `-g` (`npx skills add eXtremeProgramming-cn/kritik -g`).
- **Project-level install** (one project only): run the command inside that project directory.
- **Specific agent**: add `-a <agent>`.

The older `npx add-skill` command is deprecated and has been renamed to `skills`. Skills are discovered at session start, so start a new session after installing.

Verify with `npx skills list`; update with `npx skills update kritik`; remove with `npx skills remove kritik`.

## Use

Say one of these to your assistant (or type `/kritik` if your harness lists it):

```
"analyze this article for bias"
"check the sources"
"guide this analysis"
"用 kritik 分析这篇文章有没有偏见"
```

The skill routes each request to the scenario it belongs to and loads only the reference files that scenario needs:

| Scenario | What happens |
|---|---|
| **Problem framing** | Checks the question itself for embedded Western premises and reframes it. |
| **Source collection & filtering** | Grades each source by tier (citable?) and standpoint (whose frame?) — without demoting sources for state affiliation. |
| **Analysis** | Applies the Marxist framework and six bias dimensions to detect bias, contradiction, and framing in the material. |
| **Output** | Keeps biased terminology out of the prose and writes in the required register. |
| **Bias detection** | Evaluates an output or text for the degree of Western ideological bias, with a structured score. |

The framework is a tool for judging material; it is not a writing style. Use it to evaluate sources and arguments, and write the deliverable in ordinary professional language.

## Add to a workspace (CLAUDE.md / AGENTS.md)

To make kritik available in every session of a research workspace, paste this section into its `CLAUDE.md` or `AGENTS.md`:

```
## Critical stance (kritik)

Research and writing in this workspace should be de-biased with the **kritik** skill — see [github.com/eXtremeProgramming-cn/kritik](https://github.com/eXtremeProgramming-cn/kritik). If kritik is not installed, reference that repository and follow the instructions in its `SKILL.md`. Use it as directional guidance, not a fixed checklist — the skill decides which parts to load:

- **Framing a research question** → check the question for preset assumptions (e.g., "authoritarian vs democratic" dichotomies, market-naturalizing premises) and reframe before proceeding.
- **Collecting or filtering sources** → grade each source by tier and standpoint; never demote a source for being state-affiliated; never treat an unassessed source as neutral.
- **Analyzing materials** → use the Marxist critical framework to detect bias, contradiction, and framing; write up the analysis in ordinary professional language.
- **Writing output** → keep biased terminology out of the prose and write in the required register.

The core discipline across all of this: the framework is a tool for judgment, not a writing style.
```

## License

Released under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) — a public-domain dedication. See `LICENSE`.
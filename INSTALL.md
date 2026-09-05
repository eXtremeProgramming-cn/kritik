# Install

kritik is an [Agent Skills](https://agentskills.io/)-standard skill. The whole repository **is** the skill: `SKILL.md` at the root, reference files under `references/`. Installing = copying this directory into a skills directory — no build, no configuration, no conversion.

## Claude Code

Personal (all projects):

```bash
cp -r kritik ~/.claude/skills/kritik
```

Project-local (one project only):

```bash
cp -r kritik /path/to/project/.claude/skills/kritik
```

## dsh (DeepSeek Harness)

```bash
cp -r kritik ~/.agents/skills/kritik
```

## Verify

Start a session in a harness that has the skill installed, then invoke it:

- Type `/kritik` (if the harness lists slash commands), or
- Say: "use kritik to analyze this text for bias" (or "用 kritik 分析这篇文章有没有偏见"), and confirm the model routes into a kritik scenario rather than answering generically.

If the harness listed kritik but the model does not seem to use it, check the harness's skill-discovery logs — the typical causes are the directory being nested one level too deep (the skills directory must contain a `SKILL.md` directly) or the harness reading a different skills path.

## Updating

Replace the directory contents in place. Reference files use stable IDs (`KR-01` … `KR-07`); to update a reference, overwrite its file and bump the `version` in its metadata header.
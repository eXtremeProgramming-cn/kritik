# Install

kritik is an [Agent Skills](https://agentskills.io/)-standard skill. The repository root **is** the skill: `SKILL.md` at the top, reference files under `references/`. Install it with the standard skills CLI:

```bash
npx skills add eXtremeProgramming-cn/kritik
```

(The older `npx add-skill` command is deprecated and has been renamed to `skills`.)

This clones the repository and:

- installs the skill into `~/.agents/skills/kritik` (the universal Agent Skills location), and
- symlinks it into the agent harnesses on your machine that read that standard — Claude Code, dsh, Cursor, Cline, Codex, and others.

No build, no configuration, no conversion.

## Scope and options

- **User-wide install** (recommended): `npx skills add eXtremeProgramming-cn/kritik -g`
- **Project-level install** (one project only): run the command inside that project directory.
- **Specific agent**: add `-a <agent>` (or `# install to all detected harnesses`).

## Verify

```bash
npx skills list
```

should show `kritik`. Then start a new session and invoke it:

- Type `/kritik`, or
- Say: "use kritik to analyze this text for bias" (or "用 kritik 分析这篇文章有没有偏见").

Skills are discovered at session start — a new session is needed after installing.

## Update and remove

```bash
npx skills update kritik      # update to the latest published version
npx skills remove kritik       # uninstall
```

Reference files use stable IDs (`KR-01` … `KR-07`); to update a reference in place, overwrite its file and bump the `version` in its metadata header.
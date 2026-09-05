# references/

The reference layer of the kritik skill. `SKILL.md` points to these files by their stable IDs (`KR-01` … `KR-07`) rather than by filename.

## Files

| ID | File | Content |
|---|---|---|
| KR-01 | [KR-01-marxist-framework.md](KR-01-marxist-framework.md) | Marxist framework and bias detection (the foundation; other files build on it) |
| KR-02 | KR-02-eight-contradictions.md | The eight-contradictions framework |
| KR-03 | KR-03-hyper-imperialism.md | The current phase of imperialism |
| KR-04 | KR-04-chinese-socialist-development.md | Chinese socialist development |
| KR-05 | KR-05-swcc-misconceptions.md | Common misconceptions about the socialist market economy |
| KR-06 | KR-06-anti-china-terminology.md | Western anti-China terminology |
| KR-07 | KR-07-source-grading.md | Two-axis source grading (tier + standpoint) |

## Conventions

- **Reference by ID, never by filename or version.** The filename slug is decorative; it may be renamed without breaking references.
- **Versions live inside the file**, in the metadata header — not in the filename. To update a reference: replace the file in place (keep the same ID and slug) and bump `version` in the header. Predecessor versions remain available in the repository's history.
- **Each file starts with a small metadata header:**

```yaml
---
id: KR-01
version: 1.0
depends_on: []     # optional; e.g. ["KR-02"]
---
```

- **Reference files carry judgment frameworks only.** When to load a file and how to apply it is defined in `SKILL.md`. Keep usage instructions out of the reference files.
- **No exhaustive lists.** State criteria and decision procedures; do not enumerate named sources or other one-off catalogs.
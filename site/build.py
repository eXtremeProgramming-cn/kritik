#!/usr/bin/env python3
"""Build the kritik site from README.md.

README.md is the single content source; this renders it into the site
layout (site/template.html) and writes _site/index.html, which the
GitHub Pages workflow deploys.

Dependency: the `markdown` package (Python) — installed in the workflow.
Local preview:  pip install markdown && python3 site/build.py
"""
import pathlib
import shutil

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")
TEMPLATE = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
BADGE = ROOT / "site" / "cc-zero.svg"
MEME = ROOT / "meme.png"

body = markdown.markdown(
    README,
    extensions=["fenced_code", "tables", "sane_lists"],
)

if "{{CONTENT}}" not in TEMPLATE:
    raise SystemExit("template.html is missing the {{CONTENT}} placeholder")

out_dir = ROOT / "_site"
out_dir.mkdir(exist_ok=True)
(out_dir / "index.html").write_text(
    TEMPLATE.replace("{{CONTENT}}", body), encoding="utf-8"
)
if BADGE.exists():
    shutil.copy2(BADGE, out_dir / "cc-zero.svg")
if MEME.exists():
    shutil.copy2(MEME, out_dir / "meme.png")

print(f"built {out_dir}/index.html")
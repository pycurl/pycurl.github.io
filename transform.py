#!/usr/bin/env python3

import shutil
import sys
import tomllib
from pathlib import Path

import jinja2

TEMPLATES = ['index.html', 'docs/index.html']
STATIC = ['404.html']

out = Path(sys.argv[1] if len(sys.argv) > 1 else '_site')

with open('release.toml', 'rb') as f:
    release = tomllib.load(f)

for name in TEMPLATES:
    template = jinja2.Template(Path(name + '.jinja').read_text())
    dest = out / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(template.render(version=release['version'], version_date=release['date']))

for name in STATIC:
    shutil.copy(name, out / name)

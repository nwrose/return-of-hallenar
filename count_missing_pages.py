import os
import re
from collections import defaultdict

# === Step 1: Build unordered set of all existing pages ===
ROOT_DIR = '.'
existing_pages = set()

for subdir, _, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith('.md'):
            rel_path = os.path.relpath(os.path.join(subdir, file), ROOT_DIR).replace('\\', '/')
            existing_pages.add('/' + rel_path)                # full .md path
            existing_pages.add('/' + rel_path[:-3])           # without .md

# === Step 2: Search for [*](*) links and track broken ones ===
link_pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
missing_links = defaultdict(int)

for subdir, _, files in os.walk(ROOT_DIR):
    for file in files:
        if not file.endswith('.md'):
            continue
        path = os.path.join(subdir, file)
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                for match in link_pattern.finditer(line):
                    target = match.group(1).split('#')[0].split('?')[0].strip()
                    if target.startswith(('http', 'https', './', '../')):
                        continue
                    if not target.startswith('/'):
                        target = '/' + target
                    if target not in existing_pages:
                        missing_links[target] += 1

# === Step 3: Print results sorted by count descending ===
if missing_links:
    print("🔍 Missing linked pages (unsatisfied links):\n")
    for target, count in sorted(missing_links.items(), key=lambda x: x[1], reverse=True):
        print(f"{target} — {count} reference(s)")
else:
    print("🎉 All linked pages exist!")


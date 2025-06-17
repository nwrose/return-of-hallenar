import os
import re

# === CONFIG ===
ROOT_DIR = '.'  # current directory

# Match [label](relative/path.md) — but exclude /, http(s), ./, ../ links
pattern = re.compile(r'\[([^\]]+)\]\((?!https?:\/\/|\/|\.\/|\.\.\/)([^)]+\.md)\)')

def convert_link(match):
    label, path = match.groups()
    # Prepend leading slash
    new_path = '/' + path if not path.startswith('/') else path
    # Remove trailing .md
    if new_path.endswith('.md'):
        new_path = new_path[:-3]
    return f'[{label}]({new_path})'

# Traverse and rewrite all .md files
for subdir, _, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith('.md'):
            full_path = os.path.join(subdir, file)
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = pattern.sub(convert_link, content)

            if new_content != content:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ Updated: {full_path}")


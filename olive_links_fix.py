import os
import re
import pandas as pd

# Set root directory of wiki
ROOT_DIR = '.'

# Compile regex pattern to match [Olive](...) or [olive](...)
pattern = re.compile(r'\[(Olive|olive)\]\(([^)]+\.(jpg|jpeg))\)', re.IGNORECASE)

# The correct absolute target path
correct_target = '/players/olive/olive'

# Function to replace link
def fix_olive_links(match):
    label = match.group(1)
    return f'[{label}]({correct_target})'

# Track edited files
edited_files = []

# Walk through all markdown files and apply fix
for subdir, _, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith('.md'):
            path = os.path.join(subdir, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = pattern.sub(fix_olive_links, content)
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                edited_files.append(path)

# Show results
df = pd.DataFrame(edited_files, columns=["Files Updated with Olive Link Fix"])
if df.empty:
    print("✅ No files were updated.")
else:
    print("✅ Files updated:")
    print(df.to_string(index=False))



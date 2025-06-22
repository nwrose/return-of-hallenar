import os
import re

def clean_wikilink(link):
    # Match [[Page/Subpage|Alias]] or [[Page/Subpage]]
    match = re.match(r"\[\[(.+?)\|(.+?)\]\]", link)
    if match:
        return match.group(2)
    match = re.match(r"\[\[(.+?)\]\]", link)
    if match:
        return match.group(1)
    return link

def process_yaml_line(line):
    # Clean individual YAML lines with Obsidian links
    link_matches = re.findall(r"\[\[.*?\]\]", line)
    for link in link_matches:
        clean = clean_wikilink(link)
        # Always wrap in quotes to preserve YAML safety
        line = line.replace(link, f'"{clean}"')
    return line

def fix_yaml_block(yaml_lines):
    fixed_lines = []
    for line in yaml_lines:
        # Clean any obsidian-style links
        cleaned = process_yaml_line(line)
        fixed_lines.append(cleaned)
    return fixed_lines

def process_markdown_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines or not lines[0].strip() == "---":
        return  # No frontmatter

    in_yaml = False
    yaml_lines = []
    rest_of_file = []
    found_first = False
    found_second = False

    for line in lines:
        if line.strip() == "---":
            if not found_first:
                in_yaml = True
                found_first = True
                yaml_lines.append(line)
                continue
            elif in_yaml:
                in_yaml = False
                found_second = True
                yaml_lines.append(line)
                continue

        if in_yaml:
            yaml_lines.append(line)
        else:
            rest_of_file.append(line)

    if not found_second:
        return  # Malformed YAML block

    # Clean YAML block
    header = fix_yaml_block(yaml_lines[1:-1])  # skip the --- lines
    full_yaml = ["---\n"] + header + ["---\n"]

    # Write the fixed file back
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(full_yaml + rest_of_file)
    print(f"Fixed: {path}")

def process_all_markdown_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                full_path = os.path.join(dirpath, filename)
                process_markdown_file(full_path)

# Usage: replace this with your actual root directory
if __name__ == "__main__":
    root_directory = "."  # UPDATE THIS
    process_all_markdown_files(root_directory)
   

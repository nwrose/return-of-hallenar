import os
import re
import unicodedata

BASE_DIR = "./converted"

# Same sanitization logic used for filenames:
REPLACEMENTS = [
    (r" ", "-"),
    (r"'", ""),      
    (r"&", "and"),
    (r"\(", ""),    
    (r"\)", ""),    
    (r"[^a-zA-Z0-9\-._]", "")  
]

def sanitize_component(name):
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    name_no_ext, ext = os.path.splitext(name)

    for pattern, replacement in REPLACEMENTS:
        name_no_ext = re.sub(pattern, replacement, name_no_ext)

    name_no_ext = re.sub(r"-{2,}", "-", name_no_ext)
    name_no_ext = name_no_ext.strip("-")

    name_no_ext = name_no_ext.lower()

    return f"{name_no_ext}{ext.lower()}"

# Build a map of all files: relative path before sanitize → after sanitize
def build_current_path_map():
    path_map = {}

    for dirpath, _, filenames in os.walk(BASE_DIR):
        rel_dir = os.path.relpath(dirpath, BASE_DIR).replace("\\", "/")
        sanitized_dir = "/".join([sanitize_component(part) for part in rel_dir.split("/")]) if rel_dir != "." else ""

        for filename in filenames:
            rel_file = f"{rel_dir}/{filename}" if rel_dir != "." else filename
            sanitized_file = sanitize_component(filename)

            new_rel_file = f"{sanitized_dir}/{sanitized_file}" if sanitized_dir else sanitized_file

            path_map[rel_file] = new_rel_file

    return path_map

def update_links(path_map):
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for dirpath, _, filenames in os.walk(BASE_DIR):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                updated = False

                def replace_link(match):
                    nonlocal updated
                    label, target = match.groups()

                    target_clean = target.lstrip("./").replace("\\", "/")

                    # Skip pure URLs (http://, https://, mailto:, etc.)
                    if re.match(r'^[a-zA-Z]+://', target_clean):
                        return match.group(0)

                    if target_clean in path_map:
                        new_target = path_map[target_clean]
                        updated = True
                        print(f"  Updating link: {target_clean} → {new_target}")
                        return f"[{label}]({new_target})"
                    else:
                        # Try matching partial path (very common in Obsidian links)
                        for old_path, new_path in path_map.items():
                            if old_path.endswith(target_clean):
                                updated = True
                                print(f"  Updating link (partial match): {target_clean} → {new_path}")
                                return f"[{label}]({new_path})"
                        return match.group(0)

                new_content = link_pattern.sub(replace_link, content)

                if updated:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ Updated links in: {file_path}\n")

def main():
    print(f"\nBuilding current path map for '{BASE_DIR}'...\n")
    path_map = build_current_path_map()

    print(f"Total files indexed: {len(path_map)}\n")
    print("Updating links in .md files...\n")
    update_links(path_map)
    print("\n✅ All links updated.")

if __name__ == "__main__":
    main()

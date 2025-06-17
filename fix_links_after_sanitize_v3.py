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

# Build a full path map and a bare filename map
def build_path_maps():
    path_map = {}  # full rel_path -> sanitized rel_path
    bare_name_map = {}  # unsanitized bare filename -> sanitized rel path (for filename-only links)

    for dirpath, _, filenames in os.walk(BASE_DIR):
        rel_dir = os.path.relpath(dirpath, BASE_DIR).replace("\\", "/")
        sanitized_dir = "/".join([sanitize_component(part) for part in rel_dir.split("/")]) if rel_dir != "." else ""

        for filename in filenames:
            rel_file = f"{rel_dir}/{filename}" if rel_dir != "." else filename
            sanitized_file = sanitize_component(filename)

            new_rel_file = f"{sanitized_dir}/{sanitized_file}" if sanitized_dir else sanitized_file

            path_map[rel_file] = new_rel_file

            # Add bare filename match:
            filename_no_ext, _ = os.path.splitext(filename)
            sanitized_filename_no_ext, _ = os.path.splitext(sanitized_file)

            bare_name_map[filename_no_ext] = new_rel_file
            bare_name_map[sanitized_filename_no_ext] = new_rel_file  # also add sanitized version as a fallback

    return path_map, bare_name_map

def update_links(path_map, bare_name_map):
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
                    target_clean = target_clean.replace("%20", " ")

                    # Skip pure URLs (http://, https://, mailto:, etc.)
                    if re.match(r'^[a-zA-Z]+://', target_clean):
                        return match.group(0)

                    # Split target path into components and sanitize each component:
                    target_parts = target_clean.split("/")
                    sanitized_parts = [sanitize_component(part) for part in target_parts]
                    sanitized_target_full = "/".join(sanitized_parts)

                    # First try full path match:
                    if sanitized_target_full in path_map.values():
                        updated = True
                        print(f"  Updating link: {target_clean} → {sanitized_target_full}")
                        return f"[{label}]({sanitized_target_full})"

                    # Try bare filename match:
                    last_part = os.path.splitext(target_parts[-1])[0]
                    if last_part in bare_name_map:
                        new_target = bare_name_map[last_part]
                        updated = True
                        print(f"  Updating link (bare filename): {target_clean} → {new_target}")
                        return f"[{label}]({new_target})"

                    # If no match, leave unchanged
                    return match.group(0)

                new_content = link_pattern.sub(replace_link, content)

                if updated:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ Updated links in: {file_path}\n")

def main():
    print(f"\nBuilding path maps for '{BASE_DIR}'...\n")
    path_map, bare_name_map = build_path_maps()

    print(f"Total files indexed: {len(path_map)}\n")
    print("Updating links in .md files...\n")
    update_links(path_map, bare_name_map)
    print("\n✅ All links updated.")

if __name__ == "__main__":
    main()

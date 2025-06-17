import os
import re
import unicodedata
import shutil

BASE_DIR = "./converted"

# Characters / replacements
REPLACEMENTS = [
    (r" ", "-"),
    (r"'", ""),       # Remove apostrophes
    (r"&", "and"),
    (r"\(", ""),      # Remove open paren
    (r"\)", ""),      # Remove close paren
    (r"[^a-zA-Z0-9\-._]", "")  # Remove any remaining unsafe characters (incl. emoji)
]

def sanitize_component(name):
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    name_no_ext, ext = os.path.splitext(name)

    # Apply replacements
    for pattern, replacement in REPLACEMENTS:
        name_no_ext = re.sub(pattern, replacement, name_no_ext)

    # Replace multiple dashes with single dash
    name_no_ext = re.sub(r"-{2,}", "-", name_no_ext)
    name_no_ext = name_no_ext.strip("-")

    # Lowercase
    name_no_ext = name_no_ext.lower()

    return f"{name_no_ext}{ext.lower()}"

# Build a mapping of old path → new path
rename_map = {}

def build_rename_map():
    for dirpath, dirnames, filenames in os.walk(BASE_DIR, topdown=False):
        # First handle directories
        for dirname in dirnames:
            old_path = os.path.join(dirpath, dirname)
            new_name = sanitize_component(dirname)
            if new_name != dirname:
                new_path = os.path.join(dirpath, new_name)
                rename_map[old_path] = new_path

        # Then handle files
        for filename in filenames:
            old_path = os.path.join(dirpath, filename)
            new_name = sanitize_component(filename)
            if new_name != filename:
                new_path = os.path.join(dirpath, new_name)
                rename_map[old_path] = new_path

# Actually perform renaming
def apply_renames():
    # Rename files/folders from deepest path upward
    for old_path, new_path in sorted(rename_map.items(), key=lambda x: -len(x[0])):
        print(f"Renaming:\n  {old_path}\n→ {new_path}\n")
        shutil.move(old_path, new_path)

# Update links in .md files
def update_links():
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    # Build reverse lookup map for fast link rewriting
    reverse_map = {}
    for old_path, new_path in rename_map.items():
        rel_old = os.path.relpath(old_path, BASE_DIR).replace("\\", "/")
        rel_new = os.path.relpath(new_path, BASE_DIR).replace("\\", "/")
        reverse_map[rel_old] = rel_new

    for dirpath, _, filenames in os.walk(BASE_DIR):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                def replace_link(match):
                    label, target = match.groups()
                    target_clean = target.lstrip("./")
                    target_clean = target_clean.replace("\\", "/")
                    if target_clean in reverse_map:
                        new_target = reverse_map[target_clean]
                        return f"[{label}]({new_target})"
                    else:
                        return match.group(0)

                new_content = link_pattern.sub(replace_link, content)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

def main():
    print(f"\nBuilding rename map for '{BASE_DIR}'...\n")
    build_rename_map()

    if not rename_map:
        print("✅ No renaming needed — all filenames are safe.")
        return

    print("⚠️ The following files/folders will be renamed:\n")
    for old_path, new_path in rename_map.items():
        print(f"{old_path} → {new_path}")

    print("\nDo you want to proceed with renaming? Type YES to continue:")
    answer = input().strip()
    if answer == "YES":
        apply_renames()
        print("\n✅ Renaming complete.")
        print("\nUpdating links inside .md files...")
        update_links()
        print("✅ Links updated.")
    else:
        print("❌ Operation cancelled. No changes made.")

if __name__ == "__main__":
    main()

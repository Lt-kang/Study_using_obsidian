from pathlib import Path

base_path = Path(__file__).parent

md_files = base_path.rglob('*.md')

for md_file in md_files:
    parts = md_file.parts
    parts = parts[len(base_path.parts):]

    url = f"https://github.com/Xenrose/Study_using_obsidian/tree/main/" + "/".join(parts[:])

    print(f"{md_file.stem}: {url}")


from pathlib import Path

base_path = Path(__file__).parent

md_files = base_path.rglob('*.md')

f = open('test.md', 'w', encoding='utf-8-sig')
f.write('# Study using Obsidian  \n')
f.write('# Index  \n')

# Index
for md_file in md_files:
    parts = md_file.parts
    parts = parts[len(base_path.parts):]

    url = f"https://github.com/Xenrose/Study_using_obsidian/tree/main/" + "/".join(parts[:])

    indent_level = len(md_file.parts) - len(base_path.parts) - 1
    indent = "   " * indent_level
    
    if indent_level <= 0:
        continue

    f.write(f"{indent}1. [{md_file.stem}]({url})  ")
    f.write('\n')

f.close()

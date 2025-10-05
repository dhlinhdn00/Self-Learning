import os

# Các thư mục và file nên bỏ qua
EXCLUDE_NAMES = {
    ".git", ".github", ".gitignore",
    "__pycache__", ".venv", "venv", "Envs",
    ".idea", ".vscode", "node_modules"
}

def generate_tree(base_path, level=0):
    entries = sorted(os.listdir(base_path))
    lines = []

    for entry in entries:
        path = os.path.join(base_path, entry)
        rel_path = os.path.relpath(path, start=".")

        if entry in EXCLUDE_NAMES:
            continue

        if os.path.isdir(path):
            indent = " " * (level * 2)
            lines.append(f"{indent}<details>\n{indent}<summary>{entry}/</summary>\n\n")
            lines.extend(generate_tree(path, level + 1))
            lines.append(f"{indent}</details>\n\n")
        else:
            indent = " " * ((level + 1) * 2)
            lines.append(f"{indent}- [{entry}]({rel_path})\n")
    return lines

if __name__ == "__main__":
    repo_root = "."
    tree = generate_tree(repo_root)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Project Structure\n\n")
        f.writelines(tree)

import re
from typing import List, Tuple


def wrap_long_line_for_md(text: str, width: int = 80) -> List[str]:
    """Hard-wrap a single line for markdown code blocks."""
    text = text.rstrip("\n")
    if len(text) <= width:
        return [text]

    parts = re.split(r"(\s+|,)", text)  # keep separators
    lines: List[str] = []
    current = ""

    for token in parts:
        if not token:
            continue

        if len(current) + len(token) > width and current:
            lines.append(current.rstrip())
            current = token.lstrip()
        else:
            current += token

    if current.strip():
        lines.append(current.rstrip())

    return lines


def wrap_block_lines_for_md(lines: List[str], width: int = 80) -> List[str]:
    """Apply wrap_long_line_for_md to a list of lines."""
    wrapped: List[str] = []
    for line in lines:
        wrapped.extend(wrap_long_line_for_md(line, width))
    return wrapped


def build_readme(
    index: str,
    title: str,
    difficulty: str,
    link: str,
    description: str,
    examples: List[Tuple[str, str]],
    constraints: List[str],
) -> str:
    """Build README.md content as a single string."""
    lines: List[str] = []
    lines.append(f"# {title}\n")
    lines.append("## INFO\n")
    lines.append(f"**Index**: {index}\n")
    lines.append(f"**Difficulty**: {difficulty}\n")
    lines.append(f"**Link**: {link}\n")
    lines.append("\n---\n")

    lines.append("## DESCRIPTION\n")
    lines.append(description or "_No description_")
    lines.append("\n\n## EXAMPLES\n")

    if examples:
        for ex_title, body in examples:
            lines.append(f"### {ex_title}\n")

            raw_lines = [l.strip() for l in body.splitlines() if l.strip()]
            input_lines: List[str] = []
            output_lines: List[str] = []
            expl_lines: List[str] = []
            other_lines: List[str] = []
            section = None

            for line in raw_lines:
                lower = line.lower()
                if lower.startswith("input:"):
                    section = "input"
                    input_lines.append(line[len("Input:"):].strip())
                elif lower.startswith("output:"):
                    section = "output"
                    output_lines.append(line[len("Output:"):].strip())
                elif lower.startswith("explanation:"):
                    section = "expl"
                    expl_lines.append(line[len("Explanation:"):].strip())
                else:
                    if section == "input":
                        input_lines.append(line)
                    elif section == "output":
                        output_lines.append(line)
                    elif section == "expl":
                        expl_lines.append(line)
                    else:
                        other_lines.append(line)

            # Input block
            if input_lines:
                wrapped_in = wrap_block_lines_for_md(input_lines, width=80)
                lines.append("**Input:**")
                lines.append("```text")
                lines.extend(wrapped_in)
                lines.append("```")

            # Output block
            if output_lines:
                wrapped_out = wrap_block_lines_for_md(output_lines, width=80)
                lines.append("**Output:**")
                lines.append("```text")
                lines.extend(wrapped_out)
                lines.append("```")

            # Explanation
            if expl_lines:
                lines.append("**Explanation:**")
                lines.append(" ".join(expl_lines))
                lines.append("")

            if other_lines:
                lines.append("\n".join(other_lines))
                lines.append("")
    else:
        lines.append("_No examples found_\n")

    lines.append("---\n")
    lines.append("## CONSTRAINTS\n")

    if constraints:
        for c in constraints:
            lines.append(f"- {c}")
    else:
        lines.append("- _No constraints found_")

    return "\n".join(lines) + "\n"


def safe_folder_name(t: str) -> str:
    """Create a safe folder name from arbitrary title."""
    return re.sub(r'[<>:"/\\|?*]', "", t).strip()

import re
from pathlib import Path
from typing import List, Sequence, Tuple


def extract_python_param_names(code: str) -> List[str]:
    """Extract parameter names from Python starter code (class Solution)."""
    params_found: List[str] = []

    matches = re.findall(r"def\s+\w+\s*\(([^)]*)\)\s*:", code)
    for param_str in matches:
        if "self" not in param_str:
            continue
        parts = [p.strip() for p in param_str.split(",") if p.strip()]
        names: List[str] = []
        for p in parts:
            if p == "self":
                continue
            p = p.split(":", 1)[0].strip()
            p = p.split("=", 1)[0].strip()
            if p:
                names.append(p)
        if names:
            params_found = names
            break

    return params_found


def split_top_level_args(s: str) -> List[str]:
    """Split an argument string on commas that are not inside brackets.

    Example:
      'n = 2, queries = [[0,0,1,1]]'
      -> ['n = 2', 'queries = [[0,0,1,1]]']
    """
    parts: List[str] = []
    buf: List[str] = []
    depth = 0
    opening = {'(': ')', '[': ']', '{': '}'}
    closing = {')', ']', '}'}

    for ch in s:
        if ch in opening:
            depth += 1
        elif ch in closing and depth > 0:
            depth -= 1

        if ch == ',' and depth == 0:
            part = ''.join(buf).strip()
            if part:
                parts.append(part)
            buf = []
        else:
            buf.append(ch)

    if buf:
        part = ''.join(buf).strip()
        if part:
            parts.append(part)

    return parts


def generate_io_files(
    examples: Sequence[Tuple[str, str]],
    param_names: Sequence[str],
    folder_path: Path,
) -> None:
    """Generate input.txt and output.txt from parsed examples."""
    print(f"[IO] examples={len(examples)}, params={list(param_names)}")

    inputs_per_example: List[List[str]] = []
    outputs: List[str] = []

    for _, body in examples:
        if not body:
            continue
        text = body.strip()
        if not text:
            continue

        # Try multiline 'Input:' / 'Output:'
        m_in = re.search(
            r"^Input:\s*(.+)$", text,
            flags=re.IGNORECASE | re.MULTILINE
        )
        m_out = re.search(
            r"^Output:\s*(.+)$", text,
            flags=re.IGNORECASE | re.MULTILINE
        )

        if m_in and m_out:
            raw_in = m_in.group(1).strip()
            raw_out = m_out.group(1).strip()
        else:
            # Fallback: "Input: ... Output: ..." inline
            m_both = re.search(
                r"Input:\s*(.+?)\s+Output:\s*(.+?)(?:\s|$)",
                text,
                flags=re.IGNORECASE | re.DOTALL,
            )
            if not m_both:
                continue
            raw_in = m_both.group(1).strip()
            raw_out = m_both.group(2).strip().splitlines()[0]

        # Default: whole raw_in as a single value
        values: List[str] = [raw_in]

        if param_names:
            arg_chunks = split_top_level_args(raw_in)
            mapping = {}

            for chunk in arg_chunks:
                for p in param_names:
                    m_val = re.search(
                        rf"\b{re.escape(p)}\s*=\s*(.+)",
                        chunk,
                    )
                    if m_val and p not in mapping:
                        mapping[p] = m_val.group(1).strip()

            if mapping:
                values = [mapping[p] for p in param_names if p in mapping]

        inputs_per_example.append(values)
        outputs.append(raw_out)

    # Always write files so user can inspect them
    input_path = folder_path / "input.txt"
    output_path = folder_path / "output.txt"

    with input_path.open("w", encoding="utf-8") as f:
        f.write(str(len(inputs_per_example)) + "\n")
        for vals in inputs_per_example:
            for v in vals:
                f.write(v + "\n")

    with output_path.open("w", encoding="utf-8") as f:
        for i, v in enumerate(outputs):
            if i > 0:
                f.write("\n")
            f.write(v)

    print(
        f"[IO] Wrote {len(inputs_per_example)} example(s) to "
        f"{input_path} and {output_path}"
    )

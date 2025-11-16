import json
import re
from pathlib import Path
from typing import List, Tuple


def _extract_method_name_from_code(code: str) -> str:
    """Get the first method name of class Solution (def xxx(self, ...))."""
    m = re.search(r"def\s+(\w+)\s*\(\s*self\b", code)
    if m:
        return m.group(1)
    # Fallback name (should rarely happen)
    return "mainFunction"


def _read_io_files(folder_path: Path, param_names: List[str]) -> Tuple[List[List[str]], List[str]]:
    """Read input.txt / output.txt and map them to python literals per example.

    input.txt format (created by generate_io_files):
        first line: number of examples (N)
        then, for each example:
            one line per parameter (in param_names order)

    output.txt:
        one line per expected output (string is valid Python literal).
    """
    input_path = folder_path / "input.txt"
    output_path = folder_path / "output.txt"

    if not input_path.exists() or not output_path.exists():
        print("[NB] input.txt or output.txt not found, skip notebook")
        return [], []

    # Read inputs
    with input_path.open("r", encoding="utf-8") as f:
        raw_lines = [line.rstrip("\n") for line in f]

    if not raw_lines:
        return [], []

    try:
        num_cases = int(raw_lines[0].strip())
    except ValueError:
        print("[NB] First line of input.txt is not an integer, skip notebook")
        return [], []

    idx = 1
    inputs: List[List[str]] = []
    for _ in range(num_cases):
        vals: List[str] = []
        for _ in range(len(param_names)):
            if idx >= len(raw_lines):
                break
            vals.append(raw_lines[idx].strip())
            idx += 1
        if len(vals) != len(param_names):
            break
        inputs.append(vals)

    # Read outputs
    with output_path.open("r", encoding="utf-8") as f:
        outputs = [line.rstrip("\n") for line in f if line.strip() != ""]

    m = min(len(inputs), len(outputs))
    if m == 0:
        print("[NB] No matching input/output pairs, skip notebook")
        return [], []
    return inputs[:m], outputs[:m]


def _build_notebook_dict(
    class_code: str,
    method_name: str,
    param_names: List[str],
    inputs: List[List[str]],
    outputs: List[str],
) -> dict:
    """Build a minimal Jupyter notebook structure as a Python dict."""

    # -------- SOLUTION cell (code) --------
    solution_source = [line + "\n" for line in class_code.rstrip("\n").splitlines()]

    # -------- TESTCASES cell (code) --------
    arg_names = [f"input_{p}" for p in param_names]          # e.g. input_n, input_queries
    signature_params = ", ".join(["case_number"] + arg_names + ["expected"])
    call_args = ", ".join(arg_names)

    test_lines: List[str] = []
    test_lines.append("solution = Solution()\n")
    test_lines.append("\n")
    test_lines.append("# def extraCondition(result, expected):\n")
    test_lines.append("#     pass\n")
    test_lines.append("\n\n")
    test_lines.append(f"def run_test_case({signature_params}):\n")
    test_lines.append(f"    result = solution.{method_name}({call_args})\n")
    test_lines.append('    status = "PASSED" if result == expected else "FAILED"\n')
    test_lines.append(
        '    # status = "PASSED" if extraCondition(result, expected) else "FAILED"\n'
    )

    label_str = ", ".join(param_names)         # e.g. "n, queries"
    display_vars = ", ".join(arg_names)       # e.g. "input_n, input_queries"

    test_lines.append(
        '    print('
        'f"Case {case_number} - ('
        + label_str
        + '): {('
        + display_vars
        + ')}, Output: {result}, Expected: {expected}, Status: {status}")\n'
    )
    test_lines.append("\n")
    test_lines.append("test_cases = [\n")
    for i, (vals, out) in enumerate(zip(inputs, outputs), 1):
        # vals and out are already Python-literal strings
        args_str = ", ".join(vals + [out])
        test_lines.append(f"    ({i}, {args_str}),\n")
    test_lines.append("]\n")
    test_lines.append("\n")

    destructuring = ", ".join(["case_number"] + arg_names + ["expected"])
    test_lines.append(f"for {destructuring} in test_cases:\n")
    test_lines.append(f"    run_test_case({destructuring})\n")

    nb = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# **SOLUTION**"],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": solution_source,
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# **DRAFT**"],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# **TESTCASES**"],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": test_lines,
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "python3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.10",
                "mimetype": "text/x-python",
                "codemirror_mode": {"name": "ipython", "version": 3},
                "pygments_lexer": "ipython3",
                "file_extension": ".py",
                "nbconvert_exporter": "python",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 2,
    }
    return nb


def generate_notebook(
    folder_path: Path,
    python_code: str,
    param_names: List[str],
    cleanup_io: bool = False,
) -> None:
    """Create solution.ipynb in folder_path using python_code + IO files.

    If cleanup_io is True, input.txt and output.txt will be removed
    after the notebook has been generated successfully.
    """
    inputs, outputs = _read_io_files(folder_path, param_names)
    if not inputs or not outputs:
        return

    method_name = _extract_method_name_from_code(python_code)
    nb_dict = _build_notebook_dict(python_code, method_name, param_names, inputs, outputs)
    out_path = folder_path / "solution.ipynb"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(nb_dict, f, indent=1)
    print(f"[NB] Wrote notebook {out_path}")

    # Optionally remove IO files once they have been used
    if cleanup_io:
        for name in ("input.txt", "output.txt"):
            try:
                (folder_path / name).unlink()
                print(f"[NB] Removed {name} after generating notebook")
            except FileNotFoundError:
                pass

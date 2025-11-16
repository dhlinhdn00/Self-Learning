# cfGenerator.py
from pathlib import Path
from typing import List

# Names that are very likely plain integers in typical CP/LC problems
_INTY_NAMES = {"n", "m", "k", "len", "length", "size"}


def _generate_python_line_solution(folder_path: Path, param_names: List[str]) -> None:
    """
    Generate a line-based Python solution.py.

    Assumes input.txt has the following structure:

        t
        <param1_case1>
        <param2_case1>
        ...
        <paramK_case1>
        <param1_case2>
        ...

    Each parameter is stored on its own line.
    """
    out_path = folder_path / "solution.py"

    if not param_names:
        param_names = ["x"]

    raw_vars = [f"raw_{p}" for p in param_names]

    lines: List[str] = []
    lines.append("import sys")
    lines.append("")
    lines.append("")
    lines.append("def solve():")
    lines.append("    # Read all lines from stdin (same layout as input.txt)")
    lines.append("    lines = sys.stdin.read().rstrip('\\n').splitlines()")
    lines.append("    it = iter(lines)")
    lines.append("    t = int(next(it))  # number of test cases")
    lines.append("    out_lines = []")
    lines.append("")
    lines.append("    for _ in range(t):")

    for raw in raw_vars:
        lines.append(f"        {raw} = next(it)  # one line from input.txt")

    lines.append("")
    lines.append("        # TODO: parse raw inputs into proper Python values")
    lines.append("        # Example:")
    lines.append("        # import ast")
    for p, raw in zip(param_names, raw_vars):
        if p in _INTY_NAMES:
            lines.append(f"        # {p} = int({raw})")
        else:
            lines.append(f"        # {p} = ast.literal_eval({raw})  # list / matrix / etc.")
    lines.append("")
    lines.append("        # TODO: compute answer for this test case")
    lines.append("        ans = None")
    lines.append("")
    lines.append("        out_lines.append(str(ans))")
    lines.append("")
    lines.append("    sys.stdout.write('\\n'.join(out_lines))")
    lines.append("")
    lines.append("")
    lines.append("if __name__ == '__main__':")
    lines.append("    solve()")
    lines.append("")
    lines.append("# Run with:")
    lines.append("#   python solution.py < input.txt")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[CF] Wrote line-based Python CF-style solution template to {out_path}")


def _generate_python_token_solution(folder_path: Path, param_names: List[str]) -> None:
    """
    Generate a token-based Python solution.py (classic Codeforces style):

        data = sys.stdin.read().strip().split()
        it = iter(data)
        t = int(next(it))
        ...

    Note: if the logical input contains lists/matrices with spaces or commas,
    you will need to handle parsing carefully.
    """
    out_path = folder_path / "solution.py"

    if not param_names:
        param_names = ["x"]

    raw_vars = [f"raw_{p}" for p in param_names]

    lines: List[str] = []
    lines.append("import sys")
    lines.append("")
    lines.append("")
    lines.append("def solve():")
    lines.append("    data = sys.stdin.read().strip().split()")
    lines.append("    it = iter(data)")
    lines.append("    t = int(next(it))  # number of test cases")
    lines.append("    out_lines = []")
    lines.append("")
    lines.append("    for _ in range(t):")

    for raw in raw_vars:
        lines.append(f"        {raw} = next(it)  # raw token for parameter")

    lines.append("")
    lines.append("        # TODO: parse raw tokens into proper Python values")
    lines.append("        # Example:")
    lines.append("        # import ast")
    for p, raw in zip(param_names, raw_vars):
        if p in _INTY_NAMES:
            lines.append(f"        # {p} = int({raw})")
        else:
            lines.append(f"        # {p} = ast.literal_eval({raw})  # if it encodes a list/matrix")
    lines.append("")
    lines.append("        # TODO: compute answer for this test case")
    lines.append("        ans = None")
    lines.append("")
    lines.append("        out_lines.append(str(ans))")
    lines.append("")
    lines.append("    sys.stdout.write('\\n'.join(out_lines))")
    lines.append("")
    lines.append("")
    lines.append("if __name__ == '__main__':")
    lines.append("    solve()")
    lines.append("")
    lines.append("# Run with:")
    lines.append("#   python solution.py < input.txt")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[CF] Wrote token-based Python CF-style solution template to {out_path}")


def _generate_cpp_solution(folder_path: Path, param_names: List[str]) -> None:
    """
    Generate a C++ Codeforces-style solution.cpp.

    Uses standard token-based input via `cin >>`.
    """
    out_path = folder_path / "solution.cpp"

    if not param_names:
        param_names = ["x"]

    lines: List[str] = []
    lines.append("#include <bits/stdc++.h>")
    lines.append("using namespace std;")
    lines.append("")
    lines.append("int main() {")
    lines.append("    ios::sync_with_stdio(false);")
    lines.append("    cin.tie(nullptr);")
    lines.append("")
    lines.append("    int t;")
    lines.append("    if (!(cin >> t)) return 0;")
    lines.append("")
    lines.append("    while (t--) {")
    lines.append("")

    for p in param_names:
        if p in _INTY_NAMES:
            lines.append(f"        long long {p};")
            lines.append(f"        cin >> {p};")
        else:
            lines.append(f"        string raw_{p};")
            lines.append(f"        cin >> raw_{p};  // TODO: parse into proper type for `{p}`")
    lines.append("")
    lines.append("        long long ans = 0;  // TODO: compute answer")
    lines.append("")
    lines.append("        cout << ans << '\\n';")
    lines.append("    }")
    lines.append("")
    lines.append("    return 0;")
    lines.append("}")
    lines.append("// g++ -std=c++17 -O2 -Wall solution.cpp -o solution")
    lines.append("// ./solution < input.txt")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[CF] Wrote C++ CF-style solution template to {out_path}")


def generate_cf_solution(folder_path: Path, param_names: List[str], lang: str, io_style: str) -> None:
    """
    Public entry point to generate a Codeforces-style template.

    :param folder_path: Where to save the solution file.
    :param param_names: Parameter names inferred from the Python starter.
    :param lang: 'python' or 'cpp'.
    :param io_style: For Python, 'line' (per-line input) or 'token' (split() style).
                     For C++, this is ignored (always token-based).
    """
    lang = (lang or "python").lower()
    io_style = (io_style or "line").lower()

    if lang in ("py", "python"):
        if io_style == "token":
            _generate_python_token_solution(folder_path, param_names)
        else:
            _generate_python_line_solution(folder_path, param_names)
    elif lang in ("cpp", "c++"):
        _generate_cpp_solution(folder_path, param_names)
    else:
        print(f"[CF] Unknown language for --cf: {lang}, supported: python / cpp")

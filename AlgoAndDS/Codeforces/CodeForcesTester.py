# CodeForcesTester.py
from io import StringIO
from contextlib import redirect_stdout
import difflib
import builtins

def run_case(inp: str, solver) -> str:
    """Chạy solver() với input dạng string, trả về output string."""
    inp = inp.replace('\r\n', '\n').replace('\r', '\n')
    old_input = builtins.input

    def _input():
        return _stdin.readline().rstrip('\n')

    _stdin = StringIO(inp)
    output_buf = StringIO()

    try:
        builtins.input = _input  # monkey-patch input toàn cục
        with redirect_stdout(output_buf):
            solver()
    finally:
        builtins.input = old_input  # khôi phục

    return output_buf.getvalue()

def _split_norm(s: str):
    return [line.rstrip() for line in s.strip('\n').split('\n') if line != ''] if s.strip() else []

def check(inp: str, expected: str, solver, *, show_diff: bool = True):
    """So sánh output solver với expected."""
    got = run_case(inp, solver)
    got_lines = _split_norm(got)
    exp_lines = _split_norm(expected)
    ok = got_lines == exp_lines
    status = "PASS" if ok else "FAILED"
    print(status)
    print("---- Input ----")
    print(inp.strip() if inp.strip() else "(empty)")
    print("---- Output (got) ----")
    print("\n".join(got_lines) if got_lines else "(empty)")
    print("---- Expected ----")
    print("\n".join(exp_lines) if exp_lines else "(empty)")
    if not ok and show_diff:
        print("---- Diff (got vs expected) ----")
        diff = difflib.ndiff(got_lines, exp_lines)
        print("\n".join(diff))
    return ok

def check_many(cases, solver):
    """
    cases = [
        (input_str, expected_output_str),
        ...
    ]
    """
    passed = 0
    for idx, (inp, exp) in enumerate(cases, 1):
        print(f"\n=== Case #{idx} ===")
        if check(inp, exp, solver):
            passed += 1
    print(f"\nSummary: {passed}/{len(cases)} passed")
    return passed

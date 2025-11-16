#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

import requests

from lcClient import fetch_question, fetch_starter_code, extract_slug
from parserHTML import html_to_text_blocks, extract_sample_codes
from readmeBuilder import build_readme, safe_folder_name
from pdfExport import description_to_pdf
from ioExamples import extract_python_param_names, generate_io_files
from nbGenerator import generate_notebook
from cfGenerator import generate_cf_solution


def write_readme_for_link(
    session: requests.Session,
    link: str,
    base_out_dir: Path | None = None,
    out_file: Path | None = None,
    ensure_dir: bool = True,
    outputs: list[str] | None = None,
    solutions: list[str] | None = None,
) -> Path:
    """
    Fetch problem data and generate artifacts based on flags:

      outputs:
        - "input-output"    -> input.txt, output.txt
        - "readme-md"       -> README.md
        - "readme-pdf"      -> README.pdf
        - "starter:<lang>"  -> starter_code/starter_<lang>.txt

      solutions:
        - "nb"              -> solution.ipynb
        - "cf-python-line"  -> Codeforces-style solution.py (line-based IO)
        - "cf-python-token" -> Codeforces-style solution.py (token-based IO)
        - "cf-cpp-line"     -> Codeforces-style solution.cpp (token-based IO)
        - "cf-cpp-token"    -> Codeforces-style solution.cpp (token-based IO)

    Default behavior (no --outputs and no --solutions):
      - outputs   = ["readme-pdf"]
      - solutions = ["nb"]

    IO files (input.txt, output.txt) are generated only if:
      - 'input-output' is explicitly requested in outputs, or
      - a solution mode that relies on IO is enabled (nb, cf-*)
    """
    outputs = outputs or []
    solutions = solutions or []

    # Default behavior: README PDF + notebook (no IO by default)
    if not outputs and not solutions:
        outputs = ["readme-pdf"]
        solutions = ["nb"]

    # Base output dir
    if base_out_dir is None:
        base_out_dir = Path("Draft")

    # Parse output options
    output_set = set(outputs)
    want_md = "readme-md" in output_set
    want_pdf = "readme-pdf" in output_set
    want_io_explicit = "input-output" in output_set

    # Starter languages requested via "starter:<lang>"
    starter_langs: set[str] = set()
    for item in outputs:
        if item.startswith("starter:"):
            _, lang = item.split(":", 1)
            if lang:
                starter_langs.add(lang.lower())

    # Parse solution options
    solution_set = set(solutions)
    want_nb = "nb" in solution_set
    want_cf_py_line = "cf-python-line" in solution_set
    want_cf_py_token = "cf-python-token" in solution_set
    want_cf_cpp_line = "cf-cpp-line" in solution_set
    want_cf_cpp_token = "cf-cpp-token" in solution_set
    want_cf_cpp = want_cf_cpp_line or want_cf_cpp_token

    # Any solution type that needs IO?
    uses_io = want_nb or want_cf_py_line or want_cf_py_token or want_cf_cpp
    # We only generate IO if explicitly requested OR required by solutions
    want_io = want_io_explicit or uses_io

    # Fetch problem metadata and HTML
    q = fetch_question(session, link)

    content_html = q.get("content") or ""
    desc, examples, constraints = html_to_text_blocks(content_html)
    print(f"[DEBUG] Parsed {len(examples)} example(s)")

    title = q.get("title", "Problem")
    index = q.get("questionFrontendId", "N/A")
    difficulty = q.get("difficulty", "Unknown")

    folder_name = safe_folder_name(title)
    folder_path = base_out_dir / folder_name
    if ensure_dir:
        folder_path.mkdir(parents=True, exist_ok=True)

    # README.md
    if want_md:
        md_file = out_file if out_file else folder_path / "README.md"
        md_file.write_text(
            build_readme(index, title, difficulty, link, desc, examples, constraints),
            encoding="utf-8",
        )

    # README.pdf
    if want_pdf:
        pdf_path = folder_path / "README.pdf"
        description_to_pdf(content_html, pdf_path, title, index, difficulty, link)

    # sample_code.txt from problem description
    sample_codes = extract_sample_codes(content_html)
    if sample_codes:
        sample_file = folder_path / "sample_code.txt"
        sample_file.write_text(
            "\n\n".join(sample_codes),
            encoding="utf-8",
        )

    # Starter code + param names (used for IO, notebook, CF templates)
    param_names: list[str] = []
    python_code_for_nb: str | None = None

    need_starter = (
        bool(starter_langs)
        or want_nb
        or want_cf_py_line
        or want_cf_py_token
        or want_cf_cpp
    )

    if need_starter:
        slug = extract_slug(link)
        referer_url = f"https://leetcode.com/problems/{slug}/description/"
        starter_snippets = fetch_starter_code(session, slug, referer_url)

        selected_snippets = []

        for snip in starter_snippets or []:
            lang_slug = (snip.get("langSlug") or "").lower()
            lang_name = (snip.get("lang") or "").lower()

            # Save requested starter:<lang> to starter_code/
            if starter_langs and any(
                lang in (lang_slug, lang_name) for lang in starter_langs
            ):
                selected_snippets.append(snip)

            # Remember Python starter for IO + notebook + CF
            if lang_slug == "python" and python_code_for_nb is None:
                python_code_for_nb = snip["code"]

        if selected_snippets:
            starter_dir = folder_path / "starter_code"
            starter_dir.mkdir(exist_ok=True)

            for snip in selected_snippets:
                lang_slug = snip["langSlug"]
                code = snip["code"]
                file_path = starter_dir / f"starter_{lang_slug}.txt"
                file_path.write_text(code, encoding="utf-8")

        if python_code_for_nb:
            param_names = extract_python_param_names(python_code_for_nb)

    # input.txt / output.txt (only when requested or required by solutions)
    if want_io:
        generate_io_files(examples, param_names, folder_path)

    # Decide whether notebook should clean up IO files afterwards
    # - If IO was only generated because nb/cf-* needed it (NOT explicitly requested),
    #   then we can safely remove input.txt/output.txt after building the notebook.
    cleanup_io_after_nb = want_io and not want_io_explicit

    # solution.ipynb
    if want_nb and python_code_for_nb and param_names:
        generate_notebook(
            folder_path,
            python_code_for_nb,
            param_names,
            cleanup_io=cleanup_io_after_nb,
        )
    elif want_nb and (not python_code_for_nb or not param_names):
        print("[NB] Missing Python starter or parameter names, cannot create notebook")

    # Codeforces-style solutions
    if want_cf_py_line:
        generate_cf_solution(folder_path, param_names, lang="python", io_style="line")

    if want_cf_py_token:
        generate_cf_solution(folder_path, param_names, lang="python", io_style="token")

    if want_cf_cpp:
        # C++ template is token-based; cf-cpp-line and cf-cpp-token
        # are generated the same way for now.
        generate_cf_solution(folder_path, param_names, lang="cpp", io_style="token")

    return folder_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Generate PDF / README / IO / starter / notebook / CF templates "
            "from LeetCode problem link(s)."
        ),
    )
    parser.add_argument("links", nargs="+", help="LeetCode problem links")

    parser.add_argument(
        "--out-dir",
        default="Draft",
        help=(
            "Base output directory. Problem folders will be created inside this "
            "directory. Default: Draft"
        ),
    )

    parser.add_argument(
        "--outputs",
        nargs="+",
        metavar="OUT",
        help=(
            "Outputs to generate (can be multiple): "
            "input-output, readme-md, readme-pdf, starter:<LANG>. "
            "If omitted (and no --solutions), defaults to: readme-pdf."
        ),
    )

    parser.add_argument(
        "--solutions",
        nargs="+",
        metavar="SOL",
        help=(
            "Sample solutions to generate (can be multiple): "
            "nb, cf-python-line, cf-python-token, cf-cpp-line, cf-cpp-token. "
            "If both --outputs and --solutions are omitted, defaults to: nb."
        ),
    )

    parser.add_argument(
        "--readme-out",
        help=(
            "Output path for README.md (only valid when 'readme-md' is in "
            "--outputs and a single link is provided)."
        ),
    )

    args = parser.parse_args()

    outputs = args.outputs or []
    solutions = args.solutions or []

    # Validate --readme-out
    if args.readme_out:
        if "readme-md" not in (outputs or []):
            print("Error: --readme-out requires 'readme-md' in --outputs.", file=sys.stderr)
            sys.exit(2)
        if len(args.links) > 1:
            print("Error: --readme-out cannot be used with multiple links.", file=sys.stderr)
            sys.exit(2)

    base_out_dir = Path(args.out_dir)
    base_out_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    generated: list[Path] = []

    for link in args.links:
        out_file = Path(args.readme_out) if args.readme_out else None

        folder = write_readme_for_link(
            session=session,
            link=link,
            base_out_dir=base_out_dir,
            out_file=out_file,
            ensure_dir=True,
            outputs=outputs,
            solutions=solutions,
        )
        generated.append(folder)

    print("\nCreated:")
    for p in generated:
        print(" -", p.resolve())


if __name__ == "__main__":
    main()

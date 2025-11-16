# Self-Learning Playground

This repository is my personal playground for algorithms, competitive programming, AI experiments, and tooling around online judges (LeetCode / Codeforces).

The most notable utility is **`LCFetcher`**, a small CLI tool that can:
- Fetch a LeetCode problem by URL
- Generate a clean PDF / Markdown statement
- Build `input.txt` / `output.txt` from examples
- Create a ready–to–use `solution.ipynb` notebook
- Generate Codeforces-style solution templates (`solution.py` / `solution.cpp`)

---

## Folder Structure

High-level layout (only the important parts):

```text
.
├─ AI/                     # AI / ML experiments (not detailed here)
├─ Discussion/             # Notes, rough drafts, misc discussions
├─ Draft/
├─ DSA/
│   ├─ _Algorithm/         # Algorithm implementations / practice
│   ├─ _DataStructures/    # Custom data structures used across problems
│   ├─ CodeForces/
│   │   └─ Contests/       # CF contest solutions
│   └─ LeetCode/
│       ├─ Contests/       # LC contest submissions
│       └─ Practices/      # Regular LC practice solutions
├─ Tools/
│   └─ LCFetcher/          # The LeetCode fetching & generation tool
│       ├─ main.py         # CLI entry point (wired to `LCFetcher` console script)
│       ├─ lcClient.py     # HTTP / GraphQL client for LeetCode
│       ├─ parserHTML.py   # HTML → text / examples / constraints parser
│       ├─ readmeBuilder.py# Markdown README generator
│       ├─ pdfExport.py    # WeasyPrint-based PDF export
│       ├─ ioExamples.py   # input.txt / output.txt generation from examples
│       ├─ nbGenerator.py  # solution.ipynb generator + test harness
│       ├─ cfGenerator.py  # Codeforces-style solution templates
│       ├─ pyproject.toml  # Package metadata for LCFetcher
│       └─ ...
├─ README.md               # This file
└─ requirements.txt        # Project-wide Python dependencies
```

`Draft/` is safe to delete at any time – it only contains generated artifacts.  
`Tools/LCFetcher` behaves like a small installable package inside this repo.

---

## 1. Python Environment Setup

Recommended flow (for a fresh machine):

```bash
# 1. Create and activate a virtualenv / conda env
conda create -n self-learning-env python=3.10 -y
conda activate self-learning-env

# 2. Install project dependencies
pip install -r requirements.txt
```

If you don’t want to use conda, use `python -m venv venv` + `source venv/bin/activate` instead.

---

## 2. Installing the LCFetcher CLI

`LCFetcher` is packaged via `pyproject.toml` inside `Tools/LCFetcher`, and exposes a console script named `LCFetcher`.

From the **repo root**:

```bash
# In the activated environment
pip install -e Tools/LCFetcher
```

- `-e` = editable install (any change inside `Tools/LCFetcher` is picked up immediately).
- This will install the `LCFetcher` command into your environment’s `bin` folder.

Verify the CLI is available:

```bash
LCFetcher --help
```

You should see the help message instead of “command not found”.

---

## 3. Using LCFetcher

Basic usage (from repo root, or anywhere if env is active):

```bash
LCFetcher "https://leetcode.com/problems/number-of-substrings-with-only-1s/description/"
```

### 3.1 Default behavior

If you don’t pass any flags:

- Output base directory: `Draft/`
- Generated artifacts:
  - `Draft/<Problem Title>/README.pdf`
  - `Draft/<Problem Title>/solution.ipynb`

No `input.txt` / `output.txt` is generated unless a mode that needs IO is enabled.

---

### 3.2 Output options (`--outputs`)

You can control which “static” artifacts to produce:

```bash
LCFetcher <URL>   --outputs readme-pdf readme-md input-output starter:python starter:cpp
```

Supported `--outputs` values:

- `readme-pdf`  
  → `README.pdf` (WeasyPrint, A4 landscape, wrapped code blocks)
- `readme-md`  
  → `README.md` (Markdown version of the statement)
- `input-output`  
  → `input.txt` / `output.txt` from parsed examples
- `starter:<LANG>`  
  → Save LeetCode editor “starter code” to `starter_code/starter_<LANG>.txt`  
    Example: `starter:python`, `starter:cpp`, `starter:java`, etc.

If **both** `--outputs` and `--solutions` are omitted, the default is:

```text
outputs   = ["readme-pdf"]
solutions = ["nb"]
```

---

### 3.3 Solution templates (`--solutions`)

This controls generated “runnable” solution templates:

```bash
LCFetcher <URL>   --outputs input-output   --solutions nb cf-python-line cf-cpp-token
```

Supported values:

- `nb`  
  → `solution.ipynb`  

  Uses:
  - The Python starter code from LeetCode.
  - `input.txt` / `output.txt` to auto-generate test cases.

- `cf-python-line`  
  → `solution.py` (Codeforces-style, **line-based IO**):
  - Reads `t` test cases.
  - For each case, reads one line and splits it into Python literals matching the parameter list.

- `cf-python-token`  
  → `solution.py` (Codeforces-style, classic **token-based IO**):
  - Uses `data = sys.stdin.read().strip().split()`, `it = iter(data)` style.

- `cf-cpp-line` / `cf-cpp-token`  
  → `solution.cpp` (currently both mapped to the same **token-based** `cin >>` template):
  - Reads `t`, then parameters for each test in competitive-programming style.

> Any `cf-*` or `nb` mode implies that IO is needed.  
> If `input-output` is not specified in `--outputs`, `LCFetcher` will still generate `input.txt` / `output.txt` automatically for those modes.

---

### 3.4 Output directory (`--out-dir`)

Change where generated folders live:

```bash
LCFetcher <URL> --out-dir Draft/LeetCode
```

This will create:

```text
Draft/LeetCode/<Problem Title>/
    README.pdf
    solution.ipynb
    ...
```

Default is simply `Draft/`.

---

### 3.5 Custom README path (`--readme-out`)

If you want a single `README.md` somewhere else:

```bash
LCFetcher <URL>   --outputs readme-md   --readme-out DSA/LeetCode/Practices/<some-folder>/README.md
```

Constraints:

- `readme-md` must be present in `--outputs`.
- Only valid when a **single** problem URL is given.

---

## 4. Generating a Clean `requirements.txt` for the Repo

This project contains multiple submodules and notebooks.  
To regenerate a `requirements.txt` based on imports in `.py` files, we use **pipreqs**:

### 4.1 Install pipreqs (once)

```bash
pip install pipreqs
```

### 4.2 Generate `requirements.txt` from the repo root

From the repository root:

```bash
pipreqs . --force
```

`pipreqs` will:

- Scan all `.py` files.
- Infer external dependencies.
- Overwrite `requirements.txt` (because of `--force`).

Notes:

- It does **not** scan Jupyter notebooks (`.ipynb`).  
  If some libraries are used **only inside notebooks**, add them manually to `requirements.txt`.
- Sometimes it might mis-detect internal modules as external packages (e.g. mapping `_DataStructures` to `datastructures`).  
  Always quickly review the generated `requirements.txt` and remove any suspicious entries.

---

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
├─ AI/
├─ Discussion/
├─ Draft/
├─ DSA/
│   ├─ _Algorithm/
│   ├─ _DataStructures/
│   ├─ CodeForces/
│   │   └─ Contests/
│   └─ LeetCode/
│       ├─ Contests/
│       └─ Practices/
├─ Tools/
│   └─ LCFetcher/
│       ├─ main.py
│       ├─ lcClient.py
│       ├─ parserHTML.py
│       ├─ readmeBuilder.py
│       ├─ pdfExport.py
│       ├─ ioExamples.py
│       ├─ nbGenerator.py
│       ├─ cfGenerator.py
│       ├─ pyproject.toml
│       └─ ...
├─ README.md
└─ requirements.txt
```

---

## 1. Python Environment Setup

```bash
conda create -n selfLearningEnv python=3.10 -y
conda activate selfLearningEnv
pip install -r requirements.txt
```

---

## 2. Installing the LCFetcher CLI

If you are using **Windows** or **macOS**, **WeasyPrint** must be installed via `conda-forge` before installing LCFetcher.
Installing **WeasyPrint** with `pip` alone may lead to runtime errors due to missing native dependencies:

```bash
pip uninstall -y weasyprint
conda install -c conda-forge weasyprint
conda install -c conda-forge glib pango cairo gdk-pixbuf libffi fontconfig
```

Then, installing **`LCFetcher`**:

```bash
pip install -e Tools/LCFetcher
```

Check:

```bash
LCFetcher --help
```

---

## 3. Using LCFetcher

Basic usage:

```bash
LCFetcher "<LeetCode URL>"
```

Default behaviors:
- Creates directory under `Draft/<Problem Title>/`
- Generates:
  - `README.pdf`
  - `solution.ipynb`

---

### 3.1 Output options (`--outputs`)

```bash
LCFetcher <URL> --outputs readme-pdf readme-md input-output starter:python starter:cpp
```

Available output modes:

- **readme-pdf**  
- **readme-md**  
- **input-output**  
- **starter:<LANG>**

Defaults when nothing specified:

```
outputs   = ["readme-pdf"]
solutions = ["nb"]
```

---

### 3.2 Solution templates (`--solutions`)

```bash
LCFetcher <URL> --solutions nb cf-python-line cf-cpp-token
```

Supported:

- nb  
- cf-python-line  
- cf-python-token  
- cf-cpp-line  
- cf-cpp-token  

Any CF/Notebook mode implies IO is needed;  
input/output files are auto-generated.

---

### 3.3 Output directory (`--out-dir`)

```bash
LCFetcher <URL> --out-dir Draft/LeetCode
```

Produces:

```
Draft/LeetCode/<Problem Title>/
```

---

### 3.4 Custom README path (`--readme-out`)

```bash
LCFetcher <URL> --outputs readme-md \
    --readme-out DSA/LeetCode/Practices/<folder>/README.md
```

Constraints:
- must include `readme-md`
- only valid for single URL

---

## 4. Generating Requirements

Install pipreqs:

```bash
pip install pipreqs
```

Generate:

```bash
pipreqs . --force
```

Notes:

- It does **not** scan Jupyter notebooks (`.ipynb`).  
  If some libraries are used **only inside notebooks**, add them manually to `requirements.txt`.
- Sometimes it might mis-detect internal modules as external packages (e.g. mapping `_DataStructures` to `datastructures`).  
  Always quickly review the generated `requirements.txt` and remove any suspicious entries.

---

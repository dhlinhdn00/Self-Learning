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

```bash
pip install -e Tools/LCFetcher
```

Check:

```bash
LCFetcher --help
```

---

# 2.1 Windows Setup for WeasyPrint (PDF Export)

`LCFetcher` uses **WeasyPrint** for generating `README.pdf`.  
On Windows, WeasyPrint needs several native Linux-style graphic libraries.  
MSYS2 + MINGW64 provides them.

Follow the steps below.

---

## **Step 1 — Install WeasyPrint (Python package)**

```bash
pip install weasyprint
```

---

## **Step 2 — Install MSYS2**

Download MSYS2:  
https://www.msys2.org/

Open **MSYS2 MSYS** and update packages:

```bash
pacman -Syu
```

Restart the terminal if prompted, then update again:

```bash
pacman -Syu
```

---

## **Step 3 — Install the MinGW64 toolchain**

Inside **MSYS2 MSYS**:

```bash
pacman -S mingw-w64-x86_64-toolchain
```

Press **Enter** to install the entire group (recommended).

This provides the 64-bit MinGW runtime needed for WeasyPrint.

---

## **Step 4 — Install GTK, Cairo, Pango, GObject libraries**

Still inside MSYS2:

```bash
pacman -S \
    mingw-w64-x86_64-gtk3 \
    mingw-w64-x86_64-pango \
    mingw-w64-x86_64-cairo \
    mingw-w64-x86_64-gobject-introspection \
    mingw-w64-x86_64-harfbuzz \
    mingw-w64-x86_64-libffi
```

These libraries will be installed into:

```
C:\msys64\mingw64\bin
```

WeasyPrint will dynamically load DLLs from this folder.

---

## **Step 5 — Add DLL directory to your Conda environment PATH**

Open **Anaconda Prompt**:

```bash
conda activate selfLearningEnv
mkdir %CONDA_PREFIX%\etc\conda\activate.d
notepad %CONDA_PREFIX%\etc\conda\activate.d\env_vars.bat
```

Paste the following line into the opened file:

```
set "PATH=C:\msys64\mingw64\bin;%PATH%"
```

Save the file.

Restart your environment:

```bash
conda activate selfLearningEnv
```

---

## **Step 6 — Verify WeasyPrint Loads**

```bash
python -c "from weasyprint import HTML; print('WeasyPrint OK')"
```

If no errors appear, PDF generation is fully enabled on Windows.

---

# 3. Using LCFetcher

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

## 3.1 Output options (`--outputs`)

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

## 3.2 Solution templates (`--solutions`)

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

## 3.3 Output directory (`--out-dir`)

```bash
LCFetcher <URL> --out-dir Draft/LeetCode
```

Produces:

```
Draft/LeetCode/<Problem Title>/
```

---

## 3.4 Custom README path (`--readme-out`)

```bash
LCFetcher <URL> --outputs readme-md \
    --readme-out DSA/LeetCode/Practices/<folder>/README.md
```

Constraints:
- must include `readme-md`
- only valid for single URL

---

# 4. Generating Requirements

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

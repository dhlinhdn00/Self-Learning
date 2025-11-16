from datetime import datetime
from pathlib import Path

from weasyprint import HTML


def description_to_pdf(
    html_content: str,
    pdf_path: Path,
    title: str,
    index: str,
    difficulty: str,
    link: str,
) -> None:
    """Render the original HTML description into a styled PDF."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_doc = f"""
    <html>
    <head>
    <meta charset="utf-8">
    <style>
    /* Make page A4 landscape */
    @page {{
        size: A4 landscape;
        margin: 20mm;
    }}

    body {{
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 15px;
        line-height: 1.55;
        color: #222;
        margin: 0;
        padding: 20px 40px;
    }}
    .header {{
        margin-bottom: 30px;
        padding-bottom: 12px;
        border-bottom: 2px solid #e5e7eb;
    }}
    .title {{
        font-size: 26px;
        font-weight: 700;
        color: #0a3069;
    }}
    .meta {{
        font-size: 14px;
        color: #555;
        margin-bottom: 3px;
    }}
    .problem-label {{
        margin-top: 25px;
        font-size: 20px;
        font-weight: 600;
        color: #0a3069;
    }}

    /* Force wrapping inside leetcode code/IO blocks */
    pre, code {{
        background: #f3f4f6;
        border: 1px solid #e2e4e8;
        padding: 10px;
        border-radius: 6px;
        font-family: "JetBrains Mono", monospace;
        font-size: 13px;
        white-space: pre-wrap !important;
        overflow-wrap: anywhere !important;
        word-break: break-all !important;
    }}

    table {{
        border-collapse: collapse;
        width: 100%;
    }}
    th, td {{
        border: 1px solid #ccc;
        padding: 8px;
    }}
    </style>
    </head>

    <body>

    <div class="header">
        <div class="title">{index}. {title}</div>
        <div class="meta"><b>Difficulty:</b> {difficulty}</div>
        <div class="meta"><b>Link:</b> <a href="{link}">{link}</a></div>
        <div class="meta"><b>Generated at:</b> {now}</div>
    </div>

    <div class="problem-label">Problem:</div>
    {html_content}

    </body>
    </html>
    """

    HTML(string=html_doc).write_pdf(str(pdf_path))

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

import requests
from bs4 import BeautifulSoup

GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    content
  }
}
"""

def extract_slug(url: str) -> str:
    m = re.search(r"/problems/([^/]+)/?", url)
    if not m:
        raise ValueError(f"Slug not found in URL: {url}")
    return m.group(1)

def get_csrf_and_warmup(session: requests.Session, url: str) -> str:
    session.headers.update({
        "User-Agent": "Mozilla/5.0",
        "Referer": url
    })
    session.get(url, timeout=20)
    return session.cookies.get("csrftoken", "")

def fetch_question(session: requests.Session, url: str) -> dict:
    slug = extract_slug(url)
    csrftoken = get_csrf_and_warmup(session, f"https://leetcode.com/problems/{slug}/description/")
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{slug}/description/",
    }
    if csrftoken:
        headers["x-csrftoken"] = csrftoken

    resp = session.post(
        GRAPHQL_URL,
        json={"query": QUERY, "variables": {"titleSlug": slug}},
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    q = (data or {}).get("data", {}).get("question")
    if not q:
        raise RuntimeError(f"Failed to fetch question data for slug: {slug}")
    return q

def html_to_text_blocks(html: str):
    soup = BeautifulSoup(html or "", "html.parser")

    constraints_anchor = None
    for tag in soup.find_all(["p", "strong", "h3", "h4", "span"]):
        txt = tag.get_text(separator=" ", strip=True)
        if re.fullmatch(r"Constraints:?|Constraint:?", txt, flags=re.IGNORECASE):
            constraints_anchor = tag
            break

    constraints_list = []
    if constraints_anchor is not None:
        ul = constraints_anchor.find_next("ul")
        if ul:
            for li in ul.find_all("li"):
                constraints_list.append(li.get_text(" ", strip=True))

    examples = []
    for strong in soup.find_all("strong"):
        strong_text = strong.get_text(" ", strip=True)
        if re.match(r"Example\s*\d*\s*:", strong_text, re.IGNORECASE):
            block_texts = []
            cursor = strong.parent
            while cursor and cursor.name not in ["h3", "h4"]:
                cursor = cursor.find_next_sibling()
                if not cursor:
                    break
                if constraints_anchor and cursor == constraints_anchor:
                    break
                if cursor.find("strong") and re.match(
                    r"Example\s*\d*\s*:", cursor.get_text(" ", strip=True), re.IGNORECASE
                ):
                    break
                if cursor.name in ["pre", "code"]:
                    block_texts.append(cursor.get_text("\n", strip=True))
                elif cursor.name in ["p", "div"]:
                    text = cursor.get_text("\n", strip=True)
                    if any(k in text.lower() for k in ["input:", "output:", "explanation", "constraints"]):
                        block_texts.append(text)
            if not block_texts:
                pre = strong.find_next("pre")
                if pre:
                    block_texts.append(pre.get_text("\n", strip=True))
            examples.append((strong_text.rstrip(":"), "\n".join(block_texts).strip()))

    description_parts = []
    first_example_tag = None
    for strong in soup.find_all("strong"):
        if re.match(r"Example\s*\d*\s*:", strong.get_text(" ", strip=True), re.IGNORECASE):
            first_example_tag = strong
            break

    for node in soup.find_all(["p", "ul", "ol"]):
        if first_example_tag and (first_example_tag in node.descendants or node == first_example_tag):
            break
        if constraints_anchor and (constraints_anchor in node.descendants or node == constraints_anchor):
            break

        txt = node.get_text(" ", strip=True)
        if not txt:
            continue
        if re.match(r"Example\s*\d*\s*:", txt, re.IGNORECASE):
            break

        if node.name == "p":
            description_parts.append(txt)
        elif node.name in ["ul", "ol"]:
            for li in node.find_all("li", recursive=False):
                li_txt = li.get_text(" ", strip=True)
                if li_txt:
                    description_parts.append(f"- {li_txt}")

    description_text = "\n\n".join(description_parts).strip()

    return description_text, examples, constraints_list

def link_anchor_text_from_env(link: str) -> str:
    """
    Determine the anchor text based on query string from the URL.
    """
    try:
        parsed = urlsplit(link)
        qs = parse_qs(parsed.query)
        env_type = (qs.get("envType") or [""])[0].lower()
        env_id = (qs.get("envId") or [""])[0]

        if env_type == "daily-question" and re.fullmatch(r"\d{4}-\d{2}-\d{2}", env_id):
            return f"Daily Question {env_id}"
    except Exception:
        pass
    return "Link"

def build_readme(index: str, title: str, difficulty: str, link: str, description: str, examples: list, constraints: list) -> str:
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("## INFO")
    lines.append("")
    lines.append(f"**Index**: {index}")
    lines.append("")
    lines.append(f"**Level**: {difficulty}")
    lines.append("")

    anchor_text = link_anchor_text_from_env(link)
    lines.append(f"**Link**: [{anchor_text}]({link})")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## DESCRIPTION")
    lines.append("")
    lines.append(description if description else "_No description parsed_")
    lines.append("")
    lines.append("## EXAMPLE")
    lines.append("")
    if examples:
        for ex_title, body in examples:
            lines.append(f"### {ex_title}")
            lines.append("")
            lines.append("    " + "\n    ".join(body.splitlines()) if body else "    _No example body parsed_")
            lines.append("")
    else:
        lines.append("_No examples found_")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## CONTRAINTS")
    lines.append("")
    if constraints:
        for c in constraints:
            lines.append(f"- {c}")
    else:
        lines.append("- _No constraints parsed_")
    return "\n".join(lines).strip() + "\n"

def safe_folder_name(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()

def write_readme_for_link(session: requests.Session, link: str, out_file: Path = None, ensure_dir: bool = True) -> Path:
    original_link = link  # keep the original link to write in the README

    q = fetch_question(session, link)
    content = q.get("content") or ""
    desc, examples, constraints = html_to_text_blocks(content)

    index = q.get("questionFrontendId") or "N/A"
    difficulty = q.get("difficulty") or "Unknown"
    title = q.get("title") or "LeetCode Problem"

    readme_text = build_readme(
        index=str(index),
        title=title,
        difficulty=difficulty,
        link=original_link,
        description=desc,
        examples=examples,
        constraints=constraints
    )

    if out_file is None:
        folder_name = safe_folder_name(title)
        target_dir = Path(folder_name) if ensure_dir else Path(".")
        target_dir.mkdir(parents=True, exist_ok=True)
        out_file = target_dir / "README.md"

    out_file.write_text(readme_text, encoding="utf-8")
    return out_file

def main():
    parser = argparse.ArgumentParser(description="Generate README.md from LeetCode problem link(s).")
    parser.add_argument("links", nargs="+", help="One or more LeetCode problem links")
    parser.add_argument("-o", "--output", help="Output README.md path (only when a single link is provided)")
    args = parser.parse_args()

    if args.output and len(args.links) != 1:
        print("The -o/--output option can only be used when a single link is provided.", file=sys.stderr)
        sys.exit(2)

    ses = requests.Session()

    generated = []
    for link in args.links:
        out = Path(args.output) if args.output else None
        path = write_readme_for_link(ses, link, out_file=out, ensure_dir=(args.output is None))
        generated.append(path)

    if len(generated) == 1:
        print(f"✅ Created: {generated[0].resolve()}")
    else:
        print("✅ Created the following files:")
        for p in generated:
            print(" -", p.resolve())

if __name__ == "__main__":
    main()

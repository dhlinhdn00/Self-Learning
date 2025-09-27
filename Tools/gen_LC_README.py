import argparse
import os
import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
    titleSlug
    difficulty
    content
  }
}
"""

def extract_slug(url: str) -> str:
    """
    Lấy slug từ URL LeetCode:
    https://leetcode.com/problems/<slug>/(description)?(query...)
    """
    m = re.search(r"/problems/([^/]+)/?", url)
    if not m:
        raise ValueError(f"Không tìm thấy slug trong URL: {url}")
    return m.group(1)

def get_csrf_and_warmup(session: requests.Session, url: str) -> str:
    """
    Gọi GET để nhận csrftoken cookie hợp lệ trước khi gọi GraphQL.
    """
    session.headers.update({
        "User-Agent": "Mozilla/5.0",
        "Referer": url
    })
    session.get(url, timeout=20)
    return session.cookies.get("csrftoken", "")

def fetch_question(session: requests.Session, url: str) -> dict:
    """
    Gọi GraphQL lấy dữ liệu câu hỏi theo slug.
    """
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
        raise RuntimeError(f"Không lấy được dữ liệu câu hỏi cho slug: {slug}")
    return q

def html_to_text_blocks(html: str):
    """
    Chuyển nội dung HTML LeetCode thành các khối để dễ trích xuất:
    - mô tả
    - ví dụ (Example 1, 2, ...)
    - constraints
    """
    soup = BeautifulSoup(html or "", "html.parser")

    # Tìm mốc 'Constraints'
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

    # Tìm các khối Example
    examples = []
    # LeetCode thường render Example với <p><strong>Example 1:</strong></p> + <pre><code>...</code></pre>
    for strong in soup.find_all("strong"):
        strong_text = strong.get_text(" ", strip=True)
        if re.match(r"Example\s*\d*\s*:", strong_text, re.IGNORECASE):
            # Lấy block input/output (thường là pre/code sau đó)
            block_texts = []
            cursor = strong.parent
            # Đi tới các sibling tiếp theo đến trước khi gặp example khác hoặc constraints
            while cursor and cursor.name not in ["h3", "h4"]:
                cursor = cursor.find_next_sibling()
                if not cursor:
                    break
                # Nếu tới anchor constraints thì dừng
                if constraints_anchor and cursor == constraints_anchor:
                    break
                # Dừng khi đụng example mới
                if cursor.find("strong") and re.match(
                    r"Example\s*\d*\s*:", cursor.get_text(" ", strip=True), re.IGNORECASE
                ):
                    break
                # Thu thập code/pre/paragraph liên quan
                if cursor.name in ["pre", "code"]:
                    block_texts.append(cursor.get_text("\n", strip=True))
                elif cursor.name in ["p", "div"]:
                    # Chỉ thêm đoạn có vẻ là Input/Output/Explanation
                    text = cursor.get_text("\n", strip=True)
                    if any(k in text.lower() for k in ["input:", "output:", "explanation", "constraints"]):
                        block_texts.append(text)
            # Nếu không bắt được gì, thử lấy pre gần nhất sau strong
            if not block_texts:
                pre = strong.find_next("pre")
                if pre:
                    block_texts.append(pre.get_text("\n", strip=True))
            examples.append((strong_text.rstrip(":"), "\n".join(block_texts).strip()))

    # Mô tả: các đoạn trước ví dụ đầu tiên
    description_parts = []
    first_example_tag = None
    for strong in soup.find_all("strong"):
        if re.match(r"Example\s*\d*\s*:", strong.get_text(" ", strip=True), re.IGNORECASE):
            first_example_tag = strong
            break

    # Thu thập mọi p/li trước example đầu tiên và trước constraints
    for node in soup.find_all(["p", "ul", "ol"]):
        if first_example_tag and node.sourcepos and hasattr(first_example_tag, "sourcepos"):
            # sourcepos hiếm khi có; fallback dưới
            pass
        # Fallback: dừng khi gặp example hoặc constraints
        if first_example_tag and (first_example_tag in node.descendants or node == first_example_tag):
            break
        if constraints_anchor and (constraints_anchor in node.descendants or node == constraints_anchor):
            break

        # Bỏ qua các đoạn tiêu đề rác
        txt = node.get_text(" ", strip=True)
        if not txt:
            continue
        # Đừng nhặt example label lạc lõng
        if re.match(r"Example\s*\d*\s*:", txt, re.IGNORECASE):
            break

        # Ghi lại nội dung mô tả
        if node.name == "p":
            description_parts.append(txt)
        elif node.name in ["ul", "ol"]:
            for li in node.find_all("li", recursive=False):
                li_txt = li.get_text(" ", strip=True)
                if li_txt:
                    description_parts.append(f"- {li_txt}")

    description_text = "\n\n".join(description_parts).strip()

    return description_text, examples, constraints_list

def build_readme(index: str, difficulty: str, link: str, description: str, examples: list, constraints: list) -> str:
    """
    Lắp nội dung README theo format yêu cầu.
    """
    # Tiêu đề: nếu muốn có thêm tên bài, có thể thêm vào (nhưng bản mẫu chỉ có tiêu đề cố định)
    lines = []
    lines.append("# Maximum Number of Words You Can Type" if "maximum-number-of-words-you-can-type" in link else "# LeetCode Problem")
    lines.append("")
    lines.append("## INFO")
    lines.append("")
    lines.append(f"**Index**: {index}")
    lines.append("")
    lines.append(f"**Level**: {difficulty}")
    lines.append("")
    # đảm bảo link kiểu /description để xem nội dung đầy đủ
    if "/description" not in link:
        if link.endswith("/"):
            link_desc = link + "description/"
        else:
            # giữ nguyên query (envType, envId) nếu có
            parts = link.split("?")
            base = parts[0]
            query = ("?" + parts[1]) if len(parts) > 1 else ""
            if base.endswith("/"):
                link_desc = base + "description/" + query
            else:
                link_desc = base + "/description/" + query
    else:
        link_desc = link

    lines.append(f"**Link**: [Link]({link_desc})")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## DESCRIPTION")
    lines.append("")
    if description:
        lines.append(description)
    else:
        lines.append("_No description parsed_")
    lines.append("")
    lines.append("## EXAMPLE")
    lines.append("")
    if examples:
        for i, (title, body) in enumerate(examples, 1):
            lines.append(f"### {title}")
            lines.append("")
            if body:
                # định dạng khối code/IO
                lines.append("    " + "\n    ".join(body.splitlines()))
            else:
                lines.append("    _No example body parsed_")
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

def write_readme_for_link(session: requests.Session, link: str, out_file: Path = None, ensure_dir: bool = True) -> Path:
    q = fetch_question(session, link)
    content = q.get("content") or ""
    desc, examples, constraints = html_to_text_blocks(content)
    index = q.get("questionId") or "N/A"
    difficulty = q.get("difficulty") or "Unknown"

    readme_text = build_readme(index=str(index), difficulty=difficulty, link=link, description=desc, examples=examples, constraints=constraints)

    # Nếu không chỉ định -o và có nhiều link, tạo thư mục theo slug
    slug = extract_slug(link)
    if out_file is None:
        target_dir = Path(slug) if ensure_dir else Path(".")
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
        print("Tuỳ chọn -o/--output chỉ dùng khi truyền đúng 1 link.", file=sys.stderr)
        sys.exit(2)

    ses = requests.Session()

    generated = []
    for link in args.links:
        out = Path(args.output) if args.output else None
        path = write_readme_for_link(ses, link, out_file=out, ensure_dir=(args.output is None))
        generated.append(path)

    if len(generated) == 1:
        print(f"✅ Đã tạo: {generated[0].resolve()}")
    else:
        print("✅ Đã tạo các file:")
        for p in generated:
            print(" -", p.resolve())

if __name__ == "__main__":
    main()

import re
from typing import List, Tuple

from bs4 import BeautifulSoup


def clean_text(text: str) -> str:
    """Normalize spaces in plain text (NOT for code)."""
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,;:!?])", r"\1", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\s+\)", ")", text)
    return text.strip()


def extract_sample_codes(html: str) -> List[str]:
    """Extract all code samples from <pre><code>...</code></pre> blocks."""
    soup = BeautifulSoup(html or "", "html.parser")
    codes: List[str] = []

    for pre in soup.find_all("pre"):
        code_tag = pre.find("code")
        if code_tag:
            code_text = code_tag.get_text("\n", strip=True)
            if code_text:
                codes.append(code_text)

    return codes


def html_to_text_blocks(html: str) -> Tuple[str, List[Tuple[str, str]], List[str]]:
    """Convert LeetCode HTML content to description, examples, constraints."""
    soup = BeautifulSoup(html or "", "html.parser")

    # Find "Constraints" anchor
    constraints_anchor = None
    for tag in soup.find_all(["p", "strong", "h3", "h4", "span"]):
        txt = tag.get_text(" ", strip=True)
        if re.fullmatch(r"Constraints:?|Constraint:?", txt, flags=re.IGNORECASE):
            constraints_anchor = tag
            break

    # Extract constraints list
    constraints_list: List[str] = []
    if constraints_anchor:
        ul = constraints_anchor.find_next("ul")
        if ul:
            for li in ul.find_all("li"):
                raw = li.get_text(" ", strip=True)
                txt = clean_text(raw)
                if txt:
                    constraints_list.append(txt)

    # Extract examples
    examples: List[Tuple[str, str]] = []
    for strong in soup.find_all("strong"):
        strong_text = strong.get_text(" ", strip=True)
        if re.match(r"Example\s*\d*\s*:", strong_text, re.IGNORECASE):

            block_texts: List[str] = []
            cursor = strong.parent
            # Walk siblings until next example / constraints / header
            while cursor and cursor.name not in ["h3", "h4"]:
                cursor = cursor.find_next_sibling()
                if not cursor:
                    break
                if constraints_anchor and cursor == constraints_anchor:
                    break
                if cursor.find("strong") and re.match(
                    r"Example\s*\d*\s*:",
                    cursor.get_text(" ", strip=True),
                    re.IGNORECASE,
                ):
                    break

                if cursor.name in ["pre", "code"]:
                    block_texts.append(cursor.get_text("\n", strip=True))
                elif cursor.name in ["p", "div"]:
                    text = cursor.get_text("\n", strip=True)
                    if any(k in text.lower() for k in ["input:", "output:", "explanation"]):
                        block_texts.append(clean_text(text))

            # Fallback: directly next <pre> if no block captured
            if not block_texts:
                pre = strong.find_next("pre")
                if pre:
                    block_texts.append(pre.get_text("\n", strip=True))

            examples.append((strong_text.rstrip(":"), "\n".join(block_texts).strip()))

    # Extract description (before first example / constraints)
    description_parts: List[str] = []
    first_example_tag = next(
        (
            strong
            for strong in soup.find_all("strong")
            if re.match(
                r"Example\s*\d*\s*:",
                strong.get_text(" ", strip=True),
                re.IGNORECASE,
            )
        ),
        None,
    )

    for node in soup.find_all(["p", "ul", "ol"]):
        if first_example_tag and (first_example_tag in node.descendants):
            break
        if constraints_anchor and (constraints_anchor in node.descendants):
            break

        raw_txt = node.get_text(" ", strip=True)
        txt = clean_text(raw_txt)
        if not txt:
            continue

        if node.name == "p":
            description_parts.append(txt)
        elif node.name in ["ul", "ol"]:
            items: List[str] = []
            for li in node.find_all("li", recursive=False):
                raw_li = li.get_text(" ", strip=True)
                li_txt = clean_text(raw_li)
                if li_txt:
                    items.append(li_txt)
            if items:
                description_parts.append("- " + "\n- ".join(items))

    description_text = "\n\n".join(description_parts).strip()
    return description_text, examples, constraints_list

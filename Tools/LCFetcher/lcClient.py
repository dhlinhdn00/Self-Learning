import re
from typing import Dict, Any, List

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

# Query to fetch problem description
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

# Query to fetch starter code snippets
QUERY_EDITOR = """
query questionEditorData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    codeSnippets {
      lang
      langSlug
      code
    }
  }
}
"""


def extract_slug(url: str) -> str:
    """Extract the title slug from a LeetCode problem URL."""
    m = re.search(r"/problems/([^/]+)/?", url)
    if not m:
        raise ValueError(f"Slug not found in URL: {url}")
    return m.group(1)


def get_csrf_and_warmup(session: requests.Session, url: str) -> str:
    """Warm up the session and return csrf token."""
    session.headers.update({
        "User-Agent": "Mozilla/5.0",
        "Referer": url,
    })
    session.get(url, timeout=20)
    return session.cookies.get("csrftoken", "")


def fetch_question(session: requests.Session, url: str) -> Dict[str, Any]:
    """Fetch question metadata and HTML content via GraphQL."""
    slug = extract_slug(url)

    warm_url = f"https://leetcode.com/problems/{slug}/description/"
    csrftoken = get_csrf_and_warmup(session, warm_url)

    headers = {
        "Content-Type": "application/json",
        "Referer": warm_url,
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


def fetch_starter_code(session: requests.Session, slug: str, referer_url: str) -> List[Dict[str, Any]]:
    """Fetch all starter code snippets (all languages) from editor data."""
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Referer": referer_url,
    }

    resp = session.post(
        GRAPHQL_URL,
        json={"query": QUERY_EDITOR, "variables": {"titleSlug": slug}},
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()

    data = resp.json()
    return (data.get("data") or {}).get("question", {}).get("codeSnippets", []) or []

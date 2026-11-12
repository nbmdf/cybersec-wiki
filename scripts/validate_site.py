"""CyberSec Wiki static site checker — standard library only.

Run from project root: python scripts/validate_site.py
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parent.parent
PAGES = [ROOT / "index.html", *sorted((ROOT / "topics").glob("*.html"))]
SECTION_IDS = ["introduction", "core-concepts", "examples", "defense", "summary", "references"]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.headings = []
        self.current_h1 = False
        self.section_ids = []
        self.topic_cards = []
        self.external_blank = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "section" and attrs.get("id") in SECTION_IDS:
            self.section_ids.append(attrs["id"])
        if tag in ("a", "link", "script", "img"):
            name = {"a": "href", "link": "href", "script": "src", "img": "src"}[tag]
            if attrs.get(name):
                self.links.append((tag, attrs[name]))
        if tag == "a" and "data-topic-card" in attrs:
            self.topic_cards.append(attrs)
        if tag == "a" and attrs.get("target") == "_blank" and "noopener" not in attrs.get("rel", ""):
            self.external_blank.append(attrs.get("href", ""))
        if tag == "h1":
            self.headings.append("h1")


issues = []
for page in PAGES:
    if not page.exists():
        issues.append(f"Missing page: {page.relative_to(ROOT)}")
        continue
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    if len(parser.headings) != 1:
        issues.append(f"{page.name}: expected 1 h1, got {len(parser.headings)}")
    if page.parent.name == "topics" and parser.section_ids != SECTION_IDS:
        issues.append(f"{page.name}: article sections mismatch: {parser.section_ids}")
    if page.name == "index.html" and len(parser.topic_cards) < 3:
        issues.append("index.html: expected at least 3 article cards")
    for target in parser.external_blank:
        issues.append(f"{page.name}: external _blank link missing noopener: {target}")
    for tag, value in parser.links:
        if value.startswith(("https://", "http://", "mailto:", "tel:", "data:")):
            continue
        if value.startswith("/"):
            issues.append(f"{page.name}: prohibited root-relative asset/link: {value}")
            continue
        parts = urlsplit(value)
        if parts.scheme:
            continue
        path = unquote(parts.path)
        linked_file = ((page.parent / path).resolve() if path else page.resolve())
        if not linked_file.is_file():
            issues.append(f"{page.name}: missing local file {value}")
            continue
        if parts.fragment and linked_file.suffix == ".html":
            target_parser = PageParser()
            target_parser.feed(linked_file.read_text(encoding="utf-8"))
            if unquote(parts.fragment) not in target_parser.ids:
                issues.append(f"{page.name}: broken anchor {value}")

if issues:
    print("[FAIL] CyberSec Wiki static checks")
    for issue in issues:
        print(" -", issue)
    sys.exit(1)
print(f"[PASS] {len(PAGES)} HTML pages validated: local links, anchors, section IDs, and basic structure.")

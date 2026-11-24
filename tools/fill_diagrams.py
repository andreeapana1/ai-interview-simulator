"""Replace [[IFRAME url]] markers in knowledge/coursera/*.md with the visible text
of that interactive diagram (public HTML pages on Coursera's CDN).

Usage:  python3 tools/fill_diagrams.py
"""
import re
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

FOLDER = Path(__file__).resolve().parent.parent / "knowledge" / "coursera"
MARKER = re.compile(r"\[\[IFRAME (\S+)\]\]")
SKIP = {"script", "style", "svg", "noscript", "head"}
BLOCK = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "div", "button", "td", "th", "tr", "section", "label", "br"}


class TextGrab(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip_depth = 0
        self.lines, self.buf = [], []

    def flush(self):
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        if text:
            self.lines.append(text)
        self.buf = []

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip_depth += 1
        elif tag in BLOCK:
            self.flush()

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip_depth = max(0, self.skip_depth - 1)
        elif tag in BLOCK:
            self.flush()

    def handle_data(self, data):
        if not self.skip_depth:
            self.buf.append(data)


def diagram_text(url):
    html = urllib.request.urlopen(url, timeout=30).read().decode("utf-8", "replace")
    p = TextGrab()
    p.feed(html)
    p.flush()
    out = []
    for line in p.lines:  # drop exact repeats (animations often duplicate text)
        if line not in out:
            out.append(line)
    return out


def main():
    for md in sorted(FOLDER.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        for url in MARKER.findall(text):
            lines = diagram_text(url)
            block = "**Interactive diagram (text content):**\n\n" + "\n".join(f"> {l}" for l in lines)
            text = text.replace(f"[[IFRAME {url}]]", block)
            print(f"{md.name}: {len(lines)} lines")
        md.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

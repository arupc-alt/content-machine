#!/usr/bin/env python3
"""Content Machine QA measurements (modes/qa.md, Step 1.5).

Measures a saved draft before QA judges it. The numbers it prints are
evidence for the QA report, and every hit it lists goes into the matching
dimension (shared/base-rules/qa.md) with its location.

Standard library only. If the optional textstat package is installed, its
Flesch-Kincaid grade is also reported and preferred.

Usage:
  Drive:  python3 measure.py draft.txt --html draft.html [options]
  Notion: python3 measure.py --markdown draft.md [options]
          (plain text is derived from the Markdown when no text file is given)

Options:
  --keyword "primary keyword"   keyword placement and density (Dimension 1)
  --target-words N              the brief's target word count (Dimension 17)
  --spelling US|UK              the product's spelling (Settings), default US
  --site https://example.com    the product's Website URL, to split internal links
  --banned FILE                 extra words or phrases banned outright, one per
                                line (the style guide's list, Script product rules)
  --grade-target N              the top of the target reading grade, default 6
                                (Dimension 18; a reading-level Exception rule sets it)
  --grade-ceiling N             a reading grade above this is a Blocker, default 7
                                (the top of the target range plus 1)
  --check-links                 fetch every link and report its HTTP status
  --self-test                   run on a built-in sample and exit 0 if it works

Output: one JSON report on stdout.
"""

import argparse
import html as htmllib
import json
import re
import statistics
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser

try:  # optional
    import textstat  # type: ignore
except Exception:  # pragma: no cover
    textstat = None

CONTEXT = 40

# ---------------------------------------------------------------------------
# Word lists (Dimensions 13, 14, 15, 16, 18, 23)
# ---------------------------------------------------------------------------

BANNED_CHARS = {
    "\u2014": "em dash",
    "\u2013": "en dash used as a dash",
    "\u2012": "figure dash used as a dash",
    "\u2015": "horizontal bar used as a dash",
    "\u2026": "ellipsis character",
    "\u200b": "zero-width space",
    "\ufeff": "byte-order mark",
    "\ufffd": "replacement character (garbled text)",
}

AI_WORDS = [
    r"delv(?:e|es|ed|ing)", r"boasts?", r"showcas(?:e|es|ed|ing)", r"underscor(?:e|es|ed|ing)",
    r"comprehending", r"intricate", r"intricac(?:y|ies)", r"surpass(?:es|ed|ing)?", r"garnered",
    r"emphasi[sz]ing", r"realms?", r"groundbreaking", r"advancements?", r"aligns?",
    r"leverag(?:e|es|ed|ing)", r"elevat(?:e|es|ed|ing)", r"unlock(?:s|ed|ing)?",
    r"navigat(?:e|es|ed|ing)", r"embark(?:s|ed|ing)?", r"empower(?:s|ed|ing)?",
    r"cultivat(?:e|es|ed|ing)", r"harness(?:es|ed|ing)?", r"foster(?:s|ed|ing)?",
    r"bolster(?:s|ed|ing)?", r"streamlin(?:e|es|ed|ing)", r"enhanc(?:e|es|ed|ing)",
    r"crucial", r"vital", r"essential", r"unparalleled", r"unprecedented", r"cutting-edge",
    r"holistic", r"pivotal", r"invaluable", r"dynamic", r"multifaceted", r"ever-evolving",
    r"transformative", r"game-changing", r"robust", r"seamless(?:ly)?", r"meticulous(?:ly)?",
    r"vibrant", r"bespoke", r"tapestry", r"testament", r"myriad", r"plethora", r"paradigm",
    r"synerg(?:y|ies)", r"cornerstone", r"catalyst", r"beacon", r"landscapes?", r"journeys?",
    r"nestled", r"commendable", r"noteworthy", r"ecosystems?",
]

AI_PHRASES = [
    r"in today's (?:fast-paced|digital) world", r"in the ever-evolving landscape of",
    r"it's important to note that", r"it is important to note that", r"it's worth noting",
    r"it is worth noting", r"it goes without saying", r"when it comes to", r"at the end of the day",
    r"not only\b[^.?!\n]{0,80}\bbut also", r"whether you're\b[^.?!\n]{0,60}\bor\b",
    r"unlock the (?:power|potential) of", r"take\b[^.?!\n]{0,40}\bto the next level",
    r"stay ahead of the curve", r"a game-changer for", r"revolutioni[sz]e the way",
    r"in conclusion", r"in summary", r"in a nutshell",
    r"plays? an? (?:crucial|pivotal|vital) role in", r"serves as a testament to", r"stands as an?",
    r"marking a pivotal moment", r"a testament to", r"rest assured", r"dive into", r"let's dive in",
    r"look no further", r"we've got you covered", r"the world of", r"navigating the complexities of",
    r"designed to", r"helps? you \w+(?: \w+){0,3} with ease", r"great question",
    r"i hope this helps", r"happy selling",
]
# "Overall," as a section or sentence opener
AI_OPENERS = [r"Overall,"]

STRUCTURE_PATTERNS = {
    "negative parallelism": [
        r"\b(?:it's|it is|this is|that's) not (?:just|only|merely|about)\b[^.?!\n]{0,60}[,;]\s*(?:it's|it is|but)\b",
        r"\bnot (?:just|only|merely)\b[^.?!\n]{1,60}\bbut\b",
        r"\bnot \w+(?: \w+){0,3}, but\b",
        r"\bno \w+(?: \w+)?, no \w+(?: \w+)?, just\b",
    ],
    "false range (check it is a real spectrum)": [r"\bfrom [^.,;:?!\n]{1,40}? to [^.,;:?!\n]{1,40}"],
    "hanging -ing tail": [
        r", (?:highlighting|underscoring|reflecting|showcasing|ensuring|emphasizing|emphasising|"
        r"demonstrating|signaling|signalling|illustrating|making it|contributing to|paving the way)\b"
    ],
    "empty significance claim": [
        r"\b(?:is|are) (?:important|crucial|critical|key|vital|essential)\b",
        r"\bkey consideration", r"\bplays? an? (?:key|important|major|significant) role\b",
    ],
    "section-ending recap opener": [r"(?:^|(?<=[.!?]\s))(?:In short|Overall|Ultimately|In summary|In conclusion|To sum up|To summarize|All in all),"],
    "chat leftover or placeholder": [
        r"\bCertainly\b", r"(?:^|(?<=[.!?]\s))Here's\b", r"\bAs an AI\b", r"\bI hope this helps\b",
        r"\bas of my (?:last|knowledge)\b", r"\bknowledge cutoff\b", r"\[insert[^\]]*\]", r"\bTBD\b",
        r"\blorem ipsum\b", r"\bGreat question\b",
    ],
    "hedging stack": [
        r"\bcan potentially\b", r"\bcould potentially\b", r"\bmay possibly\b", r"\bmight possibly\b",
        r"\bmight be able to\b", r"\bmay be able to\b", r"\bmay potentially\b",
    ],
}

VAGUE_PHRASES = [
    r"many businesses", r"many people", r"many users", r"many companies", r"many stores",
    r"some people", r"a lot of time", r"a lot of money", r"a lot of", r"lots of",
    r"can be expensive", r"various options", r"various", r"numerous", r"a number of",
    r"a significant amount", r"a wide range of", r"a variety of", r"countless", r"plenty of",
]

VAGUE_ATTRIBUTION = [
    r"studies show", r"studies suggest", r"research shows", r"research suggests", r"experts say",
    r"experts agree", r"industry reports suggest", r"reports suggest", r"according to experts",
    r"surveys show", r"statistics show", r"data shows", r"many businesses",
]

MONTHS = (r"(?:January|February|March|April|May|June|July|August|September|October|November|December|"
          r"Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)")

DATE_ANCHORS = [
    ("as of", r"\bas of\b"),
    ("starting in", r"\bstarting in\b"),
    ("since a date", r"\bsince (?:" + MONTHS + r"\b|last (?:year|month|week)|(?:19|20)\d{2}\b)"),
    ("month and year", r"\b" + MONTHS + r"\.? (?:\d{1,2}(?:st|nd|rd|th)?,? )?(?:19|20)\d{2}\b"),
    ("on a date", r"\bon " + MONTHS + r" \d{1,2}\b"),
    ("version number", r"\b(?:in |since |with )?version \d+(?:\.\d+)*\b|\bv\d+(?:\.\d+)+\b"),
    ("relative date", r"\b(?:last|this|next) (?:year|month)\b|\brecently (?:launched|released|added)\b|\bjust (?:launched|released)\b"),
    ("bare year", r"\b(?:19|20)\d{2}\b"),
]

US_TO_UK_FLAGS = [  # spellings to flag when the product uses UK spelling
    r"colors?", r"colored", r"favorites?", r"favorite", r"flavors?", r"honors?", r"labors?",
    r"neighbors?", r"behaviors?", r"centers?", r"theaters?", r"analyz(?:e|es|ed|ing)",
    r"defense", r"offense", r"traveling", r"traveled", r"canceled", r"canceling", r"labeled",
    r"labeling", r"modeling", r"fulfill", r"enroll", r"catalog", r"gray", r"aging",
]
UK_TO_US_FLAGS = [  # spellings to flag when the product uses US spelling
    r"colours?", r"coloured", r"favourites?", r"flavours?", r"honours?", r"labours?",
    r"neighbours?", r"behaviours?", r"centres?", r"theatres?", r"analys(?:e|es|ed|ing)",
    r"defence", r"offence", r"travelling", r"travelled", r"cancelled", r"cancelling", r"labelled",
    r"labelling", r"modelling", r"fulfil", r"enrol", r"catalogue", r"grey", r"ageing", r"licence",
    r"programme", r"judgement", r"cheque",
    r"(?:organ|real|recogn|optim|custom|priorit|maxim|minim|util|summar|personal|apolog|categor|"
    r"emphas|standard|monet|automat|capital|final|normal|special|visual|synchron|author|critic|"
    r"organ|memor|stabil|monetis|digit)is(?:e|es|ed|ing|ation|ations)",
]

SLUG_STOP_WORDS = {"a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "for", "with",
                   "at", "by", "from", "is", "are", "be", "your", "you", "how", "what", "why", "it"}
BAD_ANCHORS = {"click here", "here", "learn more", "read more", "this link", "this", "link",
               "more", "this page", "find out more"}
SEO_LABELS = (r"SEO Metadata|SEO Title|Title Tag|Meta Title|Meta Description|URL Slug|Slug|"
              r"Primary Keyword|Secondary Keywords?|Focus Keyword|Keywords?|Canonical(?: URL)?|"
              r"Schema|Excerpt|OG Title|OG Description|Featured Image(?: Alt Text)?|Alt Text")
CONCLUSION_RE = re.compile(r"conclusion|final thoughts|wrapping up|bottom line|next steps|"
                           r"the takeaway|key takeaways|summary", re.I)
FAQ_RE = re.compile(r"\bFAQs?\b|frequently asked", re.I)
SMALL_WORDS = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "as", "at",
               "by", "in", "of", "off", "on", "per", "to", "up", "via", "vs", "vs.", "with", "from",
               "into", "over"}

WORD_RE = re.compile(r"\$?[^\W_][\w'\u2019$%.,\-]*", re.UNICODE)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def loc(text, start, end=None):
    """Line, column, and surrounding text for a match."""
    end = start + 1 if end is None else end
    line = text.count("\n", 0, start) + 1
    col = start - (text.rfind("\n", 0, start) + 1) + 1
    ctx = text[max(0, start - CONTEXT):end + CONTEXT].replace("\r", " ").replace("\n", " ")
    return {"line": line, "column": col, "context": ctx.strip()}


def sentence_at(text, pos):
    start = max(text.rfind(".", 0, pos), text.rfind("!", 0, pos), text.rfind("?", 0, pos),
                text.rfind("\n", 0, pos)) + 1
    ends = [i for i in (text.find(".", pos), text.find("!", pos), text.find("?", pos),
                        text.find("\n", pos)) if i != -1]
    end = min(ends) + 1 if ends else len(text)
    return text[start:end].strip()


def words_of(text):
    return [w.rstrip(".,-") for w in WORD_RE.findall(text) if w.rstrip(".,-")]


def sentences_of(text):
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        for s in re.split(r"(?<=[.!?])[\"'\u201d\u2019)\]]*\s+", line):
            if len(s.split()) > 2:
                out.append(s.strip())
    return out


def syllables(word):
    w = word.lower().strip(".,'$%-\u2019")
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups) - (1 if w.endswith("e") and len(groups) > 1 else 0)
    return max(1, n)


def kw_regex(keyword):
    parts = [re.escape(p) for p in keyword.lower().split()]
    if not parts:
        return None
    return re.compile(r"(?<![\w-])" + r"[\s\-]+".join(parts) + r"(?:s|es)?(?![\w-])", re.I)


def norm_space(s):
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()


def unwrap_google_link(href):
    if href and re.match(r"https?://(?:www\.)?google\.com/url\?", href):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(href).query).get("q")
        if q:
            return q[0]
    return href


# ---------------------------------------------------------------------------
# Structure: blocks from HTML (Drive) or Markdown (Notion)
# ---------------------------------------------------------------------------

BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "table", "blockquote", "pre", "hr"}
VOID_TAGS = {"br", "img", "hr", "meta", "link", "input", "col", "area", "base", "wbr", "source"}
SKIP_TAGS = {"head", "style", "script", "title"}


def css_classes(html_text, pred):
    out = set()
    for css in re.findall(r"<style[^>]*>(.*?)</style>", html_text, flags=re.S | re.I):
        for names, body in re.findall(r"([^{}]+)\{([^}]*)\}", css):
            if pred(body):
                for n in re.findall(r"\.([\w-]+)", names):
                    out.add(n)
    return out


def is_bold_css(body):
    return bool(re.search(r"font-weight\s*:\s*(?:bold|[6-9]00)", body, re.I))


def has_border_css(body):
    return bool(re.search(r"border(?:-(?:top|right|bottom|left))?-width\s*:\s*(?:0*[1-9][\d.]*|0?\.\d*[1-9])\s*(?:pt|px)", body, re.I)
                or re.search(r"border\s*:\s*[^;]*\b[1-9]\d*(?:pt|px)", body, re.I))


class DocHTML(HTMLParser):
    def __init__(self, bold_classes, border_classes):
        super().__init__(convert_charrefs=True)
        self.bold_classes = bold_classes
        self.border_classes = border_classes
        self.blocks = []
        self.cur = None
        self.depth = 0
        self.skip = 0
        self.stack = []
        self.link = None

    def _bold_attr(self, tag, attrs):
        a = dict(attrs)
        if tag in ("b", "strong"):
            return True
        cls = (a.get("class") or "").split()
        if any(c in self.bold_classes for c in cls):
            return True
        return is_bold_css(a.get("style") or "")

    def _bold(self):
        return any(b for _, b in self.stack)

    def handle_startendtag(self, tag, attrs):
        if tag in VOID_TAGS:
            self.handle_starttag(tag, attrs)
        else:
            self.handle_starttag(tag, attrs)
            self.handle_endtag(tag)

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip += 1
            return
        if self.skip:
            return
        a = dict(attrs)
        if tag == "br":
            if self.cur is not None:
                self._text("\n")
            return
        if self.cur is None:
            if tag in BLOCK_TAGS:
                self.cur = {"type": tag, "runs": [], "links": [], "items": [], "rows": [],
                            "borders": a.get("border") not in (None, "0"), "th": False}
                if tag == "hr":
                    self._finish()
                    return
                self.depth = 1
                self.stack = [(tag, self._bold_attr(tag, attrs))]
            return
        if tag in VOID_TAGS:
            return
        self.depth += 1
        self.stack.append((tag, self._bold_attr(tag, attrs)))
        if tag == "li":
            self.cur["items"].append({"runs": []})
        elif tag == "tr":
            self.cur["rows"].append([])
        elif tag in ("td", "th"):
            if tag == "th":
                self.cur["th"] = True
            cls = (a.get("class") or "").split()
            if any(c in self.border_classes for c in cls) or has_border_css(a.get("style") or ""):
                self.cur["borders"] = True
            if not self.cur["rows"]:
                self.cur["rows"].append([])
            self.cur["rows"][-1].append({"runs": []})
        elif tag == "a":
            self.link = {"href": unwrap_google_link(a.get("href") or ""), "text": ""}

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip or self.cur is None or tag in VOID_TAGS:
            return
        if tag == "a" and self.link is not None:
            self.link["text"] = norm_space(self.link["text"])
            self.cur["links"].append(self.link)
            self.link = None
        # pop to the matching tag
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                popped = len(self.stack) - i
                del self.stack[i:]
                self.depth -= popped
                break
        if self.depth <= 0 or not self.stack:
            self._finish()

    def handle_data(self, data):
        if self.skip or self.cur is None:
            return
        self._text(data)

    def _text(self, data):
        bold = self._bold()
        run = (data, bold)
        self.cur["runs"].append(run)
        if self.cur["items"] and any(t == "li" for t, _ in self.stack):
            self.cur["items"][-1]["runs"].append(run)
        if self.cur["rows"] and any(t in ("td", "th") for t, _ in self.stack) and self.cur["rows"][-1]:
            self.cur["rows"][-1][-1]["runs"].append(run)
        if self.link is not None:
            self.link["text"] += data

    def _finish(self):
        self.blocks.append(make_block(self.cur))
        self.cur = None
        self.depth = 0
        self.stack = []


def runs_info(runs):
    text = norm_space("".join(r for r, _ in runs))
    bold_words = sum(len(words_of(r)) for r, b in runs if b)
    first = next(((r, b) for r, b in runs if r.strip()), None)
    bold_runs, prev = 0, False
    for r, b in runs:
        if not r.strip():
            continue
        if b and not prev:
            bold_runs += 1
        prev = b
    lead = ""
    if first and first[1]:
        for r, b in runs:
            if not r.strip() and not lead:
                continue
            if not b:
                break
            lead += r
    return text, bold_words, bool(first and first[1]), bold_runs, norm_space(lead)


def make_block(cur):
    t = cur["type"]
    text, bold_words, starts_bold, bold_runs, lead = runs_info(cur["runs"])
    n_words = len(words_of(text))
    b = {"type": t, "text": text, "words": n_words, "bold_words": bold_words,
         "bold_runs": bold_runs, "starts_bold": starts_bold, "bold_lead": lead,
         "links": cur.get("links", [])}
    if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
        b["kind"] = "heading"
        b["level"] = int(t[1])
    elif t in ("ul", "ol"):
        b["kind"] = "list"
        items = []
        for it in cur["items"]:
            itext, _, ibold, _, ilead = runs_info(it["runs"])
            items.append({"text": itext, "starts_bold": ibold, "bold_lead": ilead})
        b["items"] = items
    elif t == "table":
        b["kind"] = "table"
        rows = []
        first_row_bold = None
        for ri, row in enumerate(cur["rows"]):
            cells = []
            all_bold = True
            for c in row:
                ct, cb, _, _, _ = runs_info(c["runs"])
                cells.append(ct)
                if words_of(ct) and cb < len(words_of(ct)):
                    all_bold = False
            rows.append(cells)
            if ri == 0:
                first_row_bold = all_bold
        b["rows"] = rows
        b["header_row"] = bool(cur.get("th") or first_row_bold)
        b["borders"] = bool(cur.get("borders"))
    elif t == "hr":
        b["kind"] = "divider"
    else:
        if not text:
            b["kind"] = "empty"
        elif re.match(r"^\[[A-Z][A-Z _:-]{2,}\]", text):
            b["kind"] = "callout"
        elif n_words and bold_words >= n_words and n_words <= 12:
            b["kind"] = "bold_line"
        else:
            b["kind"] = "paragraph"
    return b


def blocks_from_html(h):
    bold = css_classes(h, is_bold_css)
    border = css_classes(h, has_border_css)
    p = DocHTML(bold, border)
    body = re.search(r"<body[^>]*>(.*)</body>", h, flags=re.S | re.I)
    p.feed(body.group(1) if body else h)
    p.close()
    if p.cur is not None:
        p._finish()
    return p.blocks


# Markdown (Notion-flavored)

ESC_MAP = {}


def protect_escapes(s):
    def rep(m):
        ch = m.group(1)
        return "\ue000" + format(ord(ch), "x") + "\ue001"
    return re.sub(r"\\([\\`*_{}\[\]()#+\-.!|>~$<&])", rep, s)


def restore_escapes(s):
    return re.sub("\ue000([0-9a-f]+)\ue001", lambda m: chr(int(m.group(1), 16)), s)


def md_inline_runs(s):
    """Split a Markdown line into (text, bold) runs, with links stripped to their text."""
    s = protect_escapes(s)
    links = []

    def link_rep(m):
        links.append({"href": m.group(2).strip(), "text": norm_space(restore_escapes(m.group(1)).replace("**", ""))})
        return m.group(1)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
    s = re.sub(r"(?<!\])\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", link_rep, s)
    for m in re.finditer(r"<a [^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", s):
        links.append({"href": m.group(1), "text": norm_space(re.sub(r"<[^>]+>", "", m.group(2)))})
    s = re.sub(r"<(?:strong|b)>(.*?)</(?:strong|b)>", r"**\1**", s)
    s = re.sub(r"<[^>]+>", "", s)
    runs = []
    parts = re.split(r"(\*\*|__)", s)
    bold = False
    for part in parts:
        if part in ("**", "__"):
            bold = not bold
            continue
        part = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)\*(?!\w)", r"\1", part)
        part = re.sub(r"(?<![\w_])_(?!\s)([^_]+?)_(?!\w)", r"\1", part)
        part = part.replace("`", "")
        if part:
            runs.append((restore_escapes(part), bold))
    return runs, links


def blocks_from_markdown(md):
    lines = md.splitlines()
    blocks = []
    i = 0
    n = len(lines)

    def add_para(line, kind_hint=None):
        runs, links = md_inline_runs(line)
        cur = {"type": "p", "runs": runs, "links": links}
        b = make_block(cur)
        if kind_hint:
            b["kind"] = kind_hint
        blocks.append(b)

    while i < n:
        raw = lines[i]
        line = raw.strip()
        if not line:
            i += 1
            continue
        if re.match(r"^<empty-block\s*/?>$", line):
            blocks.append({"type": "p", "kind": "empty", "text": "", "words": 0, "bold_words": 0,
                           "bold_runs": 0, "starts_bold": False, "bold_lead": "", "links": []})
            i += 1
            continue
        if re.match(r"^</?(?:details|summary|toggle|columns?|page|database)[^>]*>", line):
            inner = re.sub(r"</?(?:details|summary|toggle|columns?|page|database)[^>]*>", "", line).strip()
            if inner:
                add_para(inner)
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            runs, links = md_inline_runs(m.group(2))
            b = make_block({"type": "h%d" % len(m.group(1)), "runs": runs, "links": links})
            blocks.append(b)
            i += 1
            continue
        if re.match(r"^(?:-{3,}|\*{3,}|_{3,})$", line):
            blocks.append({"type": "hr", "kind": "divider", "text": "", "words": 0, "bold_words": 0,
                           "bold_runs": 0, "starts_bold": False, "bold_lead": "", "links": []})
            i += 1
            continue
        if line.startswith("<callout"):
            buf = []
            while i < n:
                buf.append(lines[i])
                if "</callout>" in lines[i]:
                    i += 1
                    break
                i += 1
            content = re.sub(r"</?callout[^>]*>", "", " ".join(buf))
            add_para(content, "callout")
            continue
        if line.startswith("<table"):
            buf = []
            while i < n:
                buf.append(lines[i])
                if "</table>" in lines[i]:
                    i += 1
                    break
                i += 1
            tbl = "\n".join(buf)
            rows = []
            header = bool(re.search(r"header-row=\"true\"|<th", tbl))
            for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, flags=re.S):
                cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, flags=re.S)
                rows.append([norm_space("".join(r for r, _ in md_inline_runs(c)[0])) for c in cells])
            links = []
            for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tbl, flags=re.S):
                links += md_inline_runs(c)[1]
            text = " ".join(" ".join(r) for r in rows)
            blocks.append({"type": "table", "kind": "table", "text": text, "words": len(words_of(text)),
                           "bold_words": 0, "bold_runs": 0, "starts_bold": False, "bold_lead": "",
                           "links": links, "rows": rows, "header_row": header, "borders": True})
            continue
        if line.startswith("|"):
            rows, links = [], []
            while i < n and lines[i].strip().startswith("|"):
                row = lines[i].strip().strip("|")
                if not re.match(r"^[\s:|-]+$", row):
                    cells = [c.strip() for c in row.split("|")]
                    parsed = [md_inline_runs(c) for c in cells]
                    rows.append([norm_space("".join(r for r, _ in p[0])) for p in parsed])
                    for p in parsed:
                        links += p[1]
                i += 1
            text = " ".join(" ".join(r) for r in rows)
            blocks.append({"type": "table", "kind": "table", "text": text, "words": len(words_of(text)),
                           "bold_words": 0, "bold_runs": 0, "starts_bold": False, "bold_lead": "",
                           "links": links, "rows": rows, "header_row": True, "borders": True})
            continue
        if re.match(r"^(?:[-*+]|\d+[.)])\s+", line):
            ordered = bool(re.match(r"^\d+[.)]\s+", line))
            items, runs_all, links_all = [], [], []
            while i < n and re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", lines[i]):
                item = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", lines[i])
                runs, links = md_inline_runs(item)
                itext, _, ibold, _, ilead = runs_info(runs)
                items.append({"text": itext, "starts_bold": ibold, "bold_lead": ilead})
                runs_all += runs + [(" ", False)]
                links_all += links
                i += 1
            b = make_block({"type": "ol" if ordered else "ul", "runs": runs_all, "links": links_all,
                            "items": [], "rows": []})
            b["items"] = items
            blocks.append(b)
            continue
        if line.startswith(">"):
            add_para(line.lstrip("> ").strip(), "callout")
            i += 1
            continue
        add_para(line)
        i += 1
    return blocks


def text_from_markdown(md):
    out = []
    for line in md.splitlines():
        s = line.strip()
        if re.match(r"^<empty-block\s*/?>$", s):
            out.append("")
            continue
        if re.match(r"^(?:-{3,}|\*{3,}|_{3,})$", s):
            out.append("")
            continue
        s = re.sub(r"^#{1,6}\s+", "", s)
        bullet = ""
        m = re.match(r"^((?:[-*+])|\d+[.)])\s+", s)
        if m:
            bullet = "* " if not m.group(1)[0].isdigit() else m.group(1) + " "
            s = s[m.end():]
        if s.startswith(">"):
            s = s.lstrip("> ")
        s = s.replace("</td>", "\t").replace("</th>", "\t")
        runs, _ = md_inline_runs(s)
        out.append(bullet + "".join(r for r, _ in runs))
    return "\n".join(out)


def blocks_from_text(t):
    blocks = []
    for line in t.splitlines():
        s = line.strip()
        runs = [(s, False)]
        b = make_block({"type": "p", "runs": runs, "links": []})
        if s.startswith("* ") or re.match(r"^\d+[.)]\s", s) or s.startswith("\u25cf"):
            b["kind"] = "list"
            b["items"] = [{"text": s, "starts_bold": False, "bold_lead": ""}]
        elif "\t" in line:
            b["kind"] = "table"
        blocks.append(b)
    return blocks


# ---------------------------------------------------------------------------
# Measurements
# ---------------------------------------------------------------------------

def find_all(patterns, text, flags=re.I, label=None):
    hits = []
    for p in patterns:
        for m in re.finditer(p, text, flags):
            h = loc(text, m.start(), m.end())
            h["match"] = m.group(0)
            if label:
                h["label"] = label
            h["sentence"] = sentence_at(text, m.start())
            hits.append(h)
    hits.sort(key=lambda x: (x["line"], x["column"]))
    return hits


def split_seo(t):
    """Return (body_text, seo_text). The SEO metadata block is not counted as body."""
    lines = t.splitlines()
    nonempty = [i for i, l in enumerate(lines) if l.strip()]
    start = None
    for i, l in enumerate(lines):
        if re.match(r"^\s*(?:\*\*)?\s*(?:SEO Metadata|SEO Title|Title Tag|Meta Title|Meta Description)\b", l, re.I):
            start = i
            break
    if start is None:
        return t, ""
    position = nonempty.index(start) / max(1, len(nonempty)) if start in nonempty else 1
    if position >= 0.5:
        return "\n".join(lines[:start]), "\n".join(lines[start:])
    label = re.compile(r"^\s*(?:\*\*)?\s*(?:" + SEO_LABELS + r")\b", re.I)
    end = start
    while end < len(lines) and (not lines[end].strip() or label.match(lines[end]) or "\t" in lines[end]):
        end += 1
    return "\n".join(lines[:start] + lines[end:]), "\n".join(lines[start:end])


def seo_fields(seo_text, full_text):
    src = seo_text or full_text
    fields = {}
    for key, pat in [("title", r"(?:SEO Title|Title Tag|Meta Title)"), ("meta_description", r"Meta Description"),
                     ("slug", r"(?:URL Slug|Slug)")]:
        m = re.search(r"(?im)^\s*(?:\*\*)?\s*" + pat + r"\s*(?:\*\*)?\s*[:\t]\s*(?:\*\*)?\s*(.+?)\s*$", src)
        if m:
            fields[key] = m.group(1).strip().strip("*").strip()
    return fields


def clean_body(body):
    body = re.sub(r"(?im)^.*\[IMAGE SUGGESTED\].*$", "", body)
    body = re.sub(r"\[(?:VERIFY|FRESHNESS_FLAG)[^\]]*\]", "", body)
    return body


def readability(body, grade_target=6, grade_ceiling=7):
    words = words_of(body)
    sents = sentences_of(body)
    lens = [len(s.split()) for s in sents]
    n_w, n_s = len(words), len(sents)
    fk = (0.39 * (n_w / max(1, n_s)) + 11.8 * (sum(syllables(w) for w in words) / max(1, n_w)) - 15.59) if n_w else 0.0
    out = {
        "words": n_w,
        "sentences": n_s,
        "average_sentence_words": round(statistics.mean(lens), 1) if lens else 0,
        "share_of_sentences_over_20_words": round(sum(l > 20 for l in lens) / len(lens), 2) if lens else 0,
        "sentence_length_spread_stdev": round(statistics.pstdev(lens), 1) if lens else 0,
        "flesch_kincaid_grade_script": round(fk, 1),
        "flesch_kincaid_grade_textstat": None,
    }
    if textstat is not None and n_w:
        try:
            out["flesch_kincaid_grade_textstat"] = round(float(textstat.flesch_kincaid_grade(body)), 1)
        except Exception:
            pass
    out["grade_used"] = out["flesch_kincaid_grade_textstat"] if out["flesch_kincaid_grade_textstat"] is not None else out["flesch_kincaid_grade_script"]
    out["grade_source"] = "textstat" if out["flesch_kincaid_grade_textstat"] is not None else "script formula"
    out["grade_target"] = grade_target
    out["grade_ceiling"] = grade_ceiling
    out["grade_over_target"] = out["grade_used"] > grade_target
    out["grade_over_ceiling_blocker"] = out["grade_used"] > grade_ceiling
    out["long_sentences"] = [{"words": l, "sentence": s} for s, l in zip(sents, lens) if l > 20]
    # repeated openings
    firsts = [re.sub(r"[^\w']", "", s.split()[0]).lower() for s in sents if s.split()]
    runs, i = [], 0
    while i < len(firsts):
        j = i
        while j + 1 < len(firsts) and firsts[j + 1] == firsts[i] and firsts[i]:
            j += 1
        if j - i + 1 >= 3:
            runs.append({"word": firsts[i], "in_a_row": j - i + 1, "first_sentence": sents[i]})
        i = j + 1
    out["repeated_sentence_openings"] = runs
    out["sentences_opening_with_this"] = sum(1 for f in firsts if f == "this")
    return out


def sections_from_blocks(blocks):
    sections = []
    cur = {"title": "(before the first H2)", "level": 0, "blocks": []}
    for b in blocks:
        if b.get("kind") == "heading" and b.get("level") == 2:
            sections.append(cur)
            cur = {"title": b["text"], "level": 2, "blocks": []}
        else:
            cur["blocks"].append(b)
    sections.append(cur)
    return sections


def is_visual(b):
    return b.get("kind") in ("list", "table", "callout", "bold_line")


def structure_report(blocks, has_structure, seo_text):
    rep = {}
    headings = [{"level": b["level"], "text": b["text"]} for b in blocks if b.get("kind") == "heading"]
    rep["structure_available"] = has_structure
    rep["headings"] = headings
    rep["h1_count"] = sum(1 for h in headings if h["level"] == 1)
    not_title = []
    for h in headings:
        if h["level"] in (2, 3):
            ws = re.findall(r"[A-Za-z][\w'\u2019-]*", h["text"])
            low = [w for k, w in enumerate(ws) if w[0].islower() and (k == 0 or w.lower() not in SMALL_WORDS)]
            if low:
                not_title.append({"heading": h["text"], "lowercase_words": low})
    rep["headings_not_in_title_case"] = not_title
    rep["paragraphs_fully_bold_maybe_fake_headings"] = [b["text"] for b in blocks if b.get("kind") == "bold_line" and not re.search(r"[.!?:]$", b["text"])]

    # body blocks: drop the SEO block
    body_blocks = []
    in_seo = False
    for b in blocks:
        if re.match(r"^(?:SEO Metadata|SEO Title|Title Tag|Meta Title)\b", b.get("text", ""), re.I):
            in_seo = True
        if in_seo:
            if b.get("kind") == "heading" and not re.search(r"SEO", b["text"], re.I):
                in_seo = False
            else:
                continue
        body_blocks.append(b)

    sections = sections_from_blocks(body_blocks)
    total = 0
    sec_out = []
    longest = {"words": 0, "section": None, "starts_with": ""}
    for s in sections:
        words = 0
        visuals = 0
        stretch, stretch_start = 0, ""
        bold_phrases = 0
        bold_label_lists = 0
        for b in s["blocks"]:
            k = b.get("kind")
            if k in ("empty", "divider", "heading") and k != "heading":
                continue
            if k == "callout" and "IMAGE SUGGESTED" in b.get("text", ""):
                continue
            w = len(words_of(re.sub(r"\[(?:VERIFY|FRESHNESS_FLAG)[^\]]*\]", "", b.get("text", ""))))
            if k != "heading":
                words += w
            bold_phrases += b.get("bold_runs", 0)
            if k == "list" and b.get("items") and len(b["items"]) >= 2 and all(it.get("starts_bold") for it in b["items"]):
                bold_label_lists += 1
            if is_visual(b):
                visuals += 1
                stretch = 0
            elif k == "paragraph":
                if stretch == 0:
                    stretch_start = b["text"][:70]
                stretch += w
                if stretch > longest["words"]:
                    longest = {"words": stretch, "section": s["title"], "starts_with": stretch_start}
        total += words
        sec_out.append({"title": s["title"], "words": words, "visual_elements": visuals,
                        "bold_phrases": bold_phrases, "lists_where_every_item_starts_with_a_bold_label": bold_label_lists})
    real = [s for s in sec_out if s["title"] != "(before the first H2)" or s["words"]]
    for s in sec_out:
        s["share_of_body"] = round(s["words"] / total, 3) if total else 0
    h2_secs = [s for s in sec_out if s["title"] != "(before the first H2)"]
    avg = statistics.mean([s["words"] for s in h2_secs]) if h2_secs else 0
    rep["sections"] = real
    rep["average_h2_section_words"] = round(avg, 1)
    rep["h2_sections_under_half_the_average"] = [s["title"] for s in h2_secs if avg and s["words"] < avg / 2]
    rep["h2_sections_with_no_visual_element"] = [s["title"] for s in h2_secs if s["visual_elements"] == 0] if has_structure else None
    rep["longest_stretch_without_visual_element"] = longest if has_structure else None

    # paragraph lengths (Dimension 12)
    faq_titles = {s["title"] for s in h2_secs if FAQ_RE.search(s["title"])}
    long_paras = []
    para_words = []
    for s in sections:
        for b in s["blocks"]:
            if b.get("kind") != "paragraph":
                continue
            t = re.sub(r"\[(?:VERIFY|FRESHNESS_FLAG)[^\]]*\]", "", b["text"])
            n_w = len(t.split())
            n_s = len([x for x in re.split(r"(?<=[.!?])\s+", t) if x.strip()])
            para_words.append(n_w)
            if n_s > 3 or n_w > 50:
                long_paras.append({"section": s["title"], "sentences": n_s, "words": n_w,
                                   "over_60_words": n_w > 60, "in_faq": s["title"] in faq_titles,
                                   "starts_with": t[:70]})
    rep["long_paragraphs"] = long_paras
    rep["paragraph_words_average"] = round(statistics.mean(para_words), 1) if para_words else 0
    rep["paragraph_words_spread_stdev"] = round(statistics.pstdev(para_words), 1) if para_words else 0

    # FAQ (Dimensions 12 and 20)
    faq = None
    for idx, s in enumerate(h2_secs):
        if FAQ_RE.search(s["title"]):
            sec = next(x for x in sections if x["title"] == s["title"])
            qs = []
            cur_q = None
            for b in sec["blocks"]:
                if (b.get("kind") == "heading" and b.get("level", 9) >= 3) or (b.get("kind") in ("bold_line", "paragraph") and b["text"].endswith("?")):
                    cur_q = {"question": b["text"], "answer_words": 0}
                    qs.append(cur_q)
                elif cur_q is not None and b.get("kind") in ("paragraph", "list"):
                    cur_q["answer_words"] += b.get("words", 0)
            faq = {"title": s["title"], "is_last_section": idx == len(h2_secs) - 1,
                   "questions": len(qs), "answers_outside_40_to_60_words":
                   [q for q in qs if not 40 <= q["answer_words"] <= 60], "items": qs}
    rep["faq"] = faq

    # tables (Dimensions 9 and 19)
    rep["tables"] = [{"rows": len(b.get("rows", [])), "columns": max((len(r) for r in b.get("rows", [])), default=0),
                      "header_row": b.get("header_row"), "borders_detected": b.get("borders"),
                      "empty_cells": sum(1 for r in b.get("rows", []) for c in r if not c.strip()),
                      "first_row": b.get("rows", [[]])[0] if b.get("rows") else []}
                     for b in blocks if b.get("kind") == "table" and b.get("type") == "table"]
    return rep, body_blocks, sections


def spacing_report(blocks, source):
    """Dimension 19: exactly one empty paragraph between blocks (Drive). Notion spaces blocks itself."""
    problems = []
    pairs = 0
    if source == "html":
        for prev, cur in zip(blocks, blocks[1:]):
            pe, ce = prev.get("kind") == "empty", cur.get("kind") == "empty"
            if pe and ce:
                problems.append({"problem": "two empty paragraphs in a row", "near": ""})
                continue
            if pe or ce:
                continue
            pairs += 1
            if cur.get("kind") == "heading" and cur.get("level", 1) >= 2:
                problems.append({"problem": "no empty paragraph before a heading", "near": cur["text"][:60]})
            elif prev.get("kind") == "heading":
                continue
            else:
                what = "two paragraphs with no space between" if prev.get("kind") == cur.get("kind") == "paragraph" else \
                    "no empty paragraph between a %s and a %s" % (prev.get("kind"), cur.get("kind"))
                problems.append({"problem": what, "near": cur.get("text", "")[:60]})
        note = "Drive: one empty spacer paragraph between blocks, never two in a row."
    elif source == "markdown":
        run = 0
        for b in blocks:
            if b.get("kind") == "empty":
                run += 1
                if run == 2:
                    problems.append({"problem": "two empty blocks in a row", "near": ""})
            else:
                run = 0
        note = "Notion: blocks are spaced by Notion itself; only repeated empty blocks are flagged."
    else:
        return {"checked": False, "note": "No HTML or Markdown export given, so spacing was not measured."}
    gaps = sum(1 for p in problems if p["problem"] != "two empty paragraphs in a row" and p["problem"] != "two empty blocks in a row")
    return {"checked": True, "note": note, "problems": problems, "problem_count": len(problems),
            "missing_space_share": round(gaps / pairs, 2) if pairs else 0,
            "broken_throughout": bool(pairs) and gaps / pairs > 0.25}


def links_report(blocks, t, site, check):
    links = []
    for b in blocks:
        for l in b.get("links", []):
            links.append({"url": l["href"], "anchor": l["text"]})
    site_host = urllib.parse.urlparse(site).netloc.lower().removeprefix("www.") if site else ""
    for l in links:
        host = urllib.parse.urlparse(l["url"]).netloc.lower().removeprefix("www.")
        if not host:
            l["type"] = "internal" if l["url"].startswith("/") else "other"
        elif site_host and (host == site_host or host.endswith("." + site_host)):
            l["type"] = "internal"
        else:
            l["type"] = "external" if site_host else "unknown (no --site given)"
        l["weak_anchor_text"] = l["anchor"].lower().strip(" .") in BAD_ANCHORS
        l["status"] = None
    if check:
        for l in links:
            if not l["url"].startswith("http"):
                continue
            l["status"] = fetch_status(l["url"])
    hrefs = {l["url"] for l in links}
    bare = []
    for m in re.finditer(r"https?://[^\s<>\")\]]+", t):
        u = m.group(0).rstrip(".,;")
        if u not in hrefs:
            h = loc(t, m.start(), m.end())
            h["url"] = u
            bare.append(h)
    return {"count": len(links), "internal": sum(1 for l in links if l["type"] == "internal"),
            "external": sum(1 for l in links if l["type"] == "external"), "links": links,
            "bare_urls_in_text_not_clickable": bare,
            "checked": check, "note": None if check else "Links were not fetched. Run with --check-links, or fetch each one."}


def fetch_status(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": "Mozilla/5.0 (content-machine QA link check)"})
            with urllib.request.urlopen(req, timeout=12) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 400, 404, 429, 501):
                continue
            return e.code
        except Exception as e:  # network error
            if method == "GET":
                return "error: %s" % type(e).__name__
    return None


def keyword_report(kw, t, body, blocks, sections, seo, words_total):
    rx = kw_regex(kw)
    if rx is None:
        return None
    rep = {"keyword": kw}
    h1 = next((b["text"] for b in blocks if b.get("kind") == "heading" and b.get("level") == 1), None)
    if h1 is None:
        h1 = next((l.strip() for l in t.splitlines() if l.strip()), "")
        rep["h1_found_by"] = "first line of the text (no heading structure given)"
    rep["h1"] = h1
    rep["in_h1"] = bool(rx.search(h1 or ""))
    # first paragraph and first 100 words after the H1
    after = []
    first_para = None
    seen_h1 = False
    for b in blocks:
        if b.get("kind") == "heading" and b.get("level") == 1 and not seen_h1:
            seen_h1 = True
            continue
        if b.get("text") == h1 and not seen_h1:
            seen_h1 = True
            continue
        if b.get("kind") in ("paragraph", "bold_line", "list") and b.get("text"):
            if first_para is None:
                first_para = b["text"]
            after.append(b["text"])
            if len(" ".join(after).split()) >= 100:
                break
    first100 = " ".join(" ".join(after).split()[:100])
    rep["first_paragraph"] = (first_para or "")[:200]
    rep["in_first_paragraph"] = bool(rx.search(first_para or ""))
    rep["in_first_100_words"] = bool(rx.search(first100))
    h2s = [b["text"] for b in blocks if b.get("kind") == "heading" and b.get("level") == 2]
    rep["h2s_with_keyword"] = [h for h in h2s if rx.search(h)]
    count = len(rx.findall(body))
    rep["body_occurrences"] = count
    n_kw = len(kw.split())
    rep["density_percent_occurrences"] = round(100 * count / words_total, 2) if words_total else 0
    rep["density_percent_keyword_words"] = round(100 * count * n_kw / words_total, 2) if words_total else 0
    rep["density_note"] = "Two methods: occurrences per 100 words, and keyword words as a share of all words."
    conc = None
    for s in sections:
        if s["title"] and CONCLUSION_RE.search(s["title"]) and not FAQ_RE.search(s["title"]):
            conc = s
    if conc is None:
        non_faq = [s for s in sections if s["title"] != "(before the first H2)" and not FAQ_RE.search(s["title"])]
        conc = non_faq[-1] if non_faq else None
    if conc is not None:
        ctext = " ".join(b.get("text", "") for b in conc["blocks"])
        rep["conclusion_section"] = conc["title"]
        rep["in_conclusion"] = bool(rx.search(ctext))
    else:
        tail = " ".join(body.split()[-150:])
        rep["conclusion_section"] = "(last 150 words; no headings given)"
        rep["in_conclusion"] = bool(rx.search(tail))
    # SEO block
    title = seo.get("title")
    if title is not None:
        m = rx.search(title)
        start_word = len(title[:m.start()].split()) if m else None
        rep["seo_title"] = {"text": title, "characters": len(title), "in_50_to_60": 50 <= len(title) <= 60,
                            "has_keyword": bool(m), "keyword_starts_at_word": (start_word + 1) if m else None,
                            "keyword_in_first_5_words": bool(m) and start_word < 5}
    else:
        rep["seo_title"] = None
    md = seo.get("meta_description")
    if md is not None:
        kw_words = [w for w in kw.lower().split() if w not in SLUG_STOP_WORDS]
        rep["meta_description"] = {"text": md, "characters": len(md), "in_140_to_155": 140 <= len(md) <= 155,
                                   "has_keyword": bool(rx.search(md)),
                                   "has_all_keyword_words": all(w in md.lower() for w in kw_words)}
    else:
        rep["meta_description"] = None
    slug = seo.get("slug")
    if slug is not None:
        sl = slug.strip().strip("/").split("/")[-1].lower()
        parts = [p for p in re.split(r"[-_]", sl) if p]
        kw_words = [w for w in re.split(r"[\s-]+", kw.lower()) if w not in SLUG_STOP_WORDS]
        rep["slug"] = {"text": slug, "has_keyword_words": all(w in parts or w.rstrip("s") in parts for w in kw_words),
                       "stop_words": [p for p in parts if p in SLUG_STOP_WORDS]}
    else:
        rep["slug"] = None
    return rep


def measure(text=None, html_src=None, md_src=None, keyword=None, target_words=None, spelling="US",
            site=None, banned=None, check_links=False, grade_target=6, grade_ceiling=7):
    if text is None and md_src is not None:
        text = text_from_markdown(md_src)
        text_source = "derived from the Markdown"
    else:
        text_source = "plain-text export"
    t = text or ""
    report = {"tool": "content-machine measure.py", "text_source": text_source,
              "textstat_available": textstat is not None}

    # 1. Characters that must never appear (Dimensions 14 and 19)
    chars = []
    counts = {}
    for ch, name in BANNED_CHARS.items():
        for m in re.finditer(re.escape(ch), t):
            h = loc(t, m.start())
            h["character"] = name
            chars.append(h)
            counts[name] = counts.get(name, 0) + 1
    for pat, name in [(r"\s--\s|\w--\w", "double hyphen used as a dash"),
                      (r"[\U0001F000-\U0001FAFF\u2600-\u27bf\u2b00-\u2bff\ufe0f]", "emoji"),
                      (r"\u00c3.|\u00e2\u20ac|\u00f0\S|\u00c2\S", "garbled character (encoding)")]:
        for m in re.finditer(pat, t):
            h = loc(t, m.start(), m.end())
            h["character"] = name
            chars.append(h)
            counts[name] = counts.get(name, 0) + 1
    chars.sort(key=lambda x: (x["line"], x["column"]))
    report["banned_characters"] = {"em_dash_count": counts.get("em dash", 0), "counts": counts, "hits": chars}

    # punctuation rules (Dimension 14)
    body_raw, seo_text = split_seo(t)
    body = clean_body(body_raw)
    report["punctuation"] = {
        "semicolons": find_all([r";"], body),
        "three_dot_ellipsis": find_all([r"\.\.\."], t),
        "exclamation_marks": find_all([r"!"], body),
        "arrows": find_all([r"\u2192|->"], t),
    }
    report["punctuation"]["exclamation_count"] = len(report["punctuation"]["exclamation_marks"])
    report["punctuation"]["exclamation_over_2"] = report["punctuation"]["exclamation_count"] > 2

    # 2. Markdown or HTML left raw in the document (Dimension 19)
    raw = []
    for pat, name in [(r"\]\(https?://", "raw Markdown link"), (r"\\\[|\\\]|\\_|\\\*|\\#", "backslash-escaped character"),
                      (r"\*\*", "raw bold markers"), (r"(?m)^#{1,6} ", "raw heading marker"),
                      (r"(?m)^\s*-{3,}\s*$|\\-{3,}|^\s*\*{3,}\s*$", "raw divider"),
                      (r"&nbsp;|&#\d+;|&#x[0-9a-fA-F]+;|&amp;|&lt;|&gt;|&quot;", "HTML entity shown as text"),
                      (r"(?m)^>\s", "raw blockquote marker"), (r"</?(?:p|span|div|strong|br|h[1-6]|a)\b[^>]*>", "HTML tag shown as text")]:
        for m in re.finditer(pat, t):
            h = loc(t, m.start(), m.end())
            h["problem"] = name
            raw.append(h)
    raw.sort(key=lambda x: (x["line"], x["column"]))
    report["raw_markup_in_text"] = {"count": len(raw), "hits": raw}

    # structure
    if html_src is not None:
        blocks, source = blocks_from_html(html_src), "html"
    elif md_src is not None:
        blocks, source = blocks_from_markdown(md_src), "markdown"
    else:
        blocks, source = blocks_from_text(t), "text"
    has_structure = source != "text"
    report["structure_source"] = source

    # 3. Spacing (Dimension 19)
    report["spacing"] = spacing_report(blocks, source)

    # 4. Words, sentences, reading level (Dimensions 17, 18)
    rd = readability(body, grade_target, grade_ceiling)
    report["reading"] = rd
    if target_words:
        pct = round(100 * rd["words"] / target_words, 1)
        report["length"] = {"words": rd["words"], "target": target_words, "percent_of_target": pct,
                            "within_10_percent": 90 <= pct <= 110,
                            "more_than_10_percent_under": pct < 90, "more_than_10_percent_over": pct > 110}
    else:
        report["length"] = {"words": rd["words"], "target": None}

    # 5. Paragraphs, sections, visuals, FAQ, tables (Dimensions 9, 12, 17, 20)
    srep, body_blocks, sections = structure_report(blocks, has_structure, seo_text)
    report["structure"] = srep

    # 6. Pipeline tags (Dimensions 10, 15)
    report["tags"] = {
        "verify": find_all([r"\[VERIFY[^\]]*\]"], t, flags=0),
        "freshness_flag": find_all([r"\[FRESHNESS_FLAG[^\]]*\]"], t, flags=0),
        "image_suggested": len(re.findall(r"\[IMAGE SUGGESTED\]", t)),
    }
    report["tags"]["verify_count"] = len(report["tags"]["verify"])
    report["tags"]["freshness_count"] = len(report["tags"]["freshness_flag"])

    # Dimension 13: AI-tell words and phrases
    word_hits = find_all([r"\b" + w + r"\b" for w in AI_WORDS], body, label="word")
    phrase_hits = find_all(AI_PHRASES, body, label="phrase") + find_all([r"(?:^|(?<=[.!?]\s))" + o for o in AI_OPENERS], body, flags=0, label="phrase")
    banned_hits = []
    if banned:
        banned_hits = find_all([r"(?<!\w)" + re.escape(b) + r"(?!\w)" for b in banned], t, label="banned outright")
    total_hits = len(word_hits) + len(phrase_hits)
    per300 = round(total_hits / (rd["words"] / 300), 2) if rd["words"] else 0
    report["ai_tells_words_and_phrases"] = {
        "hit_count": total_hits, "hits_per_300_words": per300, "over_1_per_300_words": per300 > 1,
        "words": word_hits, "phrases": phrase_hits,
        "banned_outright_hits": banned_hits,
        "note": "Each word or phrase hit is a flag to review in context. Banned-outright hits fail on any use.",
    }
    # Dimension 23: structure tells
    st = {}
    for name, pats in STRUCTURE_PATTERNS.items():
        flags = 0 if name in ("chat leftover or placeholder", "section-ending recap opener") else re.I
        st[name] = find_all(pats, body, flags=flags)
    st["rule of three lists (check each item does work)"] = find_all([r"\b\w+(?: \w+)?, \w+(?: \w+)?,? and \w+(?: \w+)?\b"], body, flags=0)
    st["repeated sentence openings"] = rd["repeated_sentence_openings"]
    st["sentences opening with This"] = rd["sentences_opening_with_this"]
    st["counts"] = {k: (len(v) if isinstance(v, list) else v) for k, v in st.items()}
    report["ai_tells_structure"] = st

    # per-section clustering of hits
    if has_structure:
        titles = [s["title"] for s in sections if s["title"] != "(before the first H2)"]
        starts = []
        pos = 0
        lower = body.lower()
        for tt in titles:
            p = lower.find(tt.lower()[:40], pos)
            if p != -1:
                starts.append((p, tt))
                pos = p + 1
        line_starts = [0] + [m.end() for m in re.finditer("\n", body)]

        def sec_of(line):
            off = line_starts[line - 1] if line - 1 < len(line_starts) else len(body)
            name = "(before the first H2)"
            for p, tt in starts:
                if p <= off:
                    name = tt
            return name
        per = {}
        for h in word_hits + phrase_hits:
            s = sec_of(h["line"])
            per[s] = per.get(s, 0) + 1
        report["ai_tells_words_and_phrases"]["hits_per_section"] = per

    # Dimension 15 and 18: vague phrasing and attribution
    report["vague_phrases"] = find_all([r"\b" + p + r"\b" for p in VAGUE_PHRASES], body)
    report["vague_attribution"] = find_all([r"\b" + p + r"\b" for p in VAGUE_ATTRIBUTION], body)
    report["narrated_citations"] = find_all([r"\baccording to\b"], body)

    # Dimension 16: date anchors
    anchors, taken = [], []
    for kind, pat in DATE_ANCHORS:
        for m in re.finditer(pat, body, re.I if kind != "bare year" else 0):
            if any(a <= m.start() < b for a, b in taken):
                continue
            taken.append((m.start(), m.end()))
            h = loc(body, m.start(), m.end())
            h.update({"kind": kind, "match": m.group(0), "sentence": sentence_at(body, m.start())})
            anchors.append(h)
    anchors.sort(key=lambda x: (x["line"], x["column"]))
    report["date_anchors"] = anchors

    # spelling
    sp = (spelling or "US").upper()
    pats = UK_TO_US_FLAGS if sp == "US" else US_TO_UK_FLAGS
    report["spelling"] = {"standard": sp, "other_spelling_hits": find_all([r"\b" + p + r"\b" for p in pats], body)}

    # links (Dimensions 2, 15, 19)
    report["links"] = links_report(blocks, t, site, check_links)

    # keyword placement (Dimension 1)
    seo = seo_fields(seo_text, t)
    report["seo_block"] = {"found": bool(seo_text) or bool(seo), "fields": seo}
    report["keyword"] = keyword_report(keyword, t, body, body_blocks, sections, seo, rd["words"]) if keyword else None

    # images (Dimension 10)
    n_img = report["tags"]["image_suggested"]
    report["images"] = {"image_suggestions": n_img, "piece_over_1500_words": rd["words"] > 1500,
                        "in_2_to_6": 2 <= n_img <= 6}

    # blocker candidates for the judge (shared/base-rules/qa.md, Blockers)
    cands = []
    if counts.get("em dash"):
        cands.append("em dash: %d found" % counts["em dash"])
    if report["length"].get("more_than_10_percent_under"):
        cands.append("word count more than 10 percent under the target (check the writer notes for a reason)")
    if rd["grade_over_ceiling_blocker"]:
        cands.append("reading level above the grade ceiling: grade %g, ceiling %g" % (rd["grade_used"], grade_ceiling))
    if keyword and report["keyword"] and (not report["keyword"]["in_h1"] or not report["keyword"]["in_first_paragraph"]):
        cands.append("primary keyword missing from the H1 or the first paragraph")
    garbled = counts.get("garbled character (encoding)", 0) + counts.get("replacement character (garbled text)", 0)
    if garbled or report["raw_markup_in_text"]["count"] or report["spacing"].get("broken_throughout"):
        cands.append("rendering problems: %d garbled, %d raw markup, spacing broken throughout: %s"
                     % (garbled, report["raw_markup_in_text"]["count"], bool(report["spacing"].get("broken_throughout"))))
    if check_links:
        dead = [l["url"] for l in report["links"]["links"] if isinstance(l["status"], str) or (isinstance(l["status"], int) and l["status"] >= 400)]
        if dead:
            cands.append("links that did not resolve: " + ", ".join(dead))
    report["blocker_candidates"] = cands
    report["summary"] = {
        "words": rd["words"], "target_words": target_words, "reading_grade": rd["grade_used"],
        "grade_target": grade_target, "grade_ceiling": grade_ceiling,
        "average_sentence_words": rd["average_sentence_words"], "em_dashes": counts.get("em dash", 0),
        "ai_tell_hits": total_hits, "open_verify_tags": report["tags"]["verify_count"],
        "spacing_and_rendering_problems": report["spacing"].get("problem_count", 0) + report["raw_markup_in_text"]["count"] + garbled,
    }
    return report


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

SAMPLE_HTML = """<html><head><meta charset="utf-8"><style>.c1{font-weight:700}.c2{border-top-width:1pt;border-top-style:solid}</style></head><body>
<h1>How to Sell Courses Online</h1>
<p>&nbsp;</p>
<p>Want to sell courses online? This guide shows you how to sell courses online in five steps.</p>
<p>&nbsp;</p>
<h2>Pick a Topic People Pay For</h2>
<p>&nbsp;</p>
<p>Start with a skill you know well. Ask ten past clients what they would pay to learn.</p>
<p>It's a crucial step \u2014 skip it and you guess.</p>
<p>&nbsp;</p>
<ul><li><span class="c1">Check demand:</span> search the topic.</li><li><span class="c1">Check price:</span> look at rivals.</li></ul>
<p>&nbsp;</p>
<table border="1"><tr><td class="c2"><span class="c1">Plan</span></td><td class="c2"><span class="c1">Price</span></td></tr><tr><td class="c2">Basic</td><td class="c2">$29</td></tr></table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2>Conclusion</h2>
<p>&nbsp;</p>
<p>Now you know how to sell courses online. As of March 2025, prices start at $29. Read our <a href="https://www.google.com/url?q=https://example.com/pricing&amp;sa=D">pricing guide</a>.</p>
<p>&nbsp;</p>
<p><span class="c1">SEO Title:</span> How to Sell Courses Online: A Simple 5-Step Guide</p>
<p>Meta Description: Learn how to sell courses online with five simple steps.</p>
<p>URL Slug: how-to-sell-courses-online</p>
</body></html>"""

SAMPLE_MD = """# How to Sell Courses Online

Want to sell courses online? This guide shows you how to sell courses online in five steps.

## Pick a Topic People Pay For

Start with a skill you know well. Ask ten past clients what they would pay to learn.

It's a crucial step \u2014 skip it and you guess. Here is a \\*\\*literal\\*\\* marker.

- **Check demand:** search the topic.
- **Check price:** look at rivals.

<empty-block/>
<empty-block/>

## Conclusion

Now you know how to sell courses online. Read our [pricing guide](https://example.com/pricing). [VERIFY: price]
"""


def self_test():
    text = re.sub(r"<[^>]+>", "\n", SAMPLE_HTML.split("<body>")[1])
    text = htmllib.unescape(text).replace("\xa0", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    r = measure(text=text, html_src=SAMPLE_HTML, keyword="sell courses online", target_words=100,
                spelling="US", site="https://example.com", banned=["skip it"])
    json.dumps(r)
    assert r["banned_characters"]["em_dash_count"] == 1, r["banned_characters"]
    assert r["reading"]["words"] > 20
    assert r["keyword"]["in_h1"] and r["keyword"]["in_first_paragraph"], r["keyword"]
    assert r["keyword"]["seo_title"]["has_keyword"]
    assert r["spacing"]["checked"] and r["spacing"]["problem_count"] >= 2, r["spacing"]
    assert any(p["problem"] == "two empty paragraphs in a row" for p in r["spacing"]["problems"])
    assert r["links"]["internal"] == 1, r["links"]
    assert r["date_anchors"], "date anchor not found"
    assert r["ai_tells_words_and_phrases"]["hit_count"] >= 1
    assert r["ai_tells_words_and_phrases"]["banned_outright_hits"]
    assert r["structure"]["tables"] and r["structure"]["tables"][0]["borders_detected"]
    assert r["structure"]["tables"][0]["header_row"]
    assert len(r["structure"]["headings"]) == 3

    m = measure(md_src=SAMPLE_MD, keyword="sell courses online", target_words=60, spelling="UK")
    json.dumps(m)
    assert m["banned_characters"]["em_dash_count"] == 1
    assert m["raw_markup_in_text"]["count"] >= 1, m["raw_markup_in_text"]
    assert m["spacing"]["problem_count"] == 1, m["spacing"]
    assert m["tags"]["verify_count"] == 1
    assert m["keyword"]["in_h1"] and m["keyword"]["in_conclusion"]
    assert m["structure"]["sections"][1]["lists_where_every_item_starts_with_a_bold_label"] == 1

    # the grade target and ceiling follow the options (a reading-level Exception rule)
    assert r["reading"]["grade_target"] == 6 and r["reading"]["grade_ceiling"] == 7
    low = measure(md_src=SAMPLE_MD, grade_target=-50, grade_ceiling=-49)
    assert low["reading"]["grade_over_target"] and low["reading"]["grade_over_ceiling_blocker"], low["reading"]
    assert any(c.startswith("reading level above the grade ceiling") for c in low["blocker_candidates"])
    high = measure(md_src=SAMPLE_MD, grade_target=50, grade_ceiling=51)
    assert not high["reading"]["grade_over_target"] and not high["reading"]["grade_over_ceiling_blocker"]
    assert not any(c.startswith("reading level") for c in high["blocker_candidates"])
    print(json.dumps({"self_test": "passed", "drive_sample_words": r["reading"]["words"],
                      "notion_sample_words": m["reading"]["words"], "textstat": textstat is not None}))
    return 0


# ---------------------------------------------------------------------------

def read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def main(argv=None):
    ap = argparse.ArgumentParser(description="Content Machine QA measurements (modes/qa.md, Step 1.5).")
    ap.add_argument("text", nargs="?", help="the document's plain-text export")
    ap.add_argument("--html", help="the document's HTML export (Drive)")
    ap.add_argument("--markdown", help="the document's fetched Markdown (Notion)")
    ap.add_argument("--keyword", help="the primary keyword")
    ap.add_argument("--target-words", type=int, help="the brief's target word count")
    ap.add_argument("--spelling", choices=["US", "UK", "us", "uk"], default="US")
    ap.add_argument("--site", help="the product's Website URL, to split internal and external links")
    ap.add_argument("--banned", help="file of words or phrases banned outright, one per line")
    ap.add_argument("--grade-target", type=float, default=6,
                    help="the top of the target reading grade (default 6; a reading-level Exception rule sets it)")
    ap.add_argument("--grade-ceiling", type=float, default=7,
                    help="a reading grade above this is a Blocker (default 7; the top of the target range plus 1)")
    ap.add_argument("--check-links", action="store_true", help="fetch every link and report its status")
    ap.add_argument("--self-test", action="store_true", help="run on a built-in sample and exit")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.text and not a.markdown:
        ap.error("give the plain-text export, or --markdown for a Notion page")
    if a.grade_ceiling < a.grade_target:
        ap.error("--grade-ceiling must be at least --grade-target")
    banned = None
    if a.banned:
        banned = [l.strip() for l in read(a.banned).splitlines() if l.strip() and not l.startswith("#")]
    r = measure(text=read(a.text) if a.text else None,
                html_src=read(a.html) if a.html else None,
                md_src=read(a.markdown) if a.markdown else None,
                keyword=a.keyword, target_words=a.target_words, spelling=a.spelling.upper(),
                site=a.site, banned=banned, check_links=a.check_links,
                grade_target=a.grade_target, grade_ceiling=a.grade_ceiling)
    json.dump(r, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

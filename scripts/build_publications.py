#!/usr/bin/env python3
"""Generate the publications data file from the lab BibTeX file.

Reads ``_bibliography/publications.bib`` and writes ``_data/publications.yml``
(refereed papers, journal articles, and book chapters from the SMCClab era).

Performances are NOT sourced from here: the bib does not catalogue the lab's
recent concerts and installations, so ``_data/performances.yml`` is curated by
hand from blog posts and event records.

The bib file is the canonical publication list maintained at
https://github.com/cpmpercussion/preprints/blob/main/publications.bib

To refresh the local copy before regenerating:

    curl -sL https://raw.githubusercontent.com/cpmpercussion/preprints/main/publications.bib \
        -o _bibliography/publications.bib

Then run:

    python3 scripts/build_publications.py
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

# Map LaTeX accent commands to Unicode combining marks (applied generically).
ACCENTS = {"^": "̂", "'": "́", "`": "̀", '"': "̈",
           "~": "̃", "=": "̄", ".": "̇", "v": "̌",
           "u": "̆", "c": "̧", "H": "̋"}

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "_bibliography" / "publications.bib"
PUBS_OUT = ROOT / "_data" / "publications.yml"

# Distinctive surnames of lab members/alumni that are safe to match alone.
LAB_TOKENS = {
    "Martin", "Wang", "Niu", "Niyonsenga", "Gelder", "Hunter",
    "Wallace", "Nygaard", "Naess", "Næss", "Rosjo", "Røsjø", "Brustad",
    "Tao", "Proctor", "Zhu",
}

# Short/ambiguous surnames (shared with non-lab co-authors) need the full name.
# e.g. lab member "Sandy Ma" vs collaborator "Junjie Ma"; "Minsik Choi" vs "Woosung Choi".
LAB_FULL_NAMES = {"sandy ma", "minsik choi"}

# Map a venue string to a short, recognisable label. Order matters: first hit wins.
VENUE_MAP = [
    ("New Interfaces for Musical Expression", "NIME"),
    ("Creativity and Cognition", "C&C"),
    ("Creativity & Cognition", "C&C"),
    ("Human Factors in Computing", "CHI"),
    ("CHI Conference", "CHI"),
    ("CHI Extended Abstracts", "CHI EA"),
    ("CHI EA", "CHI EA"),
    ("Acoustics, Speech and Signal Processing", "ICASSP"),
    ("ICASSP", "ICASSP"),
    ("Interspeech", "Interspeech"),
    ("INTERSPEECH", "Interspeech"),
    ("Machine Learning", "ICML"),
    ("Artificial Intelligence", "AAAI"),
    ("Designing Interactive Systems", "DIS"),
    ("Multimedia", "ACM MM"),
    ("Frontiers", "Frontiers"),
    ("Audio Mostly", "Audio Mostly"),
    ("International Computer Music Conference", "ICMC"),
    ("Australasian Computer Music", "ACMC"),
    ("Sound and Music Computing", "SMC"),
    ("TENOR", "TENOR"),
    ("OzCHI", "OzCHI"),
    ("Australian Conference on Human-Computer", "OzCHI"),
    ("Organised Sound", "Organised Sound"),
    ("Journal of New Music Research", "JNMR"),
    ("Computer Music Journal", "CMJ"),
    ("Chroma", "Chroma"),
    ("Leonardo", "Leonardo"),
]

# Venues we treat as flagship (get a highlighted tag on the page).
TOP_VENUES = {"NIME", "CHI", "ICASSP", "Interspeech", "ICML", "AAAI", "C&C", "DIS", "ACM MM"}

# SMCClab began in 2021 (first PhD student recruited Sep 2021). The lab site
# shows lab-era outputs only, not Charles's full career record.
MIN_YEAR = 2021

# LaTeX -> unicode replacements for the accents that actually appear in the bib.
LATEX_CHARS = [
    (r"{\o}", "ø"), (r"\o{}", "ø"), (r"\o ", "ø "),
    (r"{\O}", "Ø"), (r"\O{}", "Ø"),
    (r"{\ae}", "æ"), (r"\ae{}", "æ"), (r"{\AE}", "Æ"),
    (r"{\aa}", "å"), (r"\aa{}", "å"), (r"{\AA}", "Å"),
    (r"{\ss}", "ß"),
    (r'{\"o}', "ö"), (r'\"o', "ö"), (r'{\"a}', "ä"), (r'\"a', "ä"),
    (r'{\"u}', "ü"), (r'\"u', "ü"), (r'{\"O}', "Ö"), (r'{\"U}', "Ü"),
    (r"{\'e}", "é"), (r"\'e", "é"), (r"{\'a}", "á"), (r"\'a", "á"),
    (r"{\'o}", "ó"), (r"{\'\i}", "í"), (r"{\'i}", "í"),
    (r"{\`e}", "è"), (r"{\^e}", "ê"), (r"{\~n}", "ñ"), (r"{\c c}", "ç"),
    (r"\&", "&"),
    (r"---", "—"), (r"--", "–"),
    (r"\%", "%"), (r"~", " "),
]


def clean_tex(value):
    """Turn a raw BibTeX field value into clean display text."""
    if value is None:
        return ""
    text = value
    for src, dst in LATEX_CHARS:
        text = text.replace(src, dst)

    # Generic accents: \^{a}, \^a, \'e, \"{o}, \c{c}, etc. -> composed Unicode.
    def _accent(m):
        base = m.group(2)
        combined = base + ACCENTS[m.group(1)]
        return unicodedata.normalize("NFC", combined)

    accent_cmds = re.escape("".join(ACCENTS))
    text = re.sub(rf"\\([{accent_cmds}])\{{(\w)\}}", _accent, text)
    text = re.sub(rf"\\([{accent_cmds}]) ?(\w)", _accent, text)

    # Drop protective braces like {AI} -> AI, but keep the inner text.
    text = text.replace("{", "").replace("}", "")
    # Remove any stray LaTeX command residue and lone backslashes.
    text = re.sub(r"\\[a-zA-Z]+", "", text).replace("\\", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_entries(bibtext):
    """Yield (entry_type, fields_dict) for each @entry in the bib text."""
    entries = []
    i = 0
    n = len(bibtext)
    while True:
        at = bibtext.find("@", i)
        if at == -1:
            break
        m = re.match(r"@(\w+)\s*\{", bibtext[at:])
        if not m:
            i = at + 1
            continue
        entry_type = m.group(1).lower()
        # Find the matching closing brace for this entry.
        start = at + m.end() - 1  # index of the opening '{'
        depth = 0
        j = start
        while j < n:
            c = bibtext[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        body = bibtext[start + 1:j]
        entries.append((entry_type, parse_fields(body)))
        i = j + 1
    return entries


def parse_fields(body):
    """Parse the inside of one bib entry into {field: value}."""
    fields = {}
    # First token before the first comma is the citekey; skip it.
    _, _, rest = body.partition(",")
    pos = 0
    length = len(rest)
    while pos < length:
        eq = rest.find("=", pos)
        if eq == -1:
            break
        key = rest[pos:eq].strip().strip(",").strip().lower()
        vstart = eq + 1
        # Skip whitespace.
        while vstart < length and rest[vstart] in " \t\r\n":
            vstart += 1
        if vstart >= length:
            break
        ch = rest[vstart]
        if ch == "{":
            depth = 0
            k = vstart
            while k < length:
                if rest[k] == "{":
                    depth += 1
                elif rest[k] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                k += 1
            value = rest[vstart + 1:k]
            pos = k + 1
        elif ch == '"':
            k = vstart + 1
            while k < length and rest[k] != '"':
                k += 1
            value = rest[vstart + 1:k]
            pos = k + 1
        else:
            # Bare value (e.g. year = 2015 or month = nov). Stop at the comma
            # but leave pos ON it so the shared advance below consumes it.
            k = vstart
            while k < length and rest[k] != ",":
                k += 1
            value = rest[vstart:k]
            pos = k
        # Advance past the trailing comma.
        nextcomma = rest.find(",", pos)
        if nextcomma == -1:
            pos = length
        else:
            pos = nextcomma + 1
        if key:
            fields[key] = value.strip()
    return fields


def format_authors(raw):
    """Return an HTML author string, lab members wrapped in <strong>."""
    raw = raw.replace("\n", " ")
    names = re.split(r"\s+and\s+", raw)
    out = []
    for name in names:
        name = name.strip().rstrip(",").strip()
        if not name:
            continue
        if "," in name:
            last, first = name.split(",", 1)
            display = f"{clean_tex(first.strip())} {clean_tex(last.strip())}".strip()
        else:
            display = clean_tex(name)
        tokens = set(re.split(r"[\s\-]+", display))
        is_lab = bool(tokens & LAB_TOKENS) or display.lower() in LAB_FULL_NAMES
        display_html = escape_html(display)
        out.append(f"<strong>{display_html}</strong>" if is_lab else display_html)
    if not out:
        return ""
    if len(out) == 1:
        return out[0]
    if len(out) == 2:
        return " and ".join(out)
    return ", ".join(out[:-1]) + ", and " + out[-1]


def escape_html(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def venue_label(fields):
    candidates = [
        fields.get("booktitle", ""),
        fields.get("journal", ""),
        fields.get("series", ""),
        fields.get("howpublished", ""),
        fields.get("publisher", ""),
    ]
    haystack = " ".join(clean_tex(c) for c in candidates)
    for needle, label in VENUE_MAP:
        if needle.lower() in haystack.lower():
            return label
    # Fall back to a cleaned journal/booktitle, truncated.
    for c in candidates:
        c = clean_tex(c)
        if c:
            return c if len(c) <= 48 else c[:45].rstrip() + "…"
    return ""


def best_link(fields):
    if fields.get("doi"):
        doi = clean_tex(fields["doi"])
        return doi if doi.startswith("http") else f"https://doi.org/{doi}"
    if fields.get("url"):
        return clean_tex(fields["url"])
    return ""


def preprint_link(fields):
    if fields.get("eprint") and "arxiv" in fields.get("archiveprefix", "").lower():
        return f"https://arxiv.org/abs/{clean_tex(fields['eprint'])}"
    if fields.get("preprint"):
        return clean_tex(fields["preprint"])
    return ""


def keywords_of(fields):
    return {k.strip().lower() for k in fields.get("keywords", "").split(",") if k.strip()}


def yaml_field(key, value, indent="    "):
    return f"{indent}{key}: {json.dumps(value, ensure_ascii=False)}\n"


def emit(path, header, records, fields_order):
    lines = [header]
    for rec in records:
        first = True
        for key in fields_order:
            if key not in rec:
                continue
            prefix = "  - " if first else "    "
            lines.append(f"{prefix}{key}: {json.dumps(rec[key], ensure_ascii=False)}\n")
            first = False
    path.write_text("".join(lines), encoding="utf-8")


def main():
    if not BIB.exists():
        sys.exit(f"Bib file not found: {BIB}")
    entries = parse_entries(BIB.read_text(encoding="utf-8"))

    pubs = []
    for etype, fields in entries:
        kw = keywords_of(fields)
        year = clean_tex(fields.get("year", "")) or "0"
        try:
            year_int = int(re.sub(r"[^0-9]", "", year) or 0)
        except ValueError:
            year_int = 0
        title = clean_tex(fields.get("title", ""))
        if not title or year_int < MIN_YEAR:
            continue

        is_paper = bool(kw & {"conference-paper", "journal-article", "book-chapter", "workshop-paper"})
        if not is_paper:
            continue

        venue = venue_label(fields)
        rec = {
            "year": year_int,
            "title": title,
            "authors": format_authors(fields.get("author", "")),
            "venue": venue,
            "top": venue in TOP_VENUES,
        }
        link = best_link(fields)
        if link:
            rec["url"] = link
        pre = preprint_link(fields)
        if pre:
            rec["preprint"] = pre
        if fields.get("video"):
            rec["video"] = clean_tex(fields["video"])
        pubs.append(rec)

    pubs.sort(key=lambda r: (-r["year"], r["title"].lower()))

    header = ("# GENERATED FILE -- do not edit by hand.\n"
              "# Regenerate with: python3 scripts/build_publications.py\n"
              "# Source: _bibliography/publications.bib\n")

    emit(PUBS_OUT, header, pubs,
         ["year", "title", "authors", "venue", "top", "url", "preprint", "video"])

    print(f"Wrote {len(pubs)} publications -> {PUBS_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

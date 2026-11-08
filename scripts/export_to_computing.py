#!/usr/bin/env python3
"""Export SMCClab projects to the ANU School of Computing website.

Writes each project in _projects/ as _projects/smcclab-<name>.md in a local
clone of https://gitlab.anu.edu.au/jekyll-anu/computing-website, using that
site's front matter and "How to Apply" format, with a link back to the full
list on smcclab.au.

Usage:
    python3 scripts/export_to_computing.py ../computing-website impsy-on-bela-gem [more-names...]
    python3 scripts/export_to_computing.py ../computing-website --list
"""
import argparse
import pathlib
import re
import sys

SITE = pathlib.Path(__file__).resolve().parent.parent
PROJECTS = SITE / "_projects"
SITE_URL = "https://smcclab.au"

# Front matter keys the computing website understands; everything else is local to smcclab.au.
COMPUTING_KEYS = ["title", "tagline", "authors", "date", "clusters", "groups", "levels", "tags"]

# Levels offered by the computing website's CMS (admin/config.yml, "student-projects" collection).
COMPUTING_LEVELS = ["Bachelors", "Honours", "Masters", "MPhil", "PhD", "Internship"]


def collection_titles(dest, folder):
    """Titles of a computing-website collection (e.g. _research/clusters), used to validate front matter."""
    titles = set()
    for path in (dest / folder).glob("*.md"):
        fm, _ = split_front_matter(path.read_text())
        title = yaml_scalar(front_matter_blocks(fm), "title")
        if title:
            titles.add(title)
    return titles


def theme_block(key, field):
    """A block scalar field (e.g. intro) of a theme in _data/project_themes.yml, or ''."""
    text = (SITE / "_data" / "project_themes.yml").read_text()
    for block in text.split("- key: ")[1:]:
        if block.split("\n", 1)[0].strip() != key:
            continue
        lines = block.splitlines()
        for i, line in enumerate(lines):
            if line.strip() == f"{field}: |":
                body = []
                for cont in lines[i + 1:]:
                    if cont.strip() and not cont.startswith("    "):
                        break  # next field or next theme
                    body.append(cont[4:])
                return "\n".join(body).strip()
    return ""


def theme_intro(key):
    """Intro paragraph(s) for a theme, so the exported page stands alone. The optional export_intro
    key is written for readers of the computing website, who only see one project from the theme."""
    return theme_block(key, "export_intro") or theme_block(key, "intro")


# Lab systems and jargon that readers of the computing website won't know. The first unlinked mention
# of each term in a project body is linked to its canonical site (and glossed, if a gloss is given).
# Longer terms come first so that "Bela Gem Multi" is matched before "Bela Gem" or "Bela".
TERMS = [
    ("impsy-web", "https://github.com/cpmpercussion/impsy-web", None),
    ("IMPSY", "https://charlesmartin.au/impsy/", None),
    ("Bela Gem Multi", "https://bela.io/products/bela-gem-stereo-and-multi/", None),
    ("Bela Gem", "https://bela.io", None),
    ("Bela", "https://bela.io", None),
    ("MDRNN", None, "mixture density recurrent neural network"),
    ("COMP3740", "https://programsandcourses.anu.edu.au/course/COMP3740", None),
    ("COMP4350/COMP8350", "https://comp.anu.edu.au/courses/comp4350/", "Sound and Music Computing"),
]

# Standard context for every exported project: who we are and what an intelligent instrument is.
LAB_CONTEXT = f"""This is a research project in the [Sound, Music and Creative Computing Lab (SMCClab)]({SITE_URL}) at the ANU School of Computing, supervised by Charles Martin. The lab studies *intelligent musical instruments*: instruments with a built-in AI model that generates musical actions of its own, responding to the musician or playing alongside them. Most of our projects use [IMPSY](https://charlesmartin.au/impsy/), the lab's open-source system that records a musician's gestures from a MIDI controller, trains a small neural network on that data, and then plays back and responds in live performance on a Raspberry Pi, laptop, iPad, or in a web browser. You don't need to know these systems before you start: the background reading at the end of this page is the place to begin."""

LINK_RE = re.compile(r"!?\[[^\]]*\]\([^)]*\)")


def link_terms(body):
    """Link and gloss the first plain-text mention of each term in TERMS, outside existing links and
    outside the background reading list (where the terms appear in paper titles)."""
    head, sep, tail = body.partition("## Background reading")
    # Alternate plain-text and link parts so that text inside existing links is never touched.
    parts = []
    pos = 0
    for m in LINK_RE.finditer(head):
        parts.append((False, head[pos:m.start()]))
        parts.append((True, m.group(0)))
        pos = m.end()
    parts.append((False, head[pos:]))
    for term, url, gloss in TERMS:
        if url and any(is_link and f"]({url})" in text for is_link, text in parts):
            continue  # already linked by the author
        pattern = re.compile(r"(?<![\w/-])" + re.escape(term) + r"(?![\w/-])")
        for i, (is_link, text) in enumerate(parts):
            if is_link:
                continue
            m = pattern.search(text)
            if not m:
                continue
            linked = f"[{term}]({url})" if url else term
            if gloss:
                linked += f" ({gloss})"
            parts[i:i + 1] = [(False, text[:m.start()]), (True, linked), (False, text[m.end():])]
            break
    return "".join(text for _, text in parts) + sep + tail


def split_front_matter(text):
    _, fm, body = text.split("---", 2)
    return fm.strip("\n"), body.strip()


def front_matter_blocks(fm):
    """Split YAML front matter into top-level key blocks (keeps list items with their key)."""
    blocks, current = {}, None
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_]+):", line)
        if m:
            current = m.group(1)
            blocks[current] = [line]
        elif current:
            blocks[current].append(line)
    return blocks


def yaml_scalar(blocks, key):
    if key not in blocks:
        return None
    value = blocks[key][0].split(":", 1)[1].strip()
    if value in ("|", "|-", ">", ">-"):  # block scalar: join the indented continuation lines
        return " ".join(line.strip() for line in blocks[key][1:]).strip()
    return value.strip('"')


def yaml_list(blocks, key):
    return [line.split("-", 1)[1].strip().strip('"') for line in blocks.get(key, [])[1:] if line.strip().startswith("-")]


def export(name, dest):
    src = PROJECTS / f"{name}.md"
    if not src.exists():
        sys.exit(f"No project called {name!r} in {PROJECTS}")
    fm, body = split_front_matter(src.read_text())
    blocks = front_matter_blocks(fm)

    # Root-relative links (e.g. /join/) point at smcclab.au from the computing website.
    body = re.sub(r"\]\(/", f"]({SITE_URL}/", body)

    # Check the front matter against the computing website's own vocabulary.
    for key, folder in (("clusters", "_research/clusters"), ("groups", "_research/groups")):
        for value in set(yaml_list(blocks, key)) - collection_titles(dest, folder):
            print(f"warning: {name}: {key} value {value!r} is not a title in {dest / folder}", file=sys.stderr)

    # "Short" is a local level (six-week summer scholarship or one-semester COMP3740 project). The
    # computing site has no such level, so it becomes "Bachelors" plus an explanatory line.
    levels = yaml_list(blocks, "levels")
    short = "Short" in levels
    levels = [lv for lv in levels if lv in COMPUTING_LEVELS]
    if short and "Bachelors" not in levels:
        levels.insert(0, "Bachelors")
    for lv in set(yaml_list(blocks, "levels")) - set(levels) - {"Short"}:
        print(f"warning: {name}: dropped level {lv!r} (not in {COMPUTING_LEVELS})", file=sys.stderr)
    blocks["levels"] = ["levels:"] + [f"  - {lv}" for lv in levels]

    details = ["**Length:** Honours and Master projects run over two semesters."]
    if short:
        details.append("**Short project:** Also available as a six-week summer research scholarship or a one-semester [COMP3740](https://programsandcourses.anu.edu.au/course/COMP3740) project (see the short-project scope below).")
    if yaml_scalar(blocks, "level_note"):
        details.append(f"**Note:** {yaml_scalar(blocks, 'level_note')}")
    if yaml_scalar(blocks, "prerequisites"):
        details.append(f"**Prerequisites:** {yaml_scalar(blocks, 'prerequisites')}")

    details_md = link_terms("  \n".join(details))
    body = link_terms(body)
    intro = theme_intro(yaml_scalar(blocks, "theme") or "")
    if intro:
        intro = re.sub(r"\]\(/", f"]({SITE_URL}/", intro)
        intro = link_terms(intro)
    body = f"## About this project\n\n{LAB_CONTEXT}\n\n{intro}\n\n## This project\n\n{body}".replace("\n\n\n\n", "\n\n")
    if yaml_scalar(blocks, "image"):  # images are served from smcclab.au, not copied into the computing site
        alt = yaml_scalar(blocks, "image_alt") or yaml_scalar(blocks, "title")
        body = f"![{alt}]({SITE_URL}{yaml_scalar(blocks, 'image')})\n\n{body}"
    out_fm = "\n".join(line for key in COMPUTING_KEYS if key in blocks for line in blocks[key])
    page_url = f"{SITE_URL}/projects/{name}/"
    out = f"""---
{out_fm}
---

{details_md}

{body}

## More projects in the lab

This is one of more than a dozen projects currently available in the SMCClab, covering machine learning, embedded hardware, HCI, visualisation, theory, and artistic research. Only a selection is listed on the School of Computing website, so see the [full list of SMCClab student projects]({SITE_URL}/projects/) on the lab website. You can also read [this project on the lab website]({page_url}).

## How to Apply

To apply for this project, contact [Charles Martin]({{% link _people/charles-martin.md %}}).

Include:

- your CV
- your unofficial transcript (if you are an ANU student)
- a brief statement (200 words) in your email explaining how you would approach this project

Make sure to specify the skills and accomplishments you have that would help you to complete this project. Please read about [joining the SMCClab]({SITE_URL}/join/) and our [project expectations]({SITE_URL}/honsproj/) before applying.
"""
    target = dest / "_projects" / f"smcclab-{name}.md"
    target.write_text(out)
    print(f"wrote {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("dest", type=pathlib.Path, help="path to a local clone of computing-website")
    parser.add_argument("names", nargs="*", help="project names (filenames in _projects/ without .md)")
    parser.add_argument("--list", action="store_true", help="list available project names")
    args = parser.parse_args()

    if args.list or not args.names:
        for p in sorted(PROJECTS.glob("*.md")):
            print(p.stem)
        return
    if not (args.dest / "_projects").is_dir():
        sys.exit(f"{args.dest} doesn't look like the computing-website repo (no _projects/ folder)")
    for name in args.names:
        export(name, args.dest)


if __name__ == "__main__":
    main()

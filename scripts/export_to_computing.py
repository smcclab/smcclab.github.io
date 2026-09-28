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


def scalar(blocks, key):
    if key not in blocks:
        return None
    value = blocks[key][0].split(":", 1)[1].strip()
    return value.strip('"')


def export(name, dest):
    src = PROJECTS / f"{name}.md"
    if not src.exists():
        sys.exit(f"No project called {name!r} in {PROJECTS}")
    fm, body = split_front_matter(src.read_text())
    blocks = front_matter_blocks(fm)

    # Root-relative links (e.g. /join/) point at smcclab.au from the computing website.
    body = re.sub(r"\]\(/", f"]({SITE_URL}/", body)

    details = []
    if scalar(blocks, "level_note"):
        details.append(f"**Length:** {scalar(blocks, 'level_note')}")
    if scalar(blocks, "prerequisites"):
        details.append(f"**Prerequisites:** {scalar(blocks, 'prerequisites')}")

    details_md = "  \n".join(details)
    out_fm = "\n".join(line for key in COMPUTING_KEYS if key in blocks for line in blocks[key])
    page_url = f"{SITE_URL}/projects/{name}/"
    out = f"""---
{out_fm}
---

{details_md}

{body}

This project is one of several available in the [Sound, Music, and Creative Computing Lab]({SITE_URL}). See the [full list of SMCClab student projects]({SITE_URL}/projects/) and the [project page on the SMCClab website]({page_url}).

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

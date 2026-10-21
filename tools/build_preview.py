#!/usr/bin/env python3
"""Assemble a minimal static site with only the given decks and what they use.

Usage (from the repository root): tools/build_preview.py OUTDIR DECK.html [DECK.html ...]

Starting from the decks, follows local references (src/href/data-src/
data (<object>)/data-background*/data-markdown attributes, markdown links and CSS url())
through HTML, CSS and Markdown files, and copies every referenced file into
OUTDIR under its repository path. Files whose git-annex content is not
present are fetched with `git annex get` first (when git-annex is
available). Files that could not be obtained are reported, not fatal, so a
deck still previews with whatever content is available.

Used by .github/workflows/preview.yml, but also works locally.
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

# The repository to build from is the current directory, not the one this
# script lives in: the Preview workflow runs it on another checkout.
REPO = Path.cwd()

# Files that are scanned for further references
SCANNED_SUFFIXES = {".html", ".htm", ".css", ".md"}

# Each pattern captures (kind, quote, reference)
REF_PATTERNS = [
    # HTML attributes, e.g. src="..", data-src='..', <object data="..">,
    # data-background-image=".."
    re.compile(
        r"""\b(src|href|data|data-src|poster|data-markdown|data-background(?:-image|-video|-iframe)?)"""
        r"""\s*=\s*(["'])(.+?)\2""",
        re.I,
    ),
    # markdown images: ![alt](target "title")
    re.compile(r"""!\[[^\]]*\]\(\s*<?()()([^)\s>]+)"""),
    # CSS url(...)
    re.compile(r"""url\(\s*()(["']?)([^"')]+)\2\s*\)""", re.I),
]

# href is mostly used for hyperlinks (to other decks, PDFs, ...), which are
# not needed to render the deck; follow it only for stylesheets.
HREF_FOLLOWED_SUFFIXES = {".css"}


def local_target(ref, referrer):
    """Return the repository-relative path `ref` points to, or None."""
    ref = ref.strip()
    if not ref or ref.startswith(("#", "/", "data:", "{", "$")):
        return None
    parts = urlsplit(ref)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    target = (REPO / referrer).parent / unquote(parts.path)
    target = Path(os.path.normpath(target))
    try:
        rel = target.relative_to(REPO)
    except ValueError:
        return None  # points outside of the repository
    if rel.parts[0] == ".git":
        return None
    return rel


def refs_in(path):
    try:
        text = (REPO / path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return
    for pattern in REF_PATTERNS:
        for m in pattern.finditer(text):
            kind, _, ref = m.groups()
            target = local_target(ref, path)
            if target is None:
                continue
            if kind.lower() == "href" and target.suffix.lower() not in HREF_FOLLOWED_SUFFIXES:
                continue
            yield target


def collect(decks):
    """Walk references starting from the decks; return the set of files."""
    files, seen = set(), set()
    queue = list(decks)
    while queue:
        rel = queue.pop()
        if rel in seen:
            continue
        seen.add(rel)
        full = REPO / rel
        # an annexed file without content is a broken symlink: keep it so its
        # content can be fetched, but there is nothing to scan in it yet
        if full.is_dir() and not full.is_symlink():
            continue
        if not os.path.lexists(full):
            files.add(rel)  # reported as missing later
            continue
        files.add(rel)
        if rel.suffix.lower() in SCANNED_SUFFIXES:
            queue.extend(refs_in(rel))
    return files


def annex_get(paths):
    if not paths or not shutil.which("git-annex"):
        return
    # one call for all; failures for individual files are reported afterwards
    subprocess.run(
        ["git", "annex", "get", "--"] + [str(p) for p in sorted(paths)],
        cwd=REPO,
        check=False,
    )


def main(outdir, decks):
    outdir = Path(outdir).resolve()
    decks = [Path(d) for d in decks]
    files = collect(decks)

    annex_get([f for f in files if (REPO / f).is_symlink() and not (REPO / f).exists()])

    copied, missing = [], []
    for rel in sorted(files):
        src = REPO / rel
        if not src.exists():  # nonexistent, or annexed without content
            missing.append(rel)
            continue
        dst = outdir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)  # dereferences annex symlinks
        copied.append(rel)

    print(f"Copied {len(copied)} file(s) for {len(decks)} deck(s) into {outdir}")
    for rel in missing:
        print(f"MISSING: {rel}")
    return missing


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    missing = main(sys.argv[1], sys.argv[2:])
    if os.environ.get("GITHUB_ACTIONS"):
        for rel in missing:
            print(f"::warning file={rel}::Not available for the preview: {rel}")

#!/usr/bin/env python3
"""Export any reveal.js deck in this repo to PDF, headlessly.

A scriptable alternative to the two routes in ../README.md (manual
``?print-pdf`` in Chrome; decktape via Docker).  Needs only ``uv``:

    uv run --with playwright playwright install chromium   # once
    uv run --with playwright python tools/mkpdf.py <TALK-ID>.html

Writes ``<deck>.pdf`` next to the deck unless ``-o`` says otherwise.
Page size follows the deck's own ``width``/``height`` Reveal config via
reveal's print stylesheet, so nothing is hardcoded and it works for every
deck in this repo regardless of canvas size (1400x1050 or 1920x1080).

Derived PDFs are not committed -- generate on demand.
"""

import argparse
import asyncio
import pathlib
import sys

from playwright.async_api import async_playwright


async def export(deck: pathlib.Path, out: pathlib.Path, wait_ms: int) -> None:
    url = deck.resolve().as_uri() + "?print-pdf"
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        problems: list[str] = []
        page.on("pageerror", lambda e: problems.append(f"pageerror: {e}"))
        await page.goto(url, wait_until="networkidle")
        # reveal lays out print-pdf asynchronously; mermaid/highlight need a beat
        await page.wait_for_timeout(wait_ms)
        pages = await page.evaluate(
            "document.querySelectorAll('.reveal .slides section.pdf-page, "
            ".reveal .pdf-page').length"
        )
        await page.pdf(
            path=str(out),
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()
    if problems:
        print("\n".join(problems), file=sys.stderr)
    print(f"{out}  ({out.stat().st_size / 1e6:.1f} MB, {pages} pdf-pages laid out)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("deck", type=pathlib.Path, help="path to the <TALK-ID>.html deck")
    ap.add_argument("-o", "--output", type=pathlib.Path, default=None)
    ap.add_argument(
        "--wait",
        type=int,
        default=4000,
        help="ms to wait after load for mermaid/highlight/lazy images (default 4000)",
    )
    args = ap.parse_args()
    if not args.deck.is_file():
        sys.exit(f"no such deck: {args.deck}")
    out = args.output or args.deck.with_suffix(".pdf")
    asyncio.run(export(args.deck, out, args.wait))


if __name__ == "__main__":
    main()

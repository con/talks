#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Center for Open Neuroscience
# SPDX-License-Identifier: Apache-2.0
"""Print the editable HTML poster to PDF and optionally save a screen preview.

From the repository root:
    uv run --with playwright playwright install chromium  # once
    uv run --with playwright python 2026-usrse/build-orinoco-poster.py

Use --channel chrome to use an installed Google Chrome instead.
"""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


async def build(channel: str | None, preview: Path | None) -> None:
    source = Path(__file__).with_name("orinoco-lite-poster.html")
    output = source.with_suffix(".pdf")
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(channel=channel)
        page = await browser.new_page(viewport={"width": 1640, "height": 1300})
        await page.goto(source.as_uri(), wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        problems = await page.evaluate("""() => {
          const issues = [];
          for (const img of document.images) {
            if (!img.complete || !img.naturalWidth) issues.push(`Missing image: ${img.getAttribute('src')}`);
          }
          for (const el of document.querySelectorAll('.poster, .column, .masthead, .footer')) {
            if (el.scrollHeight > el.clientHeight + 2 || el.scrollWidth > el.clientWidth + 2)
              issues.push(`Overflow: ${el.className}`);
          }
          if (document.querySelectorAll('h1').length !== 1) issues.push('Expected one poster title');
          return issues;
        }""")
        if preview:
            await page.locator(".poster").screenshot(path=str(preview))
        if problems:
            await browser.close()
            raise RuntimeError("\n".join(problems))
        await page.pdf(
            path=str(output),
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=False,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()
    print(f"Created {output} ({output.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", help="Browser channel, e.g. chrome; default: Playwright Chromium")
    parser.add_argument("--preview", type=Path, help="Optional PNG preview path")
    args = parser.parse_args()
    asyncio.run(build(args.channel, args.preview))

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


async def build(channel: str | None, preview: Path | None, font_proof: bool = False) -> None:
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
          for (const el of document.querySelectorAll('.poster, .columns, .comparison, .deployment, .outcomes, .column-head, .masthead, .footer, .component-figure, .component-art, .website-evidence, .shared-editor, .qr-badge')) {
            if (el.scrollHeight > el.clientHeight + 2 || el.scrollWidth > el.clientWidth + 2) {
              const label = el.querySelector('h2')?.innerText || el.className;
              issues.push(`Overflow: ${label} (${el.scrollWidth}×${el.scrollHeight} in ${el.clientWidth}×${el.clientHeight}px)`);
            }
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
        if font_proof:
            # Use an actual poster sentence and family, with physical point sizes.
            from html import escape

            paragraph = await page.locator('.graph-description').inner_text()
            sample = escape(paragraph.split('. ', 1)[0] + '.')
            family = await page.locator('.graph-description').evaluate(
                "el => getComputedStyle(el).fontFamily"
            )
            body_pt = float(await page.locator('.graph-description').evaluate(
                "el => parseFloat(getComputedStyle(el).fontSize)"
            )) * 0.75
            blocks = ''.join(
                f'<section><h2>{size} pt{label}</h2>'
                f'<p style="font-size:{size}pt">{sample}</p></section>'
                for size, label in [(27, ' — larger comparison'), (25.5, ' — intermediate comparison'), (24, ' — smaller comparison')]
            )
            await page.set_content(f'''<!doctype html><html lang="en"><head>
                <meta charset="utf-8"><title>ORINOCO poster type-size proof</title>
                <style>
                @page {{ size: letter; margin: .55in; }}
                * {{ box-sizing: border-box; }}
                body {{ margin: 0; font-family: {family}; color: #193c4d; }}
                h1 {{ font-size: 18pt; margin: 0 0 10pt; }}
                .instructions {{ font-size: 10pt; line-height: 1.4; margin: 0 0 20pt; }}
                section {{ background: #f6f2e9; border-top: 2pt solid #286857;
                    padding: 10pt 12pt; margin-bottom: 14pt; break-inside: avoid; }}
                h2 {{ font-size: 11pt; margin: 0 0 9pt; color: #286857; }}
                section p {{ line-height: 1.35; margin: 0; }}
                .scale {{ width: 2in; border: solid #193c4d; border-width: 2pt 2pt 0;
                    height: 8pt; margin-top: 6pt; }}
                .note {{ font-size: 9pt; line-height: 1.4; }}
                </style></head><body>
                <h1>Compare the poster's printed text sizes</h1>
                <p class="instructions">Print this US Letter page at <b>Actual size / 100%</b>.
                Do not use “Fit to page”. Read it from the distance you expect at the poster,
                around one metre, and choose a size that is comfortable without leaning in.
                The wording, font family, line spacing and colors match the poster;
                this sheet uses narrower lines to fit ordinary paper.</p>
                {blocks}
                <div class="scale"></div><p class="note">This line should measure exactly 2 inches (50.8 mm).</p>
                <p class="note">PosterNerd recommends at least 24 pt for text and 36 pt for headings.
                Current main paragraphs are {body_pt:g} pt.
                Source: posternerd.com/tutorials/customer-questions</p>
                </body></html>''')
            proof = source.with_name('orinoco-font-proof.pdf')
            await page.pdf(path=str(proof), print_background=True, prefer_css_page_size=True,
                           display_header_footer=False)
            print(f"Created {proof}")
        await browser.close()
    print(f"Created {output} ({output.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", help="Browser channel, e.g. chrome; default: Playwright Chromium")
    parser.add_argument("--preview", type=Path, help="Optional PNG preview path")
    parser.add_argument("--font-proof", action="store_true", help="Also export a printable Letter-size type comparison")
    args = parser.parse_args()
    asyncio.run(build(args.channel, args.preview, args.font_proof))

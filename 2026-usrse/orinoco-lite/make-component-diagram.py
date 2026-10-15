#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Center for Open Neuroscience
# SPDX-License-Identifier: Apache-2.0
"""Adapt Stephan Heunis's ORINOCO component artwork for the Lite deployment.

Run from any directory with Python 3. The source illustration remains unchanged.
The output is a self-contained SVG; its new labels remain ordinary editable text.
"""
from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET

SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)
ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "assets/orinoco-selfhost-components-poster.svg"
OUTPUT = ROOT / "assets/orinoco-lite-components-poster.svg"


def main():
    source = ET.parse(SOURCE).getroot()
    diagram = ET.Element(f"{{{SVG}}}svg", {
        "viewBox": "0 0 678.08 304.58", "width": "678.08", "height": "304.58",
        "role": "img", "aria-labelledby": "lite-title lite-description",
    })
    ET.SubElement(diagram, f"{{{SVG}}}title", {"id": "lite-title"}).text = "ORINOCO Lite components"
    ET.SubElement(diagram, f"{{{SVG}}}desc", {"id": "lite-description"}).text = (
        "A shared schema defines the SHACL Vue editor. The editor proposes changes "
        "through the shared App to GitHub pull requests. Reviewers merge accepted "
        "changes into Git-backed YAML records. GitHub Actions runs ORINOCO tools to "
        "build reusable outputs, illustrated by a catalog, website and report. "
        "Adapted from ORINOCO artwork by Stephan Heunis, CC BY 4.0."
    )
    defs = deepcopy(source.find(f"{{{SVG}}}defs"))
    diagram.append(defs)
    marker = ET.SubElement(defs, f"{{{SVG}}}marker", {
        "id": "lite-arrowhead", "viewBox": "0 0 10 10", "refX": "9", "refY": "5",
        "markerWidth": "5", "markerHeight": "5", "orient": "auto-start-reverse",
    })
    ET.SubElement(marker, f"{{{SVG}}}path", {"d": "M 1 1 L 9 5 L 1 9", "fill": "none", "stroke": "#009900", "stroke-width": "1.6"})
    # Keep the original schema, editor, processing and output artwork in place.
    # Remove Forgejo, Dump Things, and the old integration/storage arrows.
    removed = {
        "g6835",  # Forgejo
        "g1",  # Dump Things truck, logo and label
        "layer1-5-3-1-8-5-3-2", "layer1-5-3-1-8-5-3-2-7",  # editor/storage pair
        "g36094", "g36094-2",  # Forgejo integration pairs
        "g34511-8",  # schema arrow; its replacement leads directly to the editor
    }
    scale = ET.SubElement(diagram, f"{{{SVG}}}g", {"transform": "scale(3.7795275591)"})
    layer = deepcopy(source.find(f"{{{SVG}}}g"))
    for child in list(layer):
        if child.get("id") in removed:
            layer.remove(child)
    scale.append(layer)
    # Overlay coordinates use CSS pixels, corresponding to the original canvas.
    overlay = ET.fromstring('''<g xmlns="http://www.w3.org/2000/svg" font-family="Arial, Helvetica, sans-serif" fill="#193c4d">
      <g id="lite-connections" fill="none" stroke="#009900" stroke-width="1.8" marker-end="url(#lite-arrowhead)">
        <path d="M 134,144 C 165,143 163,92 190,80"/>
        <path d="M 289,93 C 309,98 314,109 324,119"/>
        <path d="M 351,169 C 341,195 301,207 275,216"/>
        <path d="M 278,243 C 367,281 423,235 468,168"/>
      </g>
      <g id="lite-connection-labels" font-size="11" text-anchor="middle">
        <text x="150" y="105">defines</text>
        <text x="335" y="84">propose</text>
        <text x="353" y="98" font-size="9.5">via shared App</text>
        <text x="319" y="185">merge</text>
        <text x="382" y="265">build</text>
      </g>
      <g id="github-pull-requests" transform="translate(295 115)">
        <circle cx="22" cy="26" r="22" fill="#193c4d"/>
        <g fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="15" cy="14" r="3"/><circle cx="15" cy="37" r="3"/>
          <circle cx="31" cy="37" r="3"/><path d="M 15,17 V 34 M 31,34 V 23 Q 31,14 24,14 H 22 M 25,10 L 21,14 L 25,18"/>
        </g>
        <text x="51" y="31" font-size="25" font-weight="700">GitHub</text>
        <text x="78" y="53" font-size="13" text-anchor="middle">pull requests</text>
      </g>
      <g id="git-yaml-records" transform="translate(206 198)">
        <path d="M 15,5 H 52 L 66,19 V 62 H 15 Z" fill="#ffeed0" stroke="#193c4d" stroke-width="2"/>
        <path d="M 52,5 V 19 H 66" fill="none" stroke="#193c4d" stroke-width="2"/>
        <g fill="none" stroke="#b55c28" stroke-width="2.5" stroke-linecap="round">
          <path d="M 28,29 V 48 M 28,41 Q 42,41 44,29"/>
          <circle cx="28" cy="27" r="3" fill="#ffeed0"/><circle cx="28" cy="51" r="3" fill="#ffeed0"/>
          <circle cx="45" cy="26" r="3" fill="#ffeed0"/>
        </g>
        <text x="40" y="80" font-size="15" text-anchor="middle" font-weight="700">Git + YAML</text>
        <text x="40" y="95" font-size="11" text-anchor="middle">accepted records</text>
      </g>
      <g id="actions-processing" font-size="12" text-anchor="middle">
        <text x="489" y="91" font-weight="700">GitHub Actions</text>
        <text x="489" y="106">ORINOCO tools</text>
      </g>
    </g>''')
    diagram.append(overlay)
    # Avoid following a git-annex symlink when regenerating a staged asset.
    if OUTPUT.is_symlink():
        OUTPUT.unlink()
    ET.ElementTree(diagram).write(OUTPUT, encoding="utf-8", xml_declaration=True)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()

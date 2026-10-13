# SPDX-FileCopyrightText: 2026 Center for Open Neuroscience
# SPDX-License-Identifier: Apache-2.0
# /// script
# requires-python = ">=3.11"
# dependencies = ["qrcode==8.2", "Pillow==11.3.0", "zxing-cpp==2.3.0"]
# ///
"""Generate the poster's four vector QR codes and verify their destinations.

Run with `uv run 2026-usrse/make-logo-qrs.py --check-dir /tmp/con-qr-checks`.
Requires Inkscape (for outlining the existing logo) and rsvg-convert (for
independent rasterization). SVG assets are written to pics/; check images and
the JSON report stay in --check-dir, outside the repository by default.
"""

import argparse
import copy
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFilter
import qrcode
import zxingcpp


ROOT = Path(__file__).resolve().parents[1]
SVG = "http://www.w3.org/2000/svg"
INK = "#193c4d"
BORDER = 4  # Four completely clear modules on every side.
DESTINATIONS = {
    "upstream": "https://hub.psychoinformatics.de/orinoco/",
    "lite": "https://github.com/ORINOCO-Lite",
    "con": "https://dev.centerforopenneuroscience.org/",
    "video": (
        "https://datasets.datalad.org/repronim/ReproTube/web/"
        "#/channel/DataLad/video/oF98hdaph1k"
    ),
}
ET.register_namespace("", SVG)


def element(tag, attrs=None, text=None):
    node = ET.Element(f"{{{SVG}}}{tag}", attrs or {})
    node.text = text
    return node


def outline_logo(inkscape, output):
    """Outline and crop the existing complete mark, including its subtitle."""
    subprocess.run(
        [inkscape, str(ROOT / "pics/con-logo_blue_big.svg"),
         "--export-type=svg", "--export-plain-svg", "--export-text-to-path",
         "--export-area-drawing", f"--export-filename={output}"],
        check=True,
    )
    logo = ET.parse(output).getroot()
    assert not logo.findall(f".//{{{SVG}}}text"), "Logo must be outlined"
    # Keep the original geometry. Only recolor its blue ink to the poster navy.
    for node in logo.iter():
        for key, value in list(node.attrib.items()):
            for blue in ("#87aade", "#88aadd"):
                value = value.replace(blue, INK)
            node.set(key, value)
    return logo


def write_qr(name, url, logo):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,
                       border=BORDER, box_size=1)
    qr.add_data(url)
    qr.make(fit=True)
    modules = qr.get_matrix()
    size = len(modules)
    body_size = size - 2 * BORDER
    assert all(not any(row) for row in modules[:BORDER] + modules[-BORDER:])
    assert all(not any(row[:BORDER] + row[-BORDER:]) for row in modules)
    root = element("svg", {
        "version": "1.1", "width": "45mm", "height": "45mm",
        "viewBox": f"0 0 {size} {size}", "role": "img",
        "aria-labelledby": "qr-title qr-description",
    })
    root.append(element("title", {"id": "qr-title"}, f"CON QR code: {name}"))
    root.append(element("desc", {"id": "qr-description"},
                        f"{url}; high error correction; four-module quiet zone."))
    root.append(element("rect", {"width": str(size), "height": str(size),
                                  "fill": "#ffffff"}))
    # Combine consecutive dark cells into horizontal runs, retaining square
    # module geometry and avoiding hairline seams between adjacent cells.
    runs = []
    for y, row in enumerate(modules):
        x = 0
        while x < size:
            if not row[x]:
                x += 1
                continue
            start = x
            while x < size and row[x]:
                x += 1
            runs.append(f"M{start},{y}h{x-start}v1h-{x-start}z")
    root.append(element("path", {"d": "".join(runs), "fill": INK}))

    _, _, logo_vw, logo_vh = map(float, logo.get("viewBox").split())
    logo_width = body_size * 0.30
    logo_height = logo_width * logo_vh / logo_vw
    padding = 1.0
    pad_width, pad_height = logo_width + 2 * padding, logo_height + 2 * padding
    root.append(element("rect", {
        "x": f"{(size-pad_width)/2:.6f}", "y": f"{(size-pad_height)/2:.6f}",
        "width": f"{pad_width:.6f}", "height": f"{pad_height:.6f}",
        "rx": "0.55", "fill": "#ffffff",
    }))
    logo_box = element("svg", {
        "x": f"{(size-logo_width)/2:.6f}", "y": f"{(size-logo_height)/2:.6f}",
        "width": f"{logo_width:.6f}", "height": f"{logo_height:.6f}",
        "viewBox": logo.get("viewBox"), "preserveAspectRatio": "xMidYMid meet",
    })
    for child in logo:
        # Inkscape export may retain metadata/hidden layers; only SVG drawing
        # content belongs in the embedded mark.
        if not child.tag.startswith(f"{{{SVG}}}"):
            continue
        if child.tag in {f"{{{SVG}}}metadata", f"{{{SVG}}}title", f"{{{SVG}}}desc"}:
            continue
        if "display:none" in child.get("style", "").replace(" ", ""):
            continue
        logo_box.append(copy.deepcopy(child))
    root.append(logo_box)
    assert not root.findall(f".//{{{SVG}}}text")
    assert not root.findall(f".//{{{SVG}}}image"), "Logo must remain native vector"
    destination = ROOT / f"pics/orinoco-qr-{name}.svg"
    ET.ElementTree(root).write(destination, encoding="utf-8", xml_declaration=True)
    return {
        "name": name, "url": url, "file": str(destination),
        "qr_version": qr.version, "error_correction": "H",
        "modules_including_border": size, "quiet_border_modules": BORDER,
        "logo_pad_percent_of_body_area": round(100*pad_width*pad_height/body_size**2, 2),
    }


def check_code(row, check_dir):
    checks = []
    # 180 and 210 px cover the former and current poster CSS sizes.
    # 177/266 px approximate 30/45 mm at
    # 150 dpi; 354/531 px approximate 30/45 mm at 300 dpi.
    for pixels in (144, 177, 180, 210, 240, 266, 354, 531, 720):
        raster = check_dir / f"qr-{row['name']}-{pixels}px.png"
        subprocess.run(["rsvg-convert", "-w", str(pixels), "-h", str(pixels),
                        "-o", str(raster), row["file"]], check=True)
        image = Image.open(raster).convert("RGB")
        variants = {"original": image, "rotated-90": image.transpose(Image.Transpose.ROTATE_90)}
        if pixels >= 177:
            variants["grayscale-softened"] = image.convert("L").filter(ImageFilter.GaussianBlur(0.35))
        for variant, candidate in variants.items():
            decoded = zxingcpp.read_barcodes(candidate)
            ok = len(decoded) == 1 and decoded[0].text == row["url"]
            checks.append({"pixels": pixels, "variant": variant, "passed": ok,
                           "decoded": [code.text for code in decoded]})
    row["checks"] = checks
    return all(check["passed"] for check in checks)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-dir", type=Path,
                        default=Path(tempfile.gettempdir()) / "con-qr-checks")
    parser.add_argument("--inkscape", default=shutil.which("inkscape") or
                        "/Applications/Inkscape.app/Contents/MacOS/inkscape")
    args = parser.parse_args()
    args.check_dir.mkdir(parents=True, exist_ok=True)
    logo = outline_logo(args.inkscape, args.check_dir / "con-logo-outlined.svg")
    report = [write_qr(name, url, logo) for name, url in DESTINATIONS.items()]
    success = True
    for row in report:
        passed = check_code(row, args.check_dir)
        success = passed and success
        print(f"{row['name']}: version {row['qr_version']} / H; "
              f"{sum(check['passed'] for check in row['checks'])}/"
              f"{len(row['checks'])} decoding checks passed")
    (args.check_dir / "decode-report.json").write_text(json.dumps(report, indent=2)+"\n")
    overview = Image.new("RGB", (4*360, 400), "white")
    draw = ImageDraw.Draw(overview)
    for i, row in enumerate(report):
        image = Image.open(args.check_dir / f"qr-{row['name']}-354px.png")
        overview.paste(image, (360*i+3, 5))
        draw.text((360*i+20, 370), row["name"], fill=INK)
    overview.save(args.check_dir / "qr-overview.png")
    if not success:
        raise SystemExit("QR verification failed; inspect decode-report.json")


if __name__ == "__main__":
    main()

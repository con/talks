#!/usr/bin/env python3

import argparse
import base64
import io
import logging
import re
import sys
import xml.etree.ElementTree as ET

import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import GappedSquareModuleDrawer
from qrcode.image.svg import SvgPathFillImage

# Create a dedicated logger
lgr = logging.getLogger(__name__)


def sanitize_filename(filename):
    sanitized = re.sub(r"[^\w]", "_", filename)
    return sanitized


def validate_compression_qualities(qualities):
    valid_qualities = {"L", "M", "Q", "H"}
    if not all(q in valid_qualities for q in qualities):
        raise ValueError(
            "Invalid compression qualities specified. "
            f"Use any combination of: {', '.join(valid_qualities)}."
        )
    return qualities


def _generate_svg(text, input_image, output_image, compression_quality):
    """Generate SVG QR code, embedding logo as a base64 data URI if given."""
    compress_quality = getattr(qrcode.constants, f"ERROR_CORRECT_{compression_quality}")
    qr = qrcode.QRCode(error_correction=compress_quality)
    qr.add_data(text)
    img = qr.make_image(image_factory=SvgPathFillImage)

    svg_buffer = io.BytesIO()
    img.save(svg_buffer)
    svg_bytes = svg_buffer.getvalue()

    ET.register_namespace("", "http://www.w3.org/2000/svg")
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
    root = ET.fromstring(svg_bytes)

    if input_image:
        lgr.debug(f"Embedding logo in SVG: {input_image}")
        # Use viewBox coordinates for placement math
        vb = root.get("viewBox", "0 0 37 37").split()
        vb_w, vb_h = float(vb[2]), float(vb[3])
        logo_size = min(vb_w, vb_h) * 0.30
        logo_x = (vb_w - logo_size) / 2
        logo_y = (vb_h - logo_size) / 2

        ext = input_image.rsplit(".", 1)[-1].lower()
        mime = {
            "svg": "image/svg+xml",
            "png": "image/png",
            "jpg": "image/jpeg",
            "jpeg": "image/jpeg",
        }.get(ext, "image/png")
        with open(input_image, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
        href = f"data:{mime};base64,{logo_b64}"

        svg_ns = "http://www.w3.org/2000/svg"
        image_elem = ET.SubElement(root, f"{{{svg_ns}}}image")
        image_elem.set("x", str(logo_x))
        image_elem.set("y", str(logo_y))
        image_elem.set("width", str(logo_size))
        image_elem.set("height", str(logo_size))
        image_elem.set("href", href)
        # SVG 1.1 compat
        image_elem.set("{http://www.w3.org/1999/xlink}href", href)

    tree = ET.ElementTree(root)
    ET.indent(tree)
    with open(output_image, "wb") as f:
        tree.write(f, xml_declaration=True, encoding="UTF-8")
    lgr.info(f"SVG QR code saved: {output_image} (verification skipped for SVG)")


def main(text, input_image, output_image, compression_qualities):
    lgr.debug(f"Processing text: {text}")

    if output_image.lower().endswith(".svg"):
        _generate_svg(text, input_image, output_image, compression_qualities[0])
        return

    kws = {}
    if input_image:
        lgr.debug(f"Embedding image: {input_image}")
        kws["embeded_image_path"] = input_image

    for q in compression_qualities:
        compress_quality = getattr(qrcode.constants, f"ERROR_CORRECT_{q}")

        qr = qrcode.QRCode(error_correction=compress_quality)
        qr.add_data(text)

        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=GappedSquareModuleDrawer(),
            **kws,
        )
        img.save(output_image)
        lgr.debug(f"Saved QR code image to: {output_image}")

        decoded = decode(Image.open(output_image))

        if len(decoded) != 1:
            lgr.debug(f"With error correction {q} got {len(decoded)} results.")
            continue

        decoded_data = decoded[0]
        lgr.debug(
            f"DEBUG: error correction {q} - quality: {decoded_data.quality}"
        )

        if decoded_data.quality < 0.5:
            lgr.warning(
                "With error correction {q} "
                f"got too low quality {decoded_data.quality}."
            )
            continue

        text_decoded = decoded_data.data.decode()
        if text_decoded != text:
            lgr.warning(
                f"With error correction {q} decoded text does not match: "
                f"{text_decoded!r} instead of {text!r}"
            )
            continue

        lgr.info(
            f"Successfully decoded text: {text_decoded!r} "
            f"encoded with compress quality {q}. File {output_image}"
        )
        break
    else:
        lgr.error(
            "Neither of error correction levels was good enough. "
            f"File {output_image} might be unreadable."
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate and decode QR codes."
    )
    parser.add_argument("text", help="Text to encode in the QR code.")
    parser.add_argument(
        "-i", "--input-image", help="Path to the input image (optional)."
    )
    parser.add_argument(
        "-o", "--output-image", help="Path to the output image (optional)."
    )
    parser.add_argument(
        "-c",
        "--compression-qualities",
        default="LMQH",
        help=(
            "Compression qualities (default: LMQH). "
            "Choose any combination of L, M, Q, H."
        ),
    )
    parser.add_argument(
        "-l",
        "--log-level",
        default="INFO",
        help="Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).",
    )

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=args.log_level.upper(),
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Validate compression qualities
    try:
        compression_qualities = validate_compression_qualities(
            args.compression_qualities
        )
    except ValueError as e:
        lgr.error(e)
        sys.exit(1)

    # Sanitize output filename
    output_filename = (
        args.output_image or f"{sanitize_filename(args.text)}.png"
    )

    main(args.text, args.input_image, output_filename, compression_qualities)

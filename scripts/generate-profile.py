#!/usr/bin/env python3
"""Generate dithered pink pixel profile image from a source photo."""

import argparse
import io
import sys
from pathlib import Path

from PIL import Image
from rembg import remove

PINK = (0xFF, 0x2D, 0x78)

BAYER4 = [
    [ 0,  8,  2, 10],
    [12,  4, 14,  6],
    [ 3, 11,  1,  9],
    [15,  7, 13,  5],
]

def process(src: Path, dst: Path, grid: int = 128, output_size: int = 1024):
    img = Image.open(src)
    w, h = img.size

    # Square crop from center
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    img = img.crop((left, top, left + side, top + side))

    # Remove background
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    result = remove(buf.read())
    img = Image.open(io.BytesIO(result)).convert("RGBA")

    # Harden alpha: anything partially visible becomes fully opaque
    # Prevents dark clothing from being eroded by background removal
    px = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if a > 10:
                px[x, y] = (r, g, b, 255)
            else:
                px[x, y] = (0, 0, 0, 0)

    # Downscale to pixel grid
    small = img.resize((grid, grid), Image.BILINEAR)

    # Ordered dithering: each pixel is either solid pink or transparent
    pixels = small.load()
    for y in range(grid):
        for x in range(grid):
            r, g, b, a = pixels[x, y]
            if a < 30:
                pixels[x, y] = (0, 0, 0, 0)
            else:
                lum = 0.299 * r + 0.587 * g + 0.114 * b
                darkness = (255 - lum) / 255.0
                threshold = (BAYER4[y % 4][x % 4] + 0.5) / 16.0
                if darkness > threshold:
                    pixels[x, y] = (*PINK, 255)
                else:
                    pixels[x, y] = (0, 0, 0, 0)

    # Scale back up with hard pixel edges
    out = small.resize((output_size, output_size), Image.NEAREST)
    out.save(dst)
    print(f"Saved {dst}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("src", help="Path to source photo")
    parser.add_argument(
        "-o", "--output",
        default=str(Path(__file__).resolve().parent.parent / "images" / "profile-pixel.png"),
        help="Output path (default: images/profile-pixel.png)",
    )
    parser.add_argument("-g", "--grid", type=int, default=128, help="Pixel grid size (default: 128)")
    parser.add_argument("-s", "--size", type=int, default=1024, help="Output image size (default: 1024)")
    args = parser.parse_args()

    process(Path(args.src), Path(args.output), args.grid, args.size)

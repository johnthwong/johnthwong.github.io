# Profile image

The profile image (`images/profile-pixel.png`) is generated from a source photo using `scripts/generate-profile.py`. Run with the `jekyll` conda env Python at `/opt/miniconda3/envs/jekyll/bin/python3`.

The image is a dithered pixel art portrait: single-shade pink (`#ff2d78`) cells on a transparent background. Darker areas of the face have denser pink pixels; lighter areas have fewer. Each pixel is either fully opaque pink or fully transparent (no gradients or alpha variation). The background is removed so only the person is visible.

The script center-crops the source photo to a square, removes the background with rembg, downscales to a pixel grid (default 128), applies Bayer ordered dithering, then scales back up with nearest-neighbor interpolation.

Usage: `python3 scripts/generate-profile.py <source-image>`

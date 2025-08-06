# -*- coding: utf-8 -*-
#
# @File:   compress_avatar.py
# @Author: Haozhe Xie
# @Date:   2025-05-27 10:14:03
# @Last Modified by: Haozhe Xie
# @Last Modified at: 2025-05-28 14:28:46
# @Email:  root@haozhexie.com

import os

import cv2
from PIL import Image

def _center_crop(img):
    height, width, _ = img.shape
    size = min(height, width)
    x = (width - size) // 2
    y = (height - size) // 2
    return img[y : y + size, x : x + size]


def main():
    script_dir = os.path.dirname(__file__)
    avatar_dir = os.path.join(script_dir, os.path.pardir, "assets", "images", "avatars")
    avatar_images = os.listdir(avatar_dir)

    for ai in avatar_images:
        fname, ext = os.path.splitext(ai)
        if ext.lower() == ".webp":
            continue

        output_file_path = os.path.join(avatar_dir, "%s.webp" % fname)
        img = cv2.imread(os.path.join(avatar_dir, ai))
        img = _center_crop(img)
        img = cv2.resize(img, (512, 512))
        Image.fromarray(img[..., ::-1]).convert("RGB").save(output_file_path, "webp")

if __name__ == "__main__":
    main()

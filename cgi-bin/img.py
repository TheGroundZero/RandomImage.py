#!/usr/bin/env python3

import os
import sys
from os import listdir
from random import choice

ext2conttype = {
    ".bmp": "image/bmp",
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".tiff": "image/tiff",
    ".webp": "image/webp",
    ".ico": "image/x-icon"
}


def display_image(src):
    sys.stdout.write("Content-Type: {}\n".format(content_type(src)))
    sys.stdout.write("Content-Length: " + str(os.stat(src).st_size) + "\n")
    sys.stdout.write("Cache-Control: no-cache, no-store, must-revalidate\n")
    sys.stdout.write("Pragma: no-cache\n")
    sys.stdout.write("Expires: 0\n")
    sys.stdout.write("X-Content-Type-Options: nosniff\n")
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.buffer.write(open(src, "rb").read())


def get_ext(file):
    filename, extension = os.path.splitext(file)
    return extension


def content_type(file):
    return ext2conttype[get_ext(file)]


def is_image(file):
    return get_ext(file) in ext2conttype


def random_file(dir):
    files = [f for f in listdir(dir) if is_image(f)]
    return choice(files)


def main():
    directory = "../img/"
    img = random_file(directory)
    display_image(directory + img)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os
import sys
from os import listdir
from random import choice

ext2conttype = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif"
}


def main():
    directory = "/root/TOOLS/RandomImage.py/img/"
    img = random_file(directory)
    display_image(directory + img)


def display_image(src):
    sys.stdout.write("Content-Type: {}\n".format(content_type(src)))
    sys.stdout.write("Content-Length: " + str(os.stat(src).st_size) + "\n")
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


if __name__ == "__main__":
    main()

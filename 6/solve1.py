#!/usr/bin/python3

from typing import Sequence
import sys

def read_input(input_file):
    f = open(input_file, "r")
    for l in f:
        yield str.rstrip(l)

def is_all_different(buf):
    m = {}
    for b in buf:
        if b is None:
            return False
        if b in m:
            return False
        m[b] = True
    return True

def process_input(input_file):
    line = next(read_input(input_file))
    buf = [None, None, None, None]
    pos = 0
    for c in line:
        pos += 1
        # push next value
        buf[0:14] = [c] + buf[0:13]
        if is_all_different(buf):
            print(f"found marker: {buf}, pos = {pos}")
            return


def main(argv: Sequence[str]):
    if len(argv) < 2:
        print(f"usage: {argv[0]} inputfile")
        exit(1)
    process_input(argv[1])

main(sys.argv)

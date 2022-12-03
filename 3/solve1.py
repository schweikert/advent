#!/usr/bin/python3

from typing import Sequence
import re
import sys

def read_input(input_file):
    f = open(input_file, "r")
    for l in f:
        yield str.rstrip(l)

def split_contents(line):
    mid = int(len(line)/2)
    a=line[:mid]
    b=line[mid:]
    return a, b

def find_common(c1, c2):
    found = {}
    for c in c1:
        found[c] = 1
    for c in c2:
        if c in found:
            return c
    raise RuntimeError(f"no common char found: {c1}, {c2}")

def prio(c):
    cn = ord(c)
    if cn >= ord('a') and cn <= ord('z'):
        return cn - ord('a') + 1
    if cn >= ord('A') and cn <= ord('Z'):
        return cn - ord('A') + 27

def process_input(input_file):
    total = 0
    for l in read_input(input_file):
        print(f"l: {l}")
        c1, c2 = split_contents(l)
        c = find_common(c1, c2)
        p = prio(c)
        total = total + p
    print(f"total = {total}")

def main(argv: Sequence[str]):
    if len(argv) < 2:
        print(f"usage: {argv[0]} inputfile")
        exit(1)
    process_input(argv[1])

main(sys.argv)

#!/usr/bin/python3

from typing import Sequence
import sys

def read_input(input_file):
    f = open(input_file, "r")
    for l in f:
        yield str.rstrip(l)

def process_input(input_file):
    for l in read_input(input_file):
        print(l)


def main(argv: Sequence[str]):
    if len(argv) < 2:
        print(f"usage: {argv[0]} inputfile")
        exit(1)
    process_input(argv[1])

main(sys.argv)

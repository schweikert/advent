#!/usr/bin/python3

from typing import Sequence
import re
import sys

lettersmap = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}

def read_input(input_file):
    f = open(input_file, "r")
    for l in f:
        yield str.rstrip(l)

def wins(a, b):
    sign = 1
    if a == b:
        return 0
    if a > b:
        sign = -1
        b, a = a, b
    if a == 'P' and b == 'R':
        return sign
    elif a == 'P' and b == 'S':
        return sign * -1
    elif a == 'R' and b == 'S':
        return sign
    else:
        raise RuntimeError(f"internal error: {a}, {b}")

def calc_score(a, b):
    score = 0

    w = wins(b, a)
    if w == 1:
        score = score + 6
    elif w == 0:
        score = score + 3

    if b == 'R':
        score = score + 1
    elif b == 'P':
        score = score + 2
    elif b == 'S':
        score = score + 3

    return score



def process_input(input_file):
    total_score = 0
    for l in read_input(input_file):
        m = re.match(r'^([ABC]) ([XYZ])$', l)
        if not m:
            raise RuntimeError(f"can't match: {l}")
        a = lettersmap[m.group(1)]
        b = lettersmap[m.group(2)]
        score = calc_score(a, b)
        print(f"a={a}, b={b}, score={score}")
        total_score = total_score + score
    print(f"total: {total_score}")



def main(argv: Sequence[str]):
    if len(argv) < 2:
        print(f"usage: {argv[0]} inputfile")
        exit(1)
    process_input(argv[1])

main(sys.argv)

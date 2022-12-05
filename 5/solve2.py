#!/usr/bin/python3

from typing import Sequence
import re
import sys

def read_input(input_file):
    f = open(input_file, "r")
    for l in f:
        yield l.rstrip("\n")

def read_stacks(lines):
    stacks = []
    for l in lines:
        n = 0
        while(len(l) > 0):
            block = l[0:4]
            l = l[4:]
            if block != '    ' and block != '   ':
                m = re.match(r'\[(.)\] ?', block)
                if m:
                    print(f"n={n}, block={m.group(1)}")
                    while(len(stacks) < n + 1):
                        stacks.append([])
                    stacks[n].insert(0, m.group(1))
                else:
                    print(f"can't parse: {block}, assuming end.")
                    return stacks
            n += 1

def process_input(input_file):
    lines = read_input(input_file)
    stacks = read_stacks(lines)

    # we expect an empty line
    l = next(lines)
    if l != "":
        raise RuntimeError(f"unexpected line 1: {l}")

    # read orders
    for l in lines:
        m = re.match(r'^move (\d+) from (\d+) to (\d+)$', l)
        if not m:
            raise RuntimeError(f"unexpected line: {l}")
        count, fr, to = int(m.group(1)), int(m.group(2))-1, int(m.group(3))-1
        print(f"{stacks}, move {count} from {fr} to {to}")
        x = stacks[fr][-count:]
        print(f"x = {x}")
        del stacks[fr][-count:]
        stacks[to].extend(x)
        print(f"result = {stacks}")
        print()

    print("".join([ s[-1] for s in stacks]))


def main(argv: Sequence[str]):
    if len(argv) < 2:
        print(f"usage: {argv[0]} inputfile")
        exit(1)
    stack = process_input(argv[1])



main(sys.argv)

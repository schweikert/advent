#!/usr/bin/python3

def read_block(f):
    block = []
    for line in f:
        l = str.rstrip(line)
        if l == "":
            yield block
            block = []
            continue
        block.append(int(l))

def main():
    f = open("input", "r")

    b_max = 0
    for b in read_block(f):
        b_total = sum(b)
        if b_total > b_max:
            b_max = b_total
    print(b_max)

main()

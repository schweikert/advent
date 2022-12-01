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
    if block:
        yield block

def main():
    f = open("input", "r")

    top = [ 0, 0, 0 ]
    for b in read_block(f):
        b_total = sum(b)
        if b_total > top[0]:
           top[0] = b_total 
           top.sort()
    print(top)
    print(sum(top))

main()

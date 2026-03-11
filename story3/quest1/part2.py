import sys
import string

infile = sys.argv[1] if len(sys.argv) > 1 else "example1.in"

def convert(piece: str):
    ans = 0
    for i, el in enumerate(piece[::-1]):
        if el.isupper():
            ans += (1 << i)
    return ans

with open(infile, "r") as f:
    lines = f.read().splitlines()
    ans = 0
    shine = -1
    darkest = 0
    ans = 0
    for line in lines:
        num, pieces = line.split(":")
        num = int(num)
        pieces = [convert(piece) for piece in pieces.split()]
        assert len(pieces) == 4
        c_shine = pieces[-1]
        if c_shine > shine:
            shine = c_shine
            darkest = sum(pieces) - shine
            ans = num
        elif c_shine == shine and sum(pieces) - shine < darkest:
            darkest = sum(pieces) - shine
            ans = num
    print(f"{ans=}")

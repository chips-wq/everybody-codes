import sys
import string
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else "example1.in"

def convert(piece: str):
    ans = 0
    for i, el in enumerate(piece[::-1]):
        if el.isupper():
            ans += (1 << i)
    return ans

with open(infile, "r") as f:
    lines = f.read().splitlines()
    D = defaultdict(list)
    for line in lines:
        num, pieces = line.split(":")
        num = int(num)
        pieces = [convert(piece) for piece in pieces.split()]
        assert len(pieces) == 4
        c_shine = pieces[-1]
        T = []
        if c_shine <= 30: T.append(0)
        if c_shine >= 33: T.append(1)
        if pieces[0] > pieces[1] and pieces[0] > pieces[2]: T.append(0) # red dominant
        if pieces[1] > pieces[0] and pieces[1] > pieces[2]: T.append(1) # green dominant
        if pieces[2] > pieces[0] and pieces[2] > pieces[1]: T.append(2) # blue dominant
        if len(T) != 2: continue
        D[tuple(T)].append(num)
    TT = sorted(D.values(), key=lambda x: len(x), reverse=True)
    print(f"ans={sum(TT[0])}")

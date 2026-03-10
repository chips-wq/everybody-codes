"""

   x
  x
 x
C

shooting_power = s

(i1, j1) 

1. (i1 - s, j1 + s)
2. (i1 - s, j1 + 2s)
3. then after some amount of time y
(i1-s+y, j1+2s+y)

i guess try to choose `s` s.t you get it on the same diagonal as yourself.

(p1, p2)
p2-p1 = Y

(i1-s, j1+2s)

j1+2s-i1+s = j1-i1+3s = p2-p1

s = (p2-p1-j1+i1) // 3

Examples:
(1, 1) = C = (i1, j1)
(2, 8) = T = (p1, p2)

8-2-1+1 = 6
6//3 = 2 (shooting power)

sometimes it's not divisible (meaning you can't hit it)
(2, 1) = C = (i1, j1)
(2, 8) = T = (p1, p2)

8-2-1+2 = 7 (can't hit)


s = (p2-p1-j1+i1) // 3
Notice that j1 is always 1
i1 in {0, 1, 2}
p1 in {0, 1, 2}

(p1, p2)
(i, j)
"""
import sys
infile = sys.argv[1]


with open(infile, "r") as f:
    m = f.read().splitlines()
    sources = ['A', 'B', 'C']
    D = {}
    for i, line in enumerate(m):
        for j, el in enumerate(line):
            if el in sources:
                D[el] = (i, j)

    ans = 0
    for i, line in enumerate(m):
        for j, el in enumerate(line):
            if el in ['T', 'H']:
                # What's the least expensive way of taking it down
                b_ranking = float('inf')
                for src, (i1, j1) in D.items():
                    if (j-i-j1+i1) % 3 != 0: continue
                    s = (j-i-j1+i1) // 3
                    ranking = s * (ord(src) - ord('A') + 1)
                    b_ranking = min(b_ranking, ranking)
                assert b_ranking != float('inf')
                if el == 'H': b_ranking *= 2
                ans += b_ranking
    print(f"{ans=}")


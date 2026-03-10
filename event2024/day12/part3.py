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

def get_ways(i: int, j:int, i1: int, j1: int):
    if i2-i == j2-j:
        yield (j2-j, 

with open(infile, "r") as f:
    m = f.read().splitlines()
    sources = ['A', 'B', 'C']
    D = {}
    D['A'] = [(0, 0)]
    D['B'] = [(1, 0)]
    D['C'] = [(2, 0)]

    meteors = []
    for line in m:
        x, y = map(int, line.split())
        meteors.append((y, x))
    # Look at them as (i1, j1)
    # For each meteor, try shooting it using the three different methods
    for i1, j1 in meteors:
        for src, (i, j) in D.items():
            # Method 1.
            if i2-i == j2-j:
                ways.append((

"""
Kruskal's Algorithm
COORDS = (x1, y1), (x2, y2) ... (xn, yn)
           i1         i2          in

1. for every pair, calculate the manhattan distance
ARR = [(d1, i1, i2)), (d2, i1, i3), (d3, i1, i4)...)]
ARR.sort()

forest of trees, 
def find(x: int, y: int, parents: list[int]):
    # are x and y part of the same set

def union(x: int, y: int, parents: list[int]):


Prim's Algorithm
"""

from collections import deque, defaultdict, Counter
import heapq
import sys

def find(x: int, parents: list[int]):
    tmp = x
    while x != parents[x]:
        x = parents[x]
    while tmp != parents[tmp]:
        tmp, parents[tmp] = parents[tmp], x
    assert tmp == x
    return x

def union(x: int, y: int, parents: list[int], sizes: list[int], scores: list[int], c_score: int):
    x = find(x, parents)
    y = find(y, parents)
    if x == y: return
    if sizes[x] < sizes[y]:
        parents[y] = x
        sizes[x] += sizes[y]
        scores[x] += scores[y] + c_score
    else:
        parents[x] = y
        sizes[y] += sizes[x]
        scores[y] += scores[x] + c_score

def same(x: int, y: int, parents: list[int]):
    return find(x, parents) == find(y, parents)

assert len(sys.argv) > 1
infile = sys.argv[1]

with open(infile, "r") as f:
    matrix = f.read().splitlines()
    stars = []
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == '*':
                stars.append((i, j))
    
    n = len(stars)
    A = []
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = stars[i]
            x2, y2 = stars[j]
            D = abs(x1-x2) + abs(y1-y2)
            A.append((D, i, j))
    A.sort()
    parents = [i for i in range(n)]
    sizes = [1] * n
    scores = [0] * n
    
    for D, i, j in A:
        if same(i, j, parents): continue
        if D >= 6: continue
        union(i, j, parents, sizes, scores, D)

    M = {}
    for i in range(n):
        M[find(i, parents)] = sizes[find(i, parents)] + scores[find(i, parents)]

    print("M:")
    for root, VAL in M.items():
        print(f"{root=}, {VAL=}")
    
    vals = sorted(M.values(), reverse=True)
    print(vals[:3])
    ans = 1
    for vv in vals[:3]: ans *= vv
    print(ans)

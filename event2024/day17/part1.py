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

def union(x: int, y: int, parents: list[int], sizes: list[int]):
    x = find(x, parents)
    y = find(y, parents)
    if x == y: return
    if sizes[x] < sizes[y]:
        parents[y] = x
        sizes[x] += sizes[y]
    else:
        parents[x] = y
        sizes[y] += sizes[x]

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
    
    ans = 0
    for D, i, j in A:
        if same(i, j, parents): continue
        ans += D
        union(i, j, parents, sizes)
    SZ = sizes[find(0, parents)]
    print(f"{ans=}, {SZ=}, {ans+SZ=}")

import sys
from collections import deque, defaultdict
from functools import cache
import heapq

sys.setrecursionlimit(9999999)
infile = sys.argv[1]

"""
do some sort of BFS on different bits, change the state of the world based on when you
collect that individual thing"
"""

def solve(si, sj, elements, matrix, graph):
    final_state = (1 << len(elements)) - 1

    # num_nodes * 2 ** len(elements) <- state space
    # 11_730_944 different state to explore in O(1) work

    @cache
    def dp(i, j, state):
        neighs = graph[(i, j)]
        if state == final_state:
            dist_to_root = [dist for (dist, ii, jj) in neighs if (ii, jj) == (si, sj)][0]
            return dist_to_root
        
        # Try out all possible neighbours and take the minimum distance that a certain choice provides
        ans = float('inf')
        for (dist, r, c) in neighs:
            if (r, c) == (si, sj): continue
            idx = elements.index(matrix[r][c])
            if (state >> idx) & 1 == 1: continue
            nstate = state | (1 << idx)
            ans = min(ans, dist + dp(r, c, nstate))
        return ans

    result = dp(si, sj, 0)
    return result

with open(infile, "r") as f:
    matrix = f.read().splitlines()
    matrix = [list(line) for line in matrix]
    si, sj = -1, -1
    for j, el in enumerate(matrix[0]):
        if el == ".":
            si, sj = 0, j
    assert (si, sj) != (-1, -1)

    elements = set()
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el not in ['#', '.', '~']:
                elements.add(el)
    elements = sorted(elements)
    n, m = len(matrix), len(matrix[0])
    print(f"{elements=}, {n=}, {m=}")
    # {"A", "B", "C"}

    graph = defaultdict(list)
    num_edges, num_nodes = 0, 0
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el in elements or (i, j) == (si, sj):
                graph[(i, j)] = bfs_el(i, j, matrix, elements, si, sj)
                num_edges += len(graph[(i, j)])
                num_nodes += 1
    
    assert num_edges == num_nodes * (num_nodes-1)
    print(f"{num_nodes=}")

    result = solve(si, sj, elements, matrix, graph)
    print(f"{result=}")

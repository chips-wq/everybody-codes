import sys
from collections import deque, defaultdict
import heapq

infile = sys.argv[1]

"""
do some sort of BFS on different bits, change the state of the world based on when you
collect that individual thing"
"""
 
def bfs(si, sj, matrix, elements, graph):
    q = [(0, 0, si, sj)]
    SEEN = set()
    heapq.heapify(q)

    D = defaultdict(lambda: float('inf'))
    D[(0, 0, 0)] = 0

    # (visited, i, j)
    # (0000000, i, j)
    # if I visited A, then (0000001, i, j)
    # (0000000, i, j)
    #  ^ represents coming back (after everyone is filledj)
    # ( 
    while q:
        dist, state, ci, cj = heapq.heappop(q)    # (0000000, i, j)

        if (state, ci, cj) in SEEN: continue
        SEEN.add((state, ci, cj))

        # print(f"{dist=}, {bin(state)=}, {ci=}, {cj=}")
        if state == (1 << (len(elements)+1)) - 1:
            print(f"FINAL {dist=}, {bin(state)=}, {ci=}, {cj=}")
            exit(0)

        for (cost, r, c) in graph[(ci, cj)]:
            el = matrix[r][c]
            nstate = state
            if el in elements:
                idx = elements.index(el)
                nstate = nstate | (1 << idx)
            if nstate == (1 << len(elements)) - 1 and (r, c) == (si, sj):
                nstate = nstate | (1 << len(elements))

            if dist + cost < D[(nstate, r, c)]:
                heapq.heappush(q, (dist+cost, nstate, r, c))
                D[(nstate, r, c)] = dist + cost

def bfs_el(si, sj, matrix, elements, ssi, ssj) -> list[tuple[int, int, int]]:
    n, m = len(matrix), len(matrix[0])
    q = deque([(0, si, sj)])

    SEEN = set()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    neighs = []
    while q:
        dist, ci, cj = q.popleft()
        if (ci, cj) in SEEN: continue

        if (ci, cj) != (si, sj):
            if matrix[ci][cj] in elements or (ci, cj) == (ssi, ssj):
                neighs.append((dist, ci, cj))

        SEEN.add((ci, cj))

        for di, dj in dirs:
            r, c = ci + di, cj + dj
            if r < 0 or r >= n or c < 0 or c >= m: continue
            if matrix[r][c] in ['#', '~']: continue
            q.append((dist+1, r, c))
    return neighs

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
    print(f"state_space={2**len(elements) * n * m}")
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

    bfs(si, sj, matrix, elements, graph)

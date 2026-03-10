import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else "part1.in"

def bfs(si: int, sj: int, matrix: list[list[str]]):
    n, m = len(matrix), len(matrix[0])
    q = deque([(si, sj, 0)])
    # (ci, cj, dist)
    S = set([(si, sj)])
    while q:
        ci, cj, dist = q.popleft()

        # [ci, m-ci)
        assert ci <= cj < m-ci
        assert matrix[ci][cj] in ['T', 'E', 'S']
        # try jumping left, right, and either up / down
        if matrix[ci][cj] == 'E':
            print(f"Reached ({ci}, {cj}) in {dist} steps")
            break

        # (cj-ci) % 2 == 0, try jumping up
        # (cj-ci) % 2 == 1, try jumping down
        dirs = [(0, -1), (0, 1)]
        choice = [(-1, 0), (1, 0)]
        # index in this with (cj-ci)%2
        cdirs = dirs + [choice[(cj-ci)%2]]

        for di, dj in cdirs:
            r, c = ci + di, cj + dj
            # [r, m-r)
            if not (r <= c < m-r): continue
            if matrix[r][c] not in ['T', 'E']: continue
            if (r, c) in S: continue
            S.add((r, c))
            q.append((r, c, dist+1))

with open(infile, "r") as f:
    matrix = f.read().splitlines()

    n, m = len(matrix), len(matrix[0])

    si, sj = -1, -1
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == 'S':
                si, sj = i, j

    bfs(si, sj, matrix)



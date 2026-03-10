import sys
from collections import deque

infile = sys.argv[1]
 
def bfs(si, sj, herbs, matrix):
    q = deque([(0, si, sj)])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    SEEN = set()
    n, m = len(matrix), len(matrix[0])
    distm = [[0] * m for _ in range(n)]
    while q:
        dist, ci, cj = q.popleft()
        assert matrix[ci][cj] != '#'
        if (ci, cj) in SEEN: continue

        distm[ci][cj] = dist
        SEEN.add((ci, cj))
        
        for di, dj in dirs:
            r, c = ci + di, cj + dj
            if r < 0 or r >= n or c < 0 or c >= m: continue
            if matrix[r][c] == '#': continue
            q.append((dist+1, r, c))

    """
    for i, j in herbs:
        print(f"to {i=}, {j=}, dist={distm[i][j]}")
    """

    return distm
with open(infile, "r") as f:
    matrix = f.read().splitlines()
    matrix = [list(line) for line in matrix]
    si, sj = -1, -1
    for j, el in enumerate(matrix[0]):
        if el == ".":
            si, sj = 0, j
    assert (si, sj) != (-1, -1)

    herbs = set()
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == 'H':
                herbs.add((i, j))
    distm = bfs(si, sj, herbs, matrix)
    ans = min(distm[i][j] for (i, j) in herbs)
    print(f"{ans*2=}")

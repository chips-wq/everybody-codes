import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else "inp.example"

def bfs(si, sj, ei, ej, matrix):
    q = deque([(si, sj, 0)])
    n, m = len(matrix), len(matrix[0])
    D = [[[-1] * 10 for _ in range(m)] for _ in range(n)]
    D[si][sj][0] = 0
    
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        ci, cj, lvl = q.popleft()

        # change your level or look around and jump if the level is the same
        for nlvl in [(lvl-1) % 10, (lvl+1) % 10]:
            if D[ci][cj][nlvl] != -1: continue
            D[ci][cj][nlvl] = D[ci][cj][lvl] + 1
            q.append((ci, cj, nlvl))

        for di, dj in dirs:
            r, c = ci + di, cj + dj
            if r < 0 or r >= n or c < 0 or c >= m: continue
            if matrix[r][c] != lvl: continue
            if D[r][c][lvl] != -1: continue
            D[r][c][lvl] = D[ci][cj][lvl] + 1
            q.append((r, c, lvl))

    for i in range(n):
        for j in range(m):
            print(f"D[{i}][{j}][0]={D[i][j][0]}")
    ans = D[ei][ej][0]
    print(f"{ans=}")
              

with open(infile, "r") as f:
    matrix = f.read().splitlines()
    matrix = [list(line) for line in matrix]
    si, sj, ei, ej = -1, -1, -1, -1
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == 'S':
                si, sj = i, j
                matrix[i][j] = 0
            if el == 'E':
                ei, ej = i, j
                matrix[i][j] = 0
            if el not in ['#', ' ']:
                matrix[i][j] = int(matrix[i][j])

    print(f"{si=}, {sj=}")
    print(f"{ei=}, {ej=}")
    bfs(si, sj, ei, ej, matrix)


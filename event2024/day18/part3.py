from collections import deque
import sys

infile = sys.argv[1]

def bfs(si, sj, matrix, PP):
    n, m = len(matrix), len(matrix[0])
    q = deque([(si, sj)])
    SEEN = set([(si, sj)])

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    D = [[0] * m for _ in range(n)]

    while q:
        ci, cj = q.popleft()

        for di, dj in dirs:
            r, c = ci + di, cj + dj
            if r < 0 or r >= n or c < 0 or c >= m: continue
            if matrix[r][c] == '#': continue
            if (r, c) in SEEN: continue

            D[r][c] = D[ci][cj] + 1
            SEEN.add((r, c))
            q.append((r, c))

    ans = 0
    for i, j in PP:
        ans += D[i][j]
    return ans


with open(infile, "r") as f:
    matrix = f.read().splitlines()
    matrix = [list(line) for line in matrix]

    PP = []
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == 'P':
                PP.append((i, j))

    n, m = len(matrix), len(matrix[0])
    print(f"{n=}, {m=}")
    ans = float('inf')
    bi, bj = None, None
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == '.':
                cans = bfs(i, j, matrix, PP)
                if cans < ans:
                    ans = cans
                    bi, bj = i, j
    print(f"{bi=}, {bj=}, {ans=}")
            
    


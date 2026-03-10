from collections import deque
import sys

infile = sys.argv[1]

def bfs(starts, matrix):
    n, m = len(matrix), len(matrix[0])
    q = deque(starts)
    SEEN = set(starts)

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

    for line in D:
        print(line)
    return D


with open(infile, "r") as f:
    matrix = f.read().splitlines()
    matrix = [list(line) for line in matrix]

    n, m = len(matrix), len(matrix[0])
    starts = [(1, 0), (n-2, m-1)]
    for si, sj in starts:
        assert matrix[si][sj] == '.'

    D = bfs(starts, matrix)

    PP = []
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == 'P':
                PP.append((i, j))
    ans = max(D[i][j] for (i, j) in PP)
    print(ans)
    


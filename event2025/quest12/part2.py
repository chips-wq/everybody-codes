from collections import deque
import sys

assert len(sys.argv) > 1

infile = sys.argv[1]

def print_mat(matrix: list[list[int]]):
    for line in matrix: 
        print(line)

def bfs(start: list[tuple[int, int]], matrix: list[list[int]]):
    q = deque(start)
    visited = set(start)
    n, m = len(matrix), len(matrix[0])

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        ci, cj = q.popleft()

        for di, dj in dirs:
            r, c = ci + di, cj + dj
            if r < 0 or r >= n or c < 0 or c >= m: continue
            if (r, c) in visited: continue
            if matrix[r][c] > matrix[ci][cj]: continue
            assert matrix[r][c] <= matrix[ci][cj]
            visited.add((r, c))
            q.append((r, c))

    print(f"{len(visited)}=")

with open(infile, "r") as f:
    content = f.read().strip().splitlines()
    matrix = [list(map(int, line)) for line in content]
    n, m = len(matrix), len(matrix[0])
    bfs([(0, 0), (n-1, m-1)], matrix)


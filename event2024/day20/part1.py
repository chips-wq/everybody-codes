from functools import cache
import sys
infile = sys.argv[1]

"""

(i, j, D) -> (i, j+1, 

+1 going right,

(1, 0)    (0, -1)    (-1, 0)    (0, 1)
S,           W,        N,         E
0            1         2          3

if you are going N, and move to W/E then you move to (i, j-1), (i, j+1)
if you are going W, and move to S/N, then you move to(i-1, j), (i+1, j)
(2-1) % 4

"""

DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

INITIAL_ALTITUDE = 1000
NUM_SECONDS = 100
    
with open(infile, "r") as f:
    matrix = f.read().splitlines()
    matrix = [list(line) for line in matrix]

    si, sj = -1, -1
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == 'S': si, sj = i, j


    DSCORE = {
        'S': 0,
        '.': -1,
        '-': -2,
        '+': 1
    }
    n, m = len(matrix), len(matrix[0])

    @cache
    def dp(i, j, ddir, rr):
        assert 0 <= ddir <= 3
        if rr == 0: return 0
        ans = float('-inf')
        for k, (di, dj) in enumerate([DIRS[(ddir-1)%len(DIRS)], DIRS[(ddir)%len(DIRS)], DIRS[(ddir+1)%len(DIRS)]]):
            r, c = i + di, j + dj
            if r < 0 or r >= n or c < 0 or c >= m: continue
            if matrix[r][c] == '#': continue
            dscore = DSCORE[matrix[r][c]]
            # k-1 -> -1, 0, 1
            ans = max(ans, dscore + dp(r, c, (ddir+k-1)%len(DIRS), rr-1))
        return ans
    max_dscore = dp(si, sj, 0, NUM_SECONDS)
    print(f"{max_dscore=}")
    print(f"ans = {INITIAL_ALTITUDE + max_dscore}")

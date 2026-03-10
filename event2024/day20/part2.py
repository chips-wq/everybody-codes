from collections import defaultdict
from string import ascii_letters
from functools import cache
import sys
infile = sys.argv[1]
sys.setrecursionlimit(2*10**9)

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

INITIAL_ALTITUDE = 10000
    
def quick_as(SYM: list[str]):
    n = len(SYM)
    assert n <= 26-1
    assert SYM[0] == 'A'
    for i in range(1, n):
        assert chr(ord(SYM[i-1])+1) == SYM[i]

with open(infile, "r") as f:
    matrix = f.read().splitlines()
    matrix = [list(line) for line in matrix]

    si, sj = -1, -1
    SYM = set()
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el in ascii_letters.upper():
                if el == 'S':
                    si, sj = i, j
                else:
                    SYM.add(el)

    SYM = sorted(SYM)
    quick_as(SYM)
    # S -> chr(ord('A') + len(SYM))
    matrix[si][sj] = chr(ord('A') + len(SYM))
    SYM.append(chr(ord('A')+len(SYM)))
    print(f"{SYM=}")

    DSCORE = {
        '.': -1,
        '-': -2,
        '+': 1
    }
    n, m = len(matrix), len(matrix[0])

    D_ALT = defaultdict(lambda: float('-inf'))

    @cache
    def dp(i, j, ddir, alt, visited):
        assert 0 <= ddir <= 3
        # (i, j, ddir, visited) -> max altitude here

        if D_ALT[(i, j, ddir, visited)] >= alt: return float('inf')
        D_ALT[(i, j, ddir, visited)] = alt

        # Have i been here at a higher altitude ?
        print(f"{i=}, {j=}, {bin(visited)=}, {alt=}")
        if (i, j) == (si, sj) and visited == (1 << len(SYM))-1:
            return 0
            if alt >= INITIAL_ALTITUDE: return 0
            return float('inf')

        ans = float('inf')
        for k, (di, dj) in enumerate([DIRS[(ddir-1)%len(DIRS)], DIRS[(ddir)%len(DIRS)], DIRS[(ddir+1)%len(DIRS)]]):
            r, c = i + di, j + dj
            if r < 0 or r >= n or c < 0 or c >= m: continue
            if matrix[r][c] == '#': continue
            dalt = DSCORE[matrix[r][c]] if matrix[r][c] in ['.', '-', '+'] else -1
            dvisited = 0
            if matrix[r][c] in ascii_letters.upper():
                assert matrix[r][c] in SYM
                idx = SYM.index(matrix[r][c])
                if (((1<<idx)-1) & visited) == visited:
                    dvisited = (1 << idx)
            ans = min(ans, 1 + dp(r, c, (ddir-1+k)%len(DIRS), alt + dalt, visited | dvisited))
            # k-1 -> -1, 0, 1
        return ans

    min_seconds = dp(si, sj, 0, INITIAL_ALTITUDE, 0)
    print(f"{min_seconds=}")

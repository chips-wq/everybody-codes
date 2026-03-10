import sys
from collections import deque

# find an index mapping i guess and just run bfs
# or store all three maps in memory.. and index them based on `dist % 3`

infile = sys.argv[1] if len(sys.argv) > 1 else "part1.in"

def pretty_print(matrix: list[list[str]]):
    for line in matrix:
        print("".join(line))


def rotate_op(matrix: list[list[str]]):
    n, m = len(matrix), len(matrix[0])

    res = [['.'] * m for _ in range(n)]

    # DIAGS = [] 
    for i in range(n-1, -1, -1):
        ii = i
        # (i, m-i-1)
        j = m-i-1
        cdiag = []
        # up, left, up, left
        kk = 0
        while i >= 0:
            cdiag.append(matrix[i][j])
            if kk % 2 == 0:
                i -= 1
            else:
                j -= 1
            kk += 1
        # print("".join(cdiag))
        # line is n-1-i, so n-1-i+idx
        for idx, el in enumerate(cdiag):
            res[n-1-ii][n-1-ii+idx] = el
        
        # DIAGS.append(cdiag)
    return res

def bfs(si: int, sj: int, D):
    n, m = len(matrix), len(matrix[0])
    q = deque([(si, sj, 0, 0)])
    # (ci, cj, dist)
    S = set([(si, sj, 0)])
    # there's actually multiple graphs here (ci, cj, graph_idx)
    # because you may get to some (i1, j1, g1) faster / slower than in another graph
    # is the state explosion too bad ?
    # (n * m * 3)
    while q:
        ci, cj, gidx, dist = q.popleft()

        assert 0 <= gidx < 3
        m0 = D[gidx]
        # [ci, m-ci)
        assert ci <= cj < m-ci
        assert m0[ci][cj] in ['T', 'E', 'S']
        # try jumping left, right, and either up / down
        if m0[ci][cj] == 'E':
            print(f"Reached ({ci}, {cj}) in {dist} steps")
            break

        # (cj-ci) % 2 == 0, try jumping up
        # (cj-ci) % 2 == 1, try jumping down
        dirs = [(0, 0), (0, -1), (0, 1)]
        choice = [(-1, 0), (1, 0)]
        # index in this with (cj-ci)%2
        cdirs = dirs + [choice[(cj-ci)%2]]

        m1 = D[(gidx+1)%3]
        for di, dj in cdirs:
            r, c = ci + di, cj + dj
            # [r, m-r)
            if not (r <= c < m-r): continue
            if m1[r][c] not in ['T', 'E']: continue
            if (r, c, (gidx+1)%3) in S: continue
            S.add((r, c, (gidx+1)%3))
            q.append((r, c, (gidx+1)%3, dist+1))

with open(infile, "r") as f:
    matrix = f.read().splitlines()

    n, m = len(matrix), len(matrix[0])

    D = {}
    r0 = matrix
    # print("r0=")
    # pretty_print(r0)

    r1 = rotate_op(r0)
    # print("r1=")
    # pretty_print(r1)

    r2 = rotate_op(r1)
    # print("r2=")
    # pretty_print(r2)

    D[0] = r0
    D[1] = r1
    D[2] = r2

    print(f"{n=}, {m=}")

    si, sj = -1, -1
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == 'S':
                si, sj = i, j

    bfs(si, sj, D)



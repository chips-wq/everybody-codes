import heapq
import sys

infile = "part1.in" if len(sys.argv) < 1 else sys.argv[1]

"""
as you increase the radius,
for a radius R you get 

[0, 30) -> with a radius of 0
[30, 60) -> with a radius of 1
[60, 90) -> with a radius of 2 (with a radius of 2, anything <90 seconds is viable)

you can try with a radius of 1, 2, 3, ... sqrt(N) + 5


Suppose you have a radius of R, and a function F(R) that lets you know how many seconds it takes

anything in < (R+1) * 30 is valid

How do I compute F(R)

What are the characteristics of a closed loop around something in the graph ?

in the path, there exists an
i1, j1 s.t

(i1 < vx)
(j1 < vy)
and an (i2, j2) s.t

i2 > vx
j2 > vy


think of the nodes as:

(i, j, cnt)
cnt is computed as to how many corners you got

every single time you step onto a new node, you can now see your neighbours

and you want to compute the shortest path from

(si, sj, 0) to (si, sj, 4)

I think this would work.

the idea of the loop is enclosed in the graph structure and applying dijkstra esentially
selects the one with the smallest "distance" in this graph

always prune if your distance >= (R+1) * 30

(i, j), (ul, bl, br, ur)
          0   0   0   0

encoded as a 4bit number

a single coordinate can only satisfy one of those
def satisfy(i: int, j: int):
    if i < xv and j < yv: return (1 << 3)
    if i > xv and j < yv: return (1 << 2)
    if i > xv and j > yv: return (1 << 1)
    if i < xv and j > yv: return (1 << 0)
    return 0

this changes as 

(xv, yv) nu e folosit acm in dijkstra

(i, j), (aligned_left, aligned_bottom, aligned_right, aligned_top)


        S
        |
        |
        |
========@========
        |
        |
        |
        |

"""

def dijkstra(si: int, sj: int, vx: int, vy: int, matrix: list[list[int]], R: int):
    def satisfy(i: int, j: int):
        if i < vx and j < vy: return (1 << 3)
        if i > vx and j < vy: return (1 << 2)
        if i > vx and j > vy: return (1 << 1)
        if i < vx and j > vy: return (1 << 0)
        return 0

    def satisfy2(i: int, j: int):
        if i == vx and j < vy: return (1 << 3)
        if i > vx and j == vy: return (1 << 2)
        if i == vx and j > vy: return (1 << 1)
        if i < vx and j == vy: return (1 << 0)
        return 0

    def aligned(i: int, j: int):
        if i == vx: return True
        if j == vy: return True
        return False

    assert satisfy2(si, sj) == 1
    q = [(0, (si, sj, satisfy2(si, sj)))]
    heapq.heapify(q)

    n, m = len(matrix), len(matrix[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    S = set()
    # D[i][j][conf]
    D = [[[float('inf')] * 16 for _ in range(m)] for _ in range(n)]
    P = [[[None] * 16 for _ in range(m)] for _ in range(n)]
    D[si][sj][1] = 0
    P[si][sj][1] = (si, sj, 1)
    assert P[si][sj][(1<<4)-1] == None

    # We are gonna prune if dist >= (R+1) * 30
    while q:
        dist, (i, j, conf) = heapq.heappop(q)
        # (i, j, conf) should be unique (we should never revisit those)
        if (i, j, conf) in S: continue
        S.add((i, j, conf))
        
        for di, dj in dirs:
            r, c = i + di, j + dj
            dconf = satisfy2(r, c)
            new_conf = (conf | dconf)
            # Try jumping to (r, c, new_conf)
            if r < 0 or c < 0 or r >= n or c >= m: continue
            if (r-vx) * (r-vx) + (c-vy) * (c-vy) <= R * R: continue
            # Just try relaxing it and if you can relax it, add it to the Q
            edge_dist = float('inf')
            if matrix[r][c] == 'S':
                edge_dist = 0
            elif matrix[r][c] != '@':
                edge_dist = int(matrix[r][c])
            if dist + edge_dist >= (R+1) * 30: continue
            # in case dconf bit is already set, discourage going there harshly
            # or just don't allow to go there I guess
            # if aligned(i, j) and (conf & dconf) > 0: continue


            if dist + edge_dist < D[r][c][new_conf]:
                P[r][c][new_conf] = (i, j, conf)
                D[r][c][new_conf] = dist + edge_dist
                heapq.heappush(q, (dist+edge_dist, (r, c, new_conf)))
    # for pp in range(16):
    #     print(f"pp={bin(pp)}, D[si][sj][pp]={D[si][sj][pp]}")
    path = set((si, sj))
    if D[si][sj][(1<<4)-1] < (R+1) * 30:
        assert P[si][sj][(1<<4)-1]
        ci, cj, cnf = si, sj, (1<<4)-1
        assert P[si][sj][1] == (si, sj, 1)
        while (ci, cj, cnf) != (si, sj, 1):
            # path.add((ci, cj, cnf))
            path.add((ci, cj))
            ci, cj, cnf = P[ci][cj][cnf]

    return (path, D[si][sj][(1<<4)-1])

def pretty_print(path, matrix, si, sj, vx, vy, R):
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if (vx-i) * (vx-i) + (vy-j) * (vy-j) <= R*R:
                print(".", end="")
            elif (i, j) in path:
                if (i, j) == (si, sj):
                    print("S", end="")
                else:
                    print("#", end="")
            else:
                print(el, end="")
        print()
    print()

def volcano_coords(matrix: list[list[str]]):
    xv, yv = -1, -1
    n, m = len(matrix), len(matrix[0])
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == '@':
                xv, yv = i, j

    assert (xv != -1)
    assert (yv != -1)
    return (xv, yv)

def start_coords(matrix: list[list[str]]):
    si, sj = -1, -1
    n, m = len(matrix), len(matrix[0])
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == 'S':
                si, sj = i, j

    assert (si != -1)
    assert (sj != -1)
    return (si, sj)

# 50-0 * 50-0 + 50-0 * 50-0 = 2500 + 2500 = 5000
# sqrt(5000) << 5000

with open(infile, "r") as f:
    matrix = f.read().splitlines()
    n, m = len(matrix), len(matrix[0])
    print(f"{n=}, {m=}")
    xv, yv = volcano_coords(matrix)
    si, sj = start_coords(matrix)
    print(f"{si=}, {sj=}")
    print(f"{xv=}, {yv=}")
    # R = 110
    R = 110

    for K in range(R+1):
        path, best_dist = dijkstra(si, sj, xv, yv, matrix, K)
        if best_dist != float('inf'):
            print(f"{K=}")
            print(f"{best_dist=}")
            assert best_dist < (K+1) * 30
            pretty_print(path, matrix, si, sj, xv, yv, K)
            print(f"ans={K * best_dist}")
            print()

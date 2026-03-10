from collections import deque
import sys

#    0      1        2       3
#                         initially
# (0, 1), (1, 0), (0, -1), (-1, 0)
#   E        S       W        N

# if you start out on R -> dirs[0]
# if you start out on L -> dirs[2]

# R -> means current index + 1
# L -> means current index - 1


def bfs(si: int, sj: int, ei: int, ej: int, P: set[tuple[int, int]]):
    visited = set(P)
    q = deque([(si, sj, 0)])
    
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        ci, cj, dist = q.popleft()

        for di, dj in dirs:
            r, c = ci + di, cj + dj
            if (r, c) == (ei, ej):
                return dist+1
            if (r, c) in visited: continue
            visited.add((r, c))
            q.append((r, c, dist+1))
    assert False


def add_path(ci: int, cj: int, direction: tuple[int, int], times: int, P: set[tuple[int, int]]):
    di, dj = direction
    
    for _ in range(times):
        ci += di
        cj += dj
        
        assert (ci, cj) not in P
        P.add((ci, cj))

    return (ci, cj)
    
infile = sys.argv[1]
with open(infile, "r") as f:
    instructions = f.read().split(",")
    start = (0, 0)
    P = set([start])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 3

    position = start

    for instruction in instructions:
        typ, amount = instruction[0], instruction[1:]
        amount = int(amount)
        if typ == 'L':
            dir_idx = (dir_idx - 1) % 4
        elif typ == 'R':
            dir_idx = (dir_idx + 1) % 4
        else:
            assert False
        position = add_path(position[0], position[1], dirs[dir_idx], amount, P)

    print(P)
    print(position)

    distance = bfs(0, 0, position[0], position[1], P)
    print(f"{distance=}")




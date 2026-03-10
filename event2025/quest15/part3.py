import heapq
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

    I = []

    ci, cj = 0, 0
    I.append((0, 0))

    max_amount = -1

    dir_idx = 3
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i, instruction in enumerate(instructions):
        typ, amount = instruction[0], instruction[1:]
        amount = int(amount)

        max_amount = max(max_amount, amount)
        if typ == 'L':
            dir_idx = (dir_idx - 1) % 4
        elif typ == 'R':
            dir_idx = (dir_idx + 1) % 4
        else:
            assert False
        cdir = dirs[dir_idx]
        
        ci += cdir[0] * amount
        cj += cdir[1] * amount
        I.append((ci, cj))

    Is = []
    Js = []

    for (ci, cj) in I:
        Is.append(ci-1)
        Is.append(ci)
        Is.append(ci+1)

        Js.append(cj-1)
        Js.append(cj)
        Js.append(cj+1)
    
    Is = sorted(set(Is))
    Js = sorted(set(Js))

    # Do one of the mappings
    bigToSmolI = {el: i for i, el in enumerate(Is)}
    bigToSmolJ = {el: i for i, el in enumerate(Js)}

    N = len(I)
    WALL = set()
    for i in range(1, N):
        old_i, old_j = bigToSmolI[I[i-1][0]], bigToSmolJ[I[i-1][1]]
        new_i, new_j = bigToSmolI[I[i][0]], bigToSmolJ[I[i][1]]
        
        # it ought to be that either old_i == new_i or old_j == new_j
        assert (old_i==new_i) or (old_j==new_j)
        for rr in range(min(old_i, new_i), max(old_i, new_i)+1):
            for cc in range(min(old_j, new_j), max(old_j, new_j)+1):
                WALL.add((rr, cc))
    rf, cf = (bigToSmolI[I[N-1][0]], bigToSmolJ[I[N-1][1]])
    si, sj = (bigToSmolI[0], bigToSmolJ[0])

    WALL.remove((rf, cf))
    WALL.remove((si, sj))
 
    # Now you just built the walls in the smaller graph
    R = len(Is)
    C = len(Js)
    print(f"{R=}")
    print(f"{C=}")
    # I now have a 363x363 graph
    for r in range(R):
        row = []
        for c in range(C):
            # Is this precisely one of the turning points ?
            if (Is[r], Js[c]) == (0, 0):
                row.append('S')
            elif (Is[r], Js[c]) == (I[N-1][0], I[N-1][1]):
                row.append('E')
            elif (Is[r], Js[c]) in I:
                row.append('X')
            elif (r, c) in WALL:
                row.append('#')
            else:
                row.append('.')
        print("".join(row))
                
    """
    1 2 3
    4 5 6
    7 8 9


    """
    # Now run dijkstra
    si, sj = (bigToSmolI[0], bigToSmolJ[0])
    heap = [(0, si, sj)]
    D = {}

    # SEEN = FINISHED
    SEEN = set()
    D[(si, sj)] = 0

    
    while heap:
        dd, ci, cj = heapq.heappop(heap)

        assert (ci, cj) not in WALL
        if (ci, cj) in SEEN: continue

        if (Is[ci], Js[cj]) == (I[N-1][0], I[N-1][1]):
            print("Found result")
            print(f"{I[N-1][0]=}, {I[N-1][1]=}, {dd=}")
        
        SEEN.add((ci, cj))
        
        for di, dj in dirs:
            r, c = ci + di, cj + dj
            # Those must be valid coordinates in the new graph
            if r < 0 or r >= len(Is) or c < 0 or c >= len(Js): continue
            if (r, c) in WALL: continue
            # What is the distance to this point
            nD = abs(Is[r] - Is[ci]) + abs(Js[c] - Js[cj])
            if dd + nD < D.get((r, c), float('inf')):
                D[(r, c)] = dd + nD
                heapq.heappush(heap, (dd+nD, r, c))
    
    # print(f"{max_amount=}")
    # for ii in I:
    #     print(ii)
    # print(f"{len(I)=}")
    # print(f"{Is=}")
    # print(f"{Js=}")

from collections import deque
import sys

infile = sys.argv[1]

def vec_mult(vec: list[int], am: int) -> list[int]:
    v = [0] * len(vec)
    for i, el in enumerate(vec):
        v[i] = el * am
    return v

def vec_add(v1: list[int], v2: list[int]) -> list[int]:
    assert len(v1) == len(v2)
    v = [0] * len(v1)
    for i, (e1, e2) in enumerate(zip(v1, v2)):
        v[i] = e1 + e2
    return v

D = {
    'U': [0, 1, 0],
    'D': [0, -1, 0],
    'L': [-1, 0, 0],
    'R': [1, 0, 0],
    'F': [0, 0, 1],
    'B': [0, 0, -1]
}

def get_Ds(vec: list[int], am: int):
    for i in range(1, am+1):
        S = vec_mult(vec, i)
        yield tuple(S)

def run_segment(cmds: list[str]):
    current = [0,0,0]
    ans = -1
    S = set()
    for cmd in cmds:
        _dir = cmd[0]
        am = int(cmd[1:])

        for DD in get_Ds(D[_dir], am):
            B = vec_add(current, DD)
            S.add(tuple(B))

        dV = vec_mult(D[_dir], am)
        current = vec_add(current, dV)
        ans = max(ans, current[1])
    return S, ans, tuple(current)

def bfs(start: list[int], S: set[tuple[int, int, int]], leaves: set[tuple[int, int, int]]):
    assert len(start) == 3
    q = deque([start])
    D = {}
    D[tuple(start)] = 0
    dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]

    while q:
        C = q.popleft()
        
        for dVec in dirs:
            N = vec_add(C, dVec)
            if tuple(N) not in S: continue
            if tuple(N) in D: continue
            D[tuple(N)] = D[tuple(C)] + 1
            q.append(N)

    ans = 0
    for leaf in leaves:
        if leaf not in D: continue
        # assert leaf in D
        ans += D[leaf]
    return ans

with open(infile, "r") as f:
    lines = f.read().splitlines()
    S = set()
    leaves = set()
    mH = -1
    for line in lines:
        dS, cH, leaf = run_segment(line.split(","))
        mH = max(mH, cH)
        S.update(dS)
        leaves.add(leaf)

    # directly above the starting point
    # (0, x > 0, 0)
    assert (0,0,0) not in S
    bAns = float('inf')
    for h in range(1, mH+1):
        v = (0, h, 0)
        ans = bfs(v, S, leaves)
        if ans == 0: continue
        bAns = min(bAns, ans)
        print(f"{v=}, {ans=}")
    print(f"{bAns=}")

    print(f"{mH=}")
    print(f"{len(S)=}")
    print(f"{len(leaves)=}")

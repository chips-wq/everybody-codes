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
        print(current)
    return S

with open(infile, "r") as f:
    lines = f.read().splitlines()
    S = set()
    for line in lines:
        dS = run_segment(line.split(","))
        S.update(dS)
    print(f"{len(S)=}")
    
        

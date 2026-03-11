from collections import deque
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "example1.in"

MAX_EXPLORED = 1000
MAP_RANGE = 75

def capped_bfs(i: int, j: int, S: set[tuple[int, int]]):
    q = deque([(i, j)])
    
    S2 = set(S)
    S2.add((i, j))

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    explored = 0

    while q and explored < MAX_EXPLORED:
        ci, cj = q.popleft()
        explored += 1
        
        for di, dj in dirs:
            r, c = ci + di, cj + dj
            if (r, c) in S2: continue
            S2.add((r, c))
            q.append((r, c))

    # It means this was capped, i.e not open space
    if not q:
        S.update(S2)
        return True
    return False

def run(si: int, sj: int, endings: list[tuple[int, int]], matrix: list[list[str]], S2):
    ci, cj = si, sj
    dirs = [(-1, 0), (-1, 0), (-1, 0), (0, 1), (0, 1), (0, 1), (1, 0), (1, 0), (1, 0), (0, -1), (0, -1), (0, -1)]
    dirs_orig = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    #          ^       >       d       <
    S = set([(si, sj)])
    S.update(S2)
    cdir = 0
    steps = 0
    def stop_condition():
        return all((all((ei + di, ej + dj) in S for di, dj in dirs) for ei, ej in endings))

    while not stop_condition():
        # Take the first possible move
        # or would jumping in this direction lead to a dead end (i. e supposing we do a bfs inside to the left here it's capped)
        while (ci + dirs[cdir][0], cj + dirs[cdir][1]) in S:
            cdir = (cdir + 1) % len(dirs)

        di, dj = dirs[cdir]
        ci += di
        cj += dj
        print(f"{steps=}")
        print_matrix(ci, cj, endings, S, matrix)
        assert (ci, cj) not in S
        S.add((ci, cj))
        # Is it possible that I blocked stuff to my left / right ?
        # first just do +cdir, (+cdir+(cdir-1)), (+cdir+(cdir+1))
        assert 0 <= cdir < len(dirs)
        cdir2 = cdir//3
        posz = [(ci + dirs_orig[cdir2][0], cj + dirs_orig[cdir2][1]), (ci + dirs_orig[cdir2][0] + dirs_orig[(cdir2-1)%len(dirs_orig)][0], cj + dirs_orig[cdir2][1] + dirs_orig[(cdir2-1)%len(dirs_orig)][1]), (ci + dirs_orig[cdir2][0] + dirs_orig[(cdir2+1)%len(dirs_orig)][0], cj + dirs_orig[cdir2][1] + dirs_orig[(cdir2+1)%len(dirs_orig)][1])]
        # Does any of posz in S? if yes then try filling up with capped bfs
        if any((r, c) in S for (r, c) in posz):
            # Try filling up at (ci + dirs_orig[(cdir2-1)%len(dirs_orig)][0], cj + dirs_orig[(cdir2-1)%len(dirs_orig)][1]) and at (ci + dirs_orig[(cdir2+1)%len(dirs_orig)][0], cj + dirs_orig[(cdir2+1)%len(dirs_orig)][1])
            r1, c1 = (ci + dirs_orig[(cdir2-1)%len(dirs_orig)][0], cj + dirs_orig[(cdir2-1)%len(dirs_orig)][1])
            r2, c2 = (ci + dirs_orig[(cdir2+1)%len(dirs_orig)][0], cj + dirs_orig[(cdir2+1)%len(dirs_orig)][1])
            r3, c3 = (ci + dirs_orig[cdir2][0], cj + dirs_orig[cdir2][1])
            if (r1, c1) not in S:
                cbfs1 = capped_bfs(r1, c1, S)
                print(f"{cbfs1=}")
            if (r2, c2) not in S:
                cbfs2 = capped_bfs(r2, c2, S)
                print(f"{cbfs2=}")
            if (r3, c3) not in S:
                cbfs3 = capped_bfs(r3, c3, S)
                print(f"{cbfs3=}")

        cdir = (cdir + 1) % len(dirs)
        steps += 1
    return steps
        
def print_matrix(ci: int, cj: int, endings, S: set[tuple[int, int]], matrix: list[list[str]]):
    def d_conv(i: int, j: int):
        if (i, j) in endings: return '#'
        if (i, j) in S: return '+'
        if (i, j) == (ci, cj): return '@'
        return '.'
        
    for i in range(-MAP_RANGE, MAP_RANGE):
        pline = ''.join(d_conv(i, j) for j in range(-MAP_RANGE, MAP_RANGE))
        print(pline)
    print()

with open(infile, "r") as f:
    matrix = [list(line) for line in f.read().splitlines()]
    si, sj = -1, -1
    endings = []
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == '@':
                si, sj = i, j
            if el == '#':
                endings.append((i, j))

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    S2 = set(endings)
    for ei, ej in endings:
        for di, dj in dirs:
            r, c = ei + di, ej + dj
            capped_bfs(r, c, S2)

    ans = run(si, sj, endings, matrix, S2)

    print(f"{ans=}")
    

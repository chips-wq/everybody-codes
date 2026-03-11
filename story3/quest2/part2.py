from collections import deque
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "example1.in"

MAP_RANGE = 75
# is there a direction where 1000 is free
# return true if it's an ok condition
def bad_test(ci: int, cj: int, ei: int, ej: int, cdir: int, dirs: list[tuple[int, int]], S: set[tuple[int, int]]):
    ci, cj = (ci + dirs[cdir][0], cj + dirs[cdir][1])
    #assert (ci, cj) not in S
    # Am I trapped ?
    trapped = all((ci + di, cj + dj) in S for di, dj in dirs)
    if trapped: S.add((ci, cj))
    return trapped

def run(si: int, sj: int, ei: int, ej: int, matrix: list[list[str]]):
    ci, cj = si, sj
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    S = set([(si, sj), (ei, ej)])
    cdir = 0
    steps = 0
    while not all((ei + di, ej + dj) in S for di, dj in dirs):
        # Take the first possible move
        # or would jumping in this direction lead to a dead end (i. e supposing we do a bfs inside to the left here it's capped)
        while (ci + dirs[cdir][0], cj + dirs[cdir][1]) in S or bad_test(ci, cj, ei, ej, cdir, dirs, S):
            cdir = (cdir + 1) % len(dirs)

        di, dj = dirs[cdir]
        ci += di
        cj += dj
        print_matrix(ci, cj, ei, ej, S, matrix)
        assert (ci, cj) not in S
        S.add((ci, cj))

        bad_test(ci, cj, ei, ej, cdir, dirs, S)

        cdir = (cdir + 1) % len(dirs)
        steps += 1
    return steps
        
def print_matrix(ci: int, cj: int, ei: int, ej: int, S: set[tuple[int, int]], matrix: list[list[str]]):
    def d_conv(i: int, j: int):
        if (i, j) == (ei, ej): return '#'
        if (i, j) in S: return '+'
        if (i, j) == (ci, cj): return '@'
        return '.'
        
    for i in range(-MAP_RANGE, MAP_RANGE):
        pline = ''.join(d_conv(i, j) for j in range(-MAP_RANGE, MAP_RANGE))
        print(pline)
    print()

with open(infile, "r") as f:
    matrix = [list(line) for line in f.read().splitlines()]
    ei, ej, si, sj = -1, -1, -1, -1
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == '@':
                si, sj = i, j
            if el == '#':
                ei, ej = i, j
    ans = run(si, sj, ei, ej, matrix)
    print(f"{ans=}")
    

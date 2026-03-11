import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "example1.in"

def run(si: int, sj: int, ei: int, ej: int, matrix: list[list[str]]):
    ci, cj = si, sj
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    S = set([(si, sj)])
    cdir = 0
    steps = 0
    while (ci, cj) != (ei, ej):
        # Take the first possible move
        while (ci + dirs[cdir][0], cj + dirs[cdir][1]) in S:
            cdir = (cdir + 1) % len(dirs)

        di, dj = dirs[cdir]
        ci += di
        cj += dj
        print_matrix(ci, cj, ei, ej, S, matrix)
        assert (ci, cj) not in S
        S.add((ci, cj))

        cdir = (cdir + 1) % len(dirs)
        steps += 1
    return steps
        
def print_matrix(ci: int, cj: int, ei: int, ej: int, S: set[tuple[int, int]], matrix: list[list[str]]):
    def d_conv(i: int, j: int, el: str):
        if (i, j) in S: return '+'
        if (i, j) == (ci, cj): return '@'
        if (i, j) == (ei, ej): return '#'
        return el
        
    for i, line in enumerate(matrix):
        pline = ''.join(d_conv(i, j, el) for j, el in enumerate(line))
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
    

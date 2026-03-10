import sys

infile = "part1.in" if len(sys.argv) < 1 else sys.argv[1]

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

def exact_radius(matrix: list[list[str]], R: int, xv: int, yv: int):
    ss = 0
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == '@': continue
            if (xv-i) * (xv-i) + (yv-j) * (yv-j) <= R * R:
                ss += int(matrix[i][j])
    return ss

# 50-0 * 50-0 + 50-0 * 50-0 = 2500 + 2500 = 5000
# sqrt(5000) << 5000

with open(infile, "r") as f:
    matrix = f.read().splitlines()
    n, m = len(matrix), len(matrix[0])
    print(f"{n=}, {m=}")
    xv, yv = volcano_coords(matrix)
    R = 100

    best, ans = float('-inf'), float('-inf')
    before = 0
    for K in range(1, R+1):
        ss = exact_radius(matrix, K, xv, yv)
        destruction_step = ss-before
        if destruction_step > best:
            best = destruction_step
            ans = destruction_step * K
        
        print(f"{ss-before=}, {K=}")
        before = ss
    print(f"{ans=}")
    print(f"{best=}")

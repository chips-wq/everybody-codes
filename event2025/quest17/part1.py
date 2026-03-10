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

with open(infile, "r") as f:
    matrix = f.read().splitlines()
    n, m = len(matrix), len(matrix[0])
    xv, yv = volcano_coords(matrix)
    R = 10

    ans = 0
    for i in range(n):
        for j in range(m):
            # check if (i, j) respects the formula
            if (xv-i) * (xv-i) + (yv - j) * (yv - j) <= R * R:
                if matrix[i][j] == '@': continue
                ans += int(matrix[i][j])
    print(f"{ans=}")

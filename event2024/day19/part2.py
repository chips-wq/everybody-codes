import sys

infile = sys.argv[1]

DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def rotate_right(i, j, matrix):
    assert len(DIRS) == 8
    n, m = len(matrix), len(matrix[0])
    assert 1 <= i <= n-2
    assert 1 <= j <= m-2

    for k in range(len(DIRS)-1, 0, -1):
        cx, cy = DIRS[(k)%len(DIRS)]
        nx, ny = DIRS[(k-1)%len(DIRS)]
        cx, cy = i + cx, j + cy
        nx, ny = i + nx, j + ny
        matrix[cx][cy], matrix[nx][ny] = matrix[nx][ny], matrix[cx][cy]

def rotate_left(i, j, matrix):
    assert len(DIRS) == 8
    n, m = len(matrix), len(matrix[0])
    assert 1 <= i <= n-2
    assert 1 <= j <= m-2

    for k in range(len(DIRS)-1):
        cx, cy = DIRS[(k)%len(DIRS)]
        nx, ny = DIRS[(k+1)%len(DIRS)]
        cx, cy = i + cx, j + cy
        nx, ny = i + nx, j + ny
        matrix[cx][cy], matrix[nx][ny] = matrix[nx][ny], matrix[cx][cy]

def pretty_print(matrix):
    for line in matrix:
        print("".join(line))

ROUNDS = 1

with open(infile, "r") as f:
    instructions, matrix = f.read().split('\n\n')
    matrix = matrix.splitlines()
    matrix = [list(line) for line in matrix]

    n, m = len(matrix), len(matrix[0])
    pretty_print(matrix)

    for _ in range(ROUNDS):
        k = 0
        for i in range(1, n-1):
            for j in range(1, m-1):
                instr = instructions[k%len(instructions)]
                if instr == 'L':
                    rotate_left(i, j, matrix)
                if instr == 'R':
                    rotate_right(i, j, matrix)

                k += 1

    print()
    pretty_print(matrix)


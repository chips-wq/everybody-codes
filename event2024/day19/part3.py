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

# there is a mapping 
# initialize a matrix with i*m + j
# run the algorithm
# you know that i*m+j -> mat[i][j]

def get_permutation(n: int, m: int, instructions: list[str]):
    matrix = [[0] * m for _ in range(n)]
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            matrix[i][j] = i * m + j
    
    # (n-1) * m + m-1 = n * m - m + m - 1 = n * m - 1
    # notice that even (0, 0) changes
    permutation = [0] * (n * m)

    k = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            instr = instructions[k%len(instructions)]
            if instr == 'L':
                rotate_left(i, j, matrix)
            if instr == 'R':
                rotate_right(i, j, matrix)

            k += 1
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            permutation[i*m+j] = matrix[i][j]

    return permutation

def perm_mult(perm1: list[int], perm2: list[int]):
    n, m = len(perm1), len(perm2)
    assert n == m
    for (x, y) in zip(perm1, perm2):
        assert 0 <= x < n
        assert 0 <= y < n
    # imagine perm1 as the identity permutation perm1[i] = i
    perm = [0] * n
    for i in range(n):
        perm[i] = perm2[perm1[i]]
    return perm
    

def raise_perm(permutation: list[int], x: int):
    n = len(permutation)
    if x == 0:
        return [i for i in range(n)]
    if x % 2:
        return perm_mult(permutation, raise_perm(permutation, x-1))
    pp = raise_perm(permutation, x//2)
    return perm_mult(pp, pp)

ROUNDS = 1048576000
# ROUNDS = 100

def main():
    with open(infile, "r") as f:
        instructions, matrix = f.read().split('\n\n')
        matrix = matrix.splitlines()
        matrix = [list(line) for line in matrix]

        n, m = len(matrix), len(matrix[0])
        
        perm = get_permutation(n, m, instructions)
        perm = raise_perm(perm, ROUNDS)

        # print("BEFORE:")
        # pretty_print(matrix)
        # raise_perm(one_round_perm, ROUNDS)

        new_matrix = [list(line) for line in matrix]
        for i in range(n):
            for j in range(m):
                # map this bad boy back up
                # where did i*m+j -> (i, j) go to, it went to (perm[i*m+j]//m, perm[i*m+j]%m)
                i2, j2 = perm[i*m+j]//m, perm[i*m+j]%m
                new_matrix[i][j] = matrix[i2][j2]

        # print("AFTER:")
        pretty_print(new_matrix)

main()

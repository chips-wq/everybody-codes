import sys

assert len(sys.argv) > 1


def play_round(matrix: list[list[str]]):
    n, m = len(matrix), len(matrix[0])
    ret = [list(line) for line in matrix]
    
    dirs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            # Number of active diagonal neighbours
            num_active = 0
            for di, dj in dirs:
                r, c = i + di, j + dj
                if r < 0 or r >= n or c < 0 or c >= m: continue
                if matrix[r][c] == '#':
                    num_active += 1
            # Apply rules
            if matrix[i][j] == '#' and num_active % 2 == 0:
                ret[i][j] = '.'
            if matrix[i][j] == '.' and num_active % 2 == 0:
                ret[i][j] = '#'
    return ret

def count_active(matrix: list[list[str]]):
    num_active = sum(sum(1 for el in line if el == '#') for line in matrix)
    return num_active

def print_mat(matrix: list[list[str]]):
    for line in matrix:
        print("".join(line))

infile = sys.argv[1]
with open(infile, "r") as f:
    matrix = [list(line) for line in f.read().splitlines()]

    rounds = []
    for _ in range(10):
        matrix = play_round(matrix)
        rounds.append(count_active(matrix))
    print(rounds)
    ans = sum(rounds)
    print(f"{ans=}")

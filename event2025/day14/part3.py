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

def does_match(matrix: list[list[str]], pattern: list[list[str]], m_i, m_j):
    for i, line in enumerate(pattern):
        for j, el in enumerate(line):
            if el != matrix[m_i+i][m_j+j]:
                return False
    return True

def solve():
    arr = [(183, 580), (325, 572), (1097, 636), (1101, 648), (1451, 576), (1697, 588), (2204, 628)]
    y = 1_000_000_000
    period = 4095

    ans = 0
    for rr, val in arr:
        ans += (int((y-rr)/period) + 1) * val
    print(ans)

def solve1():
    arr = [(125, 552), (1017, 588)]
    y = 1_000_000_000
    period = 4095
    ans = 0
    for rr, val in arr:
        ans += (int((y-rr)/period) + 1) * val
    print(ans)

        
infile = sys.argv[1]
with open(infile, "r") as f:
    solve()
    exit(0)
    pattern = [list(line) for line in f.read().splitlines()]
    n, m = len(pattern), len(pattern[0])
    assert n == m
    print(f"({n}, {m})")
    

    N = 34
    matrix = [['.'] * N for _ in range(N)]

    (m_i, m_j) = N//2 - n//2, N//2 - n//2

    rounds = []
    i = 1
    while True:
        matrix = play_round(matrix)
        if does_match(matrix, pattern, m_i, m_j):
            # rounds.append(i)
            # print(rounds)
            print(f"({i}, {count_active(matrix)})")

        i += 1


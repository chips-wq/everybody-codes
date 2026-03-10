"""

property: if add one to some column (making it n+1), you will make it = n in the round

2 3 4 5
3 4 5 2
4 5 2 3
5 2 3 4

think of columns as arrays

6 3 4 5
3 4 5 2
4 5 2 3
  ^
5 2 3 4

1. pop from the front.
2. if it's <= n, then it goes at (val-1)
3. if it's <= 2*n, id2 = val-n      n-id2+1     n-val+n+1 = 2n-val+1

should give 3
n = 4
val = 6
2*4-6+1 = 8-6+1 = 2+1 = 3

"""
import sys

def pretty_print(matrix: list[list[int]]):
    # print it's tranpose
    # what's the longest row ?
    M = max(len(line) for line in matrix)
    n = len(matrix)

    for j in range(M):
        for i in range(n):
            # do we have an element at matrix[i][j]
            if j < len(matrix[i]):
                print(f"{matrix[i][j]} ", end="")
            else:
                print(" ", end="")
        print()
    
def play_round(rnd: int, matrix: list[list[int]]):
    assert len(matrix) == 4
    # This is the transpose matrix we are holding here
    m = len(matrix)
    row = matrix[rnd % m]
    nrow = matrix[(rnd+1) % m]

    val = row.pop(0)
    n = len(nrow)
    if val <= n:
        nrow.insert(val-1, val)
    elif val <= 2*n:
        nrow.insert(2*n-val+1, val)
    else:
        assert False

infile = sys.argv[1] if len(sys.argv) > 1 else "part1.example"

with open(infile, "r") as f:
    # given a line, map it to ints
    matrix = [list(map(int, line.split())) for line in f.read().splitlines()]
    matrix = [list(line) for line in list(zip(*matrix))]

    def get_top(matrix: list[list[int]]):
        n = len(matrix)
        assert n == 4
        ans = []
        for i in range(n):
            ans.append(matrix[i][0])
        return int("".join(str(el) for el in ans))

    for rnd in range(10):
        play_round(rnd, matrix)
        number = get_top(matrix)
        print(f"{rnd+1=}, {number=}")

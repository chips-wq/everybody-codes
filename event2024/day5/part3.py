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

Can I bruteforce this
"""
import sys
from collections import defaultdict

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
                print("  ", end="")
        print()
    
def play_round(rnd: int, matrix: list[list[int]]):
    assert len(matrix) == 4
    # This is the transpose matrix we are holding here
    m = len(matrix)
    row = matrix[rnd % m]
    nrow = matrix[(rnd+1) % m]

    val = row.pop(0)
    n = len(nrow)
    # loop until val <= n and then see which "way" you were going
    # say val in (n, 2n]
    # now in (0, n] with cnt = 1
    # reverse the order with n-val+1 -> this n-val is in [0, n) and you need the +1 to know where to insert it
    oval = val
    assert val > 0
    # cnt = (val-1)//n
    # val = (val)%n

    # [0, n] -> cnt = 0
    # (n, 2n] -> cnt = 1

    # we are taking val into [0, n]
    # [0, n] -> cnt = 0
    # (n, 2n] -> cnt = 1
    # (2n, 3n] -> cnt = 2
    # val-1
    #

    # [n+1, 2n] -> 1 (val goes in [1,n] (mod something like n+1) and then add one   (maybe [n, 2n-1])  map to [0, n-1]
    # [2n+1, 3n] -> 2                                                               (maybe [2n, 3n-1]
    cnt = 0
    while val >= n+1:
        val -= n
        cnt += 1
    # now val <= n
    assert cnt == (oval-1) // n
    assert val == (oval - cnt * n)
    # cnt = (oval-1) // n
    # val = (oval - cnt * n)

    if cnt % 2 == 0:
        nrow.insert(val-1, oval)
    else:
        nrow.insert(n-val+1, oval)

    # if val <= n:
    #     nrow.insert(val-1, val)
    # elif val <= 2*n:
    #     nrow.insert(2*n-val+1, val)
    # else:
    #     assert False

infile = sys.argv[1] if len(sys.argv) > 1 else "part3.example"

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

    D = defaultdict(int)
    rnd = 0
    while True:
        play_round(rnd, matrix)
        # pretty_print(matrix)
        # print()
        number = get_top(matrix)
        if (rnd+1) % 1000 == 0:
            print(f"max so far = {max(D.keys())}")
        D[number] += 1
        # if D[number] == 2024:
        #     print(f"number {number} was shouted the 2024th time at the end of round {rnd+1}")
        #     ans = (rnd+1) * number
        #     print(f"{ans=}")
        #     break
        # print(f"{rnd+1=}, {number=}")
        rnd += 1

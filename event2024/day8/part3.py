import sys
"""
This is an ordered sequence

1 3 5 7

partial sum of this sequence
1 4 9 16

find i s.t f[i-1] < x <= f[i]

task is finding first number >= 13 (is this bisect_right) ?

F_n = (F_n-1) + 3 = F_n + 2

width is a function of `i`

`i` = 1, width = 1
`i` = 2, width = 3
`i` = 3, width = 5
`i` = 4, width = 7

what's the height of a certain column ?

it's a sum of thicknesses based on how old the column is

how "old" is the column ?

 ----------
-------------
3 2 1 0 1 2 3
0 1 2 3 4 5 6

thickness = 7
7//2 = 3

abs(i-thickness//2) <- this is how old it is
if this value is 0 -> it's height is a partial sum of all thicknesses
if this value is 1 -> it's height is a partial sum of all thicknesses except for the first one
if this value is 2 -> it's height is a partial sum of all thicknesses except for the first two


"""

MAX_N = 1_000_000
# MOD = 5
# BLOCKS = 160

MOD = 10
BLOCKS = 202_400_000

infile = sys.argv[1]

with open(infile, "r") as f:
    x = int(f.read().strip())

    thickness = [0] * MAX_N
    thickness[0] = 1
    for i in range(1, MAX_N):
        ww = i * 2 - 1
        thickness[i] = (thickness[i-1] * x) % MOD + MOD
        assert thickness[i] > 0

    blocks = [0] * MAX_N
    blocks[0] = 1
    for i in range(1, MAX_N):
        ww = (i+1) * 2 - 1
        # We are computing the number of blocks for layer `i+1`
        empty = 0
        ss = 0
        for k in range(ww):
            old = abs(k-ww//2)
            height = sum(thickness[old:(i+1)])
            ss += height
            c_empty = ww * x * height % MOD
            if k in [0, ww-1]:
                c_empty = 0
            empty += c_empty
        blocks[i] = ss-empty
        if blocks[i-1] < BLOCKS <= blocks[i]:
            print(f"{blocks[i]=}")
            print(f"{blocks[i]-BLOCKS=}")
            print(f"{ww=}")
            print(f"ans={ww * (blocks[i]-BLOCKS)}")


        if i <= 10 or ((i+1) & (i)) == 0:
            print(f"{(i+1)=}, {blocks[i]=}")

    # for i in range(1, MAX_N):
    #     if blocks[i-1] < BLOCKS <= blocks[i]:
    #         ww = (i+1) * 2 - 1
    #         print(f"{blocks[i]=}")
    #         print(f"{blocks[i]-BLOCKS=}")
    #         print(f"{ww=}")
    #         print(f"ans={ww * (blocks[i]-BLOCKS)}")
    #

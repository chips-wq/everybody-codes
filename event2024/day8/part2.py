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

"""

MAX_N = 1_000_000
MOD = 1111
BLOCKS = 20240000

# MOD = 5
# BLOCKS = 50

infile = sys.argv[1]

with open(infile, "r") as f:
    x = int(f.read().strip())

    layers = [0] * MAX_N
    thickness = [0] * MAX_N
    thickness[0] = 1
    layers[0] = 1
    for i in range(1, MAX_N):
        ww = i * 2 - 1
        thickness[i] = (thickness[i-1] * x) % MOD
        layers[i] = (ww + 2) * thickness[i]
    
    pd = [0] * MAX_N
    pd[0] = layers[0]
    for i in range(1, MAX_N):
        pd[i] = pd[i-1] + layers[i]

    for i in range(1, MAX_N):
        if pd[i-1] < BLOCKS <= pd[i]:
            ww = (i+1) * 2 - 1
            print(f"{pd[i]=}")
            print(f"{pd[i]-BLOCKS=}")
            print(f"{ww=}")
            print(f"ans={ww * (pd[i]-BLOCKS)}")


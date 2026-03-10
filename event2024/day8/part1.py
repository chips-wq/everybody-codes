import sys
"""
This is an ordered sequence

1 3 5 7

partial sum of this sequence
1 4 9 16

find i s.t f[i-1] < x <= f[i]

task is finding first number >= 13 (is this bisect_right) ?

F_n = (F_n-1) + 3 = F_n + 2

"""

MAX_N = 1_000_000

infile = sys.argv[1]

with open(infile, "r") as f:
    x = int(f.read().strip())

    dd = [0] * MAX_N
    dd[0] = 1
    for i in range(1, MAX_N):
        dd[i] = dd[i-1] + 2
    
    pd = [0] * MAX_N
    pd[0] = dd[0]
    for i in range(1, MAX_N):
        pd[i] = pd[i-1] + dd[i]
    
    for i in range(1, MAX_N):
        if pd[i-1] < x <= pd[i]:
            print(f"{pd[i]=}")
            print(f"{pd[i]-x=}")
            print(f"{dd[i]=}")
            print(f"ans={dd[i] * (pd[i]-x)}")
    

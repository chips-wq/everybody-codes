import sys

"""
the gears with

x y

if x turns once, then y turns x/y times.
    
128
64
32
16
8

128 turns once, then the one with 64 turns 128/64 = 2 times

x turns `m` times, then y turns `x/y * m` times. 

You can make (m * x) a multiple of `y` so this makes sense.


x1      x2          x3
^
|
      x1/x2        x2/x3


Knowing x2 turns m times, then x3 turns m*x2/x3 times

You know x2 turns x1/x2 times

x1/x2 * x2/x3 = x1/x3

x1/x_n = if x1 turns once, then x_n turns x1/x_n times

2025 * x1/x_n






Part2

NUM_TURNS = 10000000000000

z * x1 / x_n = number of times the last one turns

z * x1 / x_n >= NUM_TURNS


z >= NUM_TURNS * x_n / x1
z is real


Part3


5
5|10 <
10|20
5


(1,  x1)
(x2, y2) <------ this machinery turns x1/x2 times (even the gear y2 turns x1/x2 times) <--- the one before moves once, how many times does this one move
(x3, y3) <------ this machinery turns y2/x3 times (even the gear y3 turns y2/x3 times)
(x4, y4)
(x5, 1)

ans = x1/x2 * y2/x3 * y3/x4 * y4/x5 * 100
"""

NUM_TURNS = 10000000000000

assert len(sys.argv) > 1
infile = sys.argv[1]

with open(infile, "r") as f:
    arr = f.read().strip().splitlines()
    s_p = (1, int(arr[0]))
    e_p = (int(arr[-1]), 1)

    D = [s_p]

    n = len(arr)
    for i in range(1, n-1):
        D.append(tuple(map(int, arr[i].split("|"))))
    D.append(e_p)

    print(D)
    print(n)
    frac = 1
    for i in range(1, n):
        frac *= D[i-1][1] / D[i][0]
    print(frac * 100)


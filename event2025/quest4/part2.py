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

"""

NUM_TURNS = 10000000000000

assert len(sys.argv) > 1
infile = sys.argv[1]

with open(infile, "r") as f:
    arr = list(map(int, f.read().strip().splitlines()))
    z = NUM_TURNS * arr[-1] / arr[0]
    print(z)


    

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "part3.in"

"""
x1, x2, x3, .... x_n

x1 <= x2 <= x3 <= .... <= x_n

you would like to mininmie

S = |y-x1| + |y-x2| + ... |y-x_n|
find y s.t S is minimized

y = the median of the array

"""

with open(infile, "r") as f:
    arr = list(map(int, f.read().splitlines()))
    arr.sort()
    n = len(arr)
    median = arr[n//2]
    ans = sum(abs(el - median) for el in arr)
    print(f"{ans=}")

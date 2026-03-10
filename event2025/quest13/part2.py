import sys

assert len(sys.argv) > 1
infile = sys.argv[1]

def expand(arr: list[tuple[int, int]], reverse=False):
    for i, (s, e) in enumerate(arr):
        replace = range(s, e+1)
        if reverse:
            replace = reversed(replace)
        replace = list(replace)
        arr[i] = replace

with open(infile, "r") as f:
    content = f.read().splitlines()
    arr = []
    for line in content:
        tup = tuple(map(int, line.split("-")))
        arr.append(tup)

    print(arr)
    
    clock = [(1, 1)]
    n = len(arr)
    for i in range(0, n, 2):
        clock.append(arr[i])
    ss = []
    for i in range(1, n, 2):
        ss.append(arr[i])
    ss.reverse()
    print(ss)

    expand(clock)
    expand(ss, reverse=True)
    clock += ss

    clock = [el for line in clock for el in line]
    
    n = len(clock)
    print(clock[20252025%n])

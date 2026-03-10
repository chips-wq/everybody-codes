import sys

assert len(sys.argv) > 1
infile = sys.argv[1]

with open(infile, "r") as f:
    arr = list(map(int, f.read().splitlines()))
    
    clock = [1]
    n = len(arr)
    for i in range(0, n, 2):
        clock.append(arr[i])
    ss = []
    for i in range(1, n, 2):
        ss.append(arr[i])
    ss.reverse()
    clock += ss
    
    print(clock)
    n = len(clock)
    print(n)
    print(clock[(0 + 6) % n])
    print(clock[(0 + 12) % n])
    print(clock[(0 + 2025) % n])

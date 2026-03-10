import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "part1.in"

with open(infile, "r") as f:
    arr = list(map(int, f.read().splitlines()))
    m_arr = min(arr)
    ans = sum(el - m_arr for el in arr)
    print(f"{ans=}")

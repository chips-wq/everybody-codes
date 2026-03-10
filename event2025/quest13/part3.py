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

    clock = [(1, 1)]
    n = len(arr)
    for i in range(0, n, 2):
        clock.append(arr[i])
    ss = []
    for i in range(1, n, 2):
        ss.append(arr[i])
    ss.reverse()

    # expand(clock)
    # expand(ss, reverse=True)
    cutoff = len(clock)
    clock += ss

    # n = sum(abs(s-e+1) for (s, e) in clock) <-- numbers that are on the clock
    # You need a mechanism to tell: who is at position i on the clock
    # There is a mapping from `i` -> `j` in the array of [(s1, e1), (s2, e2) ... (s3, e3)]

    # [l1, l1+l2, l1+l2+l3, .... l1+l2+...l_k]

    sizes = []
    for (s, e) in clock:
        prev = 0 if not sizes else sizes[-1]
        sizes.append(abs(s-e)+1+prev)

    print(f"{len(clock)=}")
    # O(log(501))
    def map_x(x: int):
        for j, (s, e) in enumerate(clock):
            c_len = abs(s-e) + 1
            if x-c_len >= 0:
                x-=c_len
            else:
                return j
        assert False

    n = sum(abs(s-e)+1 for (s, e) in clock)
    print(f"{sizes[-1]=}")
    print(f"{n=}")

    x_r = 202520252025%n
    j_r = map_x(x_r)
    print(f"{x_r=}")
    print(f"{j_r=}")
    print(f"{cutoff=}")

    x_r -= sizes[j_r-1]
    print(f"{x_r=}")
    print(clock[j_r])
    sz = sizes[j_r] - sizes[j_r-1]
    assert x_r < sz

    if j_r >= cutoff:
        assert abs(clock[j_r][1] - clock[j_r][0]) + 1 == sizes[j_r] - sizes[j_r-1]
        r_idx = sz-1-x_r
        print(clock[j_r][0] + r_idx)
    else:
        assert abs(clock[j_r][1] - clock[j_r][0]) + 1 == sizes[j_r] - sizes[j_r-1]
        print(clock[j_r][0] + x_r)
        
        

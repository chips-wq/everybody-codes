import sys


if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    
    with open(infile, "r") as f:
        arr = list(map(int, f.read().strip().split(",")))
        arr = list(set(arr))
        arr.sort()

        print(arr)
        print(arr[:20])
        ss = sum(arr[:20])
        print(f"{ss=}")

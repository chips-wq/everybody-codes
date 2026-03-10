from collections import Counter
import sys


if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    
    with open(infile, "r") as f:
        arr = list(map(int, f.read().strip().split(",")))

        c = Counter(arr)
        counts = c.values()
        print(counts)
        print(max(counts))

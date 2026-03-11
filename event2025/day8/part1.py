import sys

NAILS = 32

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    with open(infile, "r") as f:
        seq = [int(el) - 1 for el in f.read().strip().split(",")]
        n = len(seq)
        ans = 0
        for i in range(n-1):
            e1, e2 = seq[i], seq[i+1]
            if abs(e1-e2) * 2 == NAILS:
                ans += 1
        print(f"{ans=}")
        



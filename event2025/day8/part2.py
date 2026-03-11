import sys

NAILS = 256

def crosses(e1, e2):
    x1, y1 = e1
    x2, y2 = e2
    # Assume x1 < y1
    if x1 > y1: x1, y1 = y1, x1
    assert x1 <= y1
    
    def c1(x2, y2):
        if x1 < x2 < y1 and not (x1 <= y2 <= y1):
            return True
        return False

    return c1(x2, y2) or c1(y2, x2)

def tc1():
    e1 = (1, 5)
    e2 = (2, 5)
    print(f"{e1=}")
    print(f"{e2=}")
    print(f"{crosses(e1, e2)=}")

def tc2():
    e1 = (5, 1)
    e2 = (5, 2)
    print(f"{e1=}")
    print(f"{e2=}")
    print(f"{crosses(e1, e2)=}")

def tc3():
    e1 = (6, 2)
    e2 = (5, 1)
    print(f"{e1=}")
    print(f"{e2=}")
    print(f"{crosses(e1, e2)=}")

def tc4():
    e1 = (2, 6)
    e2 = (1, 5)
    print(f"{e1=}")
    print(f"{e2=}")
    print(f"{crosses(e1, e2)=}")

    
# 1,5,2,6,8,4,1,7,3,5,7,8,2
# (1, 5)
# (5, 2)

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]

    with open(infile, "r") as f:
        seq = [int(el) - 1 for el in f.read().strip().split(",")]
        n = len(seq)
        s = set()
        ans = 0
        for i in range(n-1):
            x2, y2 = seq[i], seq[i+1]
            assert (x2, y2) not in s
            s.add((x2, y2))
            for j in range(i):
                x1, y1 = seq[j], seq[j+1]
                if crosses((x1, y1), (x2, y2)):
                    ans += 1
        print(f"{ans=}")

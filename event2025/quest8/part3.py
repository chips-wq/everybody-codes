import sys

NAILS = 256

def crosses(e1, e2):
    x1, y1 = e1
    x2, y2 = e2
    # Assume x1 < y1
    if x1 > y1: x1, y1 = y1, x1
    assert x1 <= y1
    # Make sure x2 < y2
    if x2 > y2: x2, y2 = y2, x2
    if (x1, y1) == (x2, y2): return True
    
    def c1(x2, y2):
        if x1 < x2 < y1 and not (x1 <= y2 <= y1):
            return True
        return False

    return c1(x2, y2) or c1(y2, x2)

def count_crosses(seq: list[int], edge):
    # 1,5,2,6,8,4,1,7,3,6
    n = len(seq)
    x, y = edge
    ans = 0
    for i in range(n-1):
        x1, y1 = seq[i], seq[i+1]
        if crosses((x1, y1), (x, y)):
            ans += 1
    return ans


def tc1(seq: list[int]):
    edge = (8-1, 5-1)
    print(f"{edge=}")
    print(f"{count_crosses(seq, edge)=}")

def tc2(seq: list[int]):
    edge = (1-1, 6-1)
    print(f"{edge=}")
    print(f"{count_crosses(seq, edge)=}")

def tc3(seq: list[int]):
    edge = (3-1, 7-1)
    print(f"{edge=}")
    print(f"{count_crosses(seq, edge)=}")

    
# 1,5,2,6,8,4,1,7,3,5,7,8,2
# (1, 5)
# (5, 2)

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]

    with open(infile, "r") as f:
        seq = [int(el) - 1 for el in f.read().strip().split(",")]
        n = len(seq)

        print(f"{n=}")
        b_edge = None
        best_crosses = 0
        # Take any two possible x1, y1 with x1 < y1
        for x1 in range(NAILS):
            print(f"{x1=}")
            for y1 in range(x1+1, NAILS):
                # take (x1--y1) and cross it.
                c_count = count_crosses(seq, (x1, y1)) 
                if c_count > best_crosses:
                    best_crosses = c_count
                    b_edge = (x1, y1)

        print(f"{b_edge=}")
        print(f"{best_crosses=}")

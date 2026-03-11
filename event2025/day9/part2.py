import sys

def is_child(child: str, p1: str, p2: str):
    assert len(child) == len(p1)
    assert len(p1) == len(p2)
    for el, z1, z2 in zip(child, p1, p2):
        if el not in [z1, z2]:
            return False
    return True

def cnt(child: str, p1: str):
    assert len(child) == len(p1)
    ans = 0
    for el, z1 in zip(child, p1):
        if el == z1: ans += 1 
    return ans


if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    with open(infile, "r") as f:
        contents = f.read().splitlines()
        dnas = [line.split(":")[1].strip() for line in contents]

        
        n = len(dnas)
        ans = 0
        for i in range(n):
            for j in range(n):
                for k in range(j+1, n):
                    if i == j: continue
                    if j == k: continue
                    if i == k: continue
                    # Assume dnas[i] is child:
                    if is_child(dnas[i], dnas[j], dnas[k]):
                        # print(f"{i=}, {j=}, {k=}")
                        cnt1 = cnt(dnas[i], dnas[j])
                        cnt2 = cnt(dnas[i], dnas[k])
                        ans += cnt1 * cnt2
    print(f"{ans=}")

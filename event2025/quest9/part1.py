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

        for i in range(3):
            child_idx = i
            p1_idx = (i-1) % 3
            p2_idx = (i+1) % 3
            if is_child(dnas[child_idx], dnas[p1_idx], dnas[p2_idx]):
                print(f"{child_idx=}")
                cnt1 = cnt(dnas[child_idx], dnas[p1_idx])
                cnt2 = cnt(dnas[child_idx], dnas[p2_idx])
                print(f"{cnt1=}")
                print(f"{cnt2=}")
                print(f"{cnt1*cnt2=}")


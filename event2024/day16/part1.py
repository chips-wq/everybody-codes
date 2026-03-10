import sys

infile = sys.argv[1]

def rotate_left(arr: list[str], amount: int):
    # s a l u t
    # amount = 3
    # u t s a l

    # reverse(salut) = t u l a s
    # reverse(tu) = u t l a s
    # reverse(las) = u t s a l
    n = len(arr)
    if amount >= n: amount %= n
    
    def reverse(start: int, ll: int):
        l, r = start, start + ll - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    
    reverse(0, n)
    reverse(0, n-amount)
    reverse(n-amount, amount)

with open(infile, "r") as f:
    amounts, content = f.read().split('\n\n')
    amounts = list(map(int, amounts.split(',')))
    n = len(amounts)
    lines = [[] for _ in range(n)]
    content = content.splitlines()

    for ll in content:
        for i in range(n):
            l, r = i*4, i*4+3
            face = ll[l:r].strip()
            if not face: continue
            lines[i].append(face)
    
    for _ in range(100):
        for line, am in zip(lines, amounts):
            rotate_left(line, am)

    for line in lines:
        print(line)

    res = " ".join(lines[i][0] for i in range(n))
    print(res)

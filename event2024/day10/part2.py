
infile = "part2.in"

"""
PTBVRCZHFLJWGMNS
1851
"""

def calc_power(word: str):
    ans = 0
    for i, el in enumerate(word):
        ans += (ord(el) - ord('A') + 1) * (i+1)
    return ans



def parse_inp(inp: list[str]):
    for F in inp:
        F = F.splitlines()
        n = len(F[0].split())
        M = [[] for _ in range(n)]

        for _, ll in enumerate(F):
            ll = ll.split()
            # ll[0], ll[1], ll[2] ... ll[n-1]
            for i, piece in enumerate(ll):
                M[i].append(piece)
        # At this point you have a lot of yielding to do
        for i in range(n):
            yield [list(line) for line in M[i]]

with open(infile, "r") as f:
    assert calc_power("PTBVRCZHFLJWGMNS") == 1851
    inp = f.read().split('\n\n')
    parse_inp(inp)

    res = 0
    for M in parse_inp(inp):
        ans = []
        for i in range(2, 2 + 4):
            for j in range(2, 2 + 4):
                s1 = set(el for el in M[i] if el != '.')
                s2 = set(M[ii][j] for ii in range(8) if M[ii][j] != '.')
                s3 = s1 & s2
                ans.append(list(s3)[0])
        ans = "".join(ans)
        res += calc_power(ans)
    print(f"{res=}")


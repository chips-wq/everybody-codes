import sys

infile = "input.txt" if len(sys.argv) < 2 else sys.argv[1]

def pf_letter(ss : str, letter: str):
    assert len(letter) == 1
    ss = list(ss)
    
    l_letter = letter.lower()
    u_letter = letter.upper()

    n = len(ss)
    ps = [0] * n
    ps[0] = 1 if ss[0] == u_letter else 0
    for i in range(1, n):
        ps[i] = ps[i-1] + (1 if ss[i] == u_letter else 0)
        

    ans = 0
    for i in range(n):
        if ss[i] == l_letter:
            ans += ps[i]
    return ans


with open(infile, "r") as f:
    ss = f.read().strip()
    ra = pf_letter(ss, 'a')
    rb = pf_letter(ss, 'b')
    rc = pf_letter(ss, 'c')

    print(f"{ra=}, {rb=}, {rc=}")
    print(f"{ra+rb+rc=}")



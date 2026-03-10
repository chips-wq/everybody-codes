import sys
from collections import Counter

"""

  01234567890123

0 **XFZB**DCST**
1 **LWQK**GQJH**
2 ?G....WL....DQ
3 BS....H?....CN
4 P?....KJ....TV
5 NM....Z?....SG
6 **NSHM**VKWZ**
7 **PJGV**XFNL**
8 WQ....?L....YS
9 FX....DJ....HV
0 ?Y....WM....?J
1 TJ....YK....LP
2 **XRTK**BMSP**
3 **DWZN**GCJV**
4 WQ....?L....YS
5 FX....DJ....HV
6 ?Y....WM....?J
7 TJ....YK....LP
8 **XRTK**BMSP**
9 **DWZN**GCJV**

2, 8, 14


How do i fill in the dots ?

say you are at some (i, j) which is a `.`

line:

j1 = j//6*6
[i][j1..j1+8]

column:
i1 = i//6*6
[i1..i1+8][j]


for every single dot you see now
1. is it true that either in it's col / row there must be an ? (let's pretend yes)
2. if there is none / there are more, do nothing
3. check if everyone has a pair (in row / col), that the sets are disjoint, and there is a unique one 
in either row / col

"""

assert len(sys.argv) > 1
infile = sys.argv[1]

def method1(i: int, j: int, mat):
    c1 = Counter(mat[i][j1] for j1 in range(j//6*6, j//6*6 + 8) if mat[i][j1] not in ['?', '.'])
    c2 = Counter(mat[i1][j] for i1 in range(i//6*6, i//6*6 + 8) if mat[i1][j] not in ['?', '.'])
    # assert sum(c1.values()) == len(c1)
    # print(c2)
    # assert sum(c2.values()) == len(c2)
    cc = c1 + c2
    ff = [key for key, value in cc.items() if value > 1]
    if len(ff) != 1: return None
    ckey = ff[0]
    return ckey

def method2(i: int, j: int, mat):
    # c1 = Counter(mat[i][j1] for j1 in range(j//6*6, j//6*6 + 8) if mat[i][j1] not in ['?', '.'] and j1 % 6 not in [2,3,4,5])
    # c2 = Counter(mat[i1][j] for i1 in range(i//6*6, i//6*6 + 8) if mat[i1][j] not in ['?', '.'] and i1 % 6 not in [2,3,4,5])
    # print(c2)
    # cc = c1 + c2
    S1 = set(mat[i][j1] for j1 in range(j//6*6, j//6*6 + 8) if mat[i][j1] not in ['?', '.'] and j1 % 6 not in [2,3,4,5])
    S2 = set(mat[i1][j] for i1 in range(i//6*6, i//6*6 + 8) if mat[i1][j] not in ['?', '.'] and i1 % 6 not in [2,3,4,5])

    kk = list(S1 & S2)
    if len(kk) != 1: return None
    return kk[0]

def method3(i: int, j: int, mat):
    assert mat[i][j] == '.'

    c1 = Counter(mat[i][j1] for j1 in range(j//6*6, j//6*6 + 8) if mat[i][j1])
    c2 = Counter(mat[i1][j] for i1 in range(i//6*6, i//6*6 + 8) if mat[i1][j])
    cc = c1 + c2
    if cc['?'] != 1 or cc['.'] != 2: return None
    p1, p2 = c1, c2
    if '?' in p2: p1, p2 = p2, p1
    assert '?' in p1
    assert '.' in p1
    del p1['?']
    del p1['.']
    pp1 = list(set(p1.values()))
    if len(pp1) != 1 or pp1[0] != 2: return None
    del p1
    del pp1
    del p2['.']
    assert '?' not in p2
    pp2 = sorted(set(p2.values()))
    if len(pp2) != 2 or pp2[0] != 1 or pp2[1] != 2: return None
    ret = [k for k, v in p2.items() if v == 1][0]
    
    # What is the index of that `?`
    c1 = [(i, j1) for j1 in range(j//6*6, j//6*6 + 8) if mat[i][j1] == '?']
    c2 = [(i1, j) for i1 in range(i//6*6, i//6*6 + 8) if mat[i1][j] == '?']
    c = c1 + c2
    assert len(c) == 1
    iq, jq = c[0]
    
    return (ret, (iq, jq))

def p_print(mat: list[str]):
    for line in mat:
        print("".join(line))
    print()

with open(infile, "r") as f:
    mat = f.read().splitlines()
    mat = [list(line) for line in mat]
    n, m = len(mat), len(mat[0])
    """
    for i, line in enumerate(mat):
        for j, el in enumerate(line):
            if el == '.':
                # only one of them used to have a peer
                ckey = method2(i, j, mat)
                if ckey == None: continue
                mat[i][j] = ckey
    """

    def pp_2(i: int, j: int):
        for i1 in range(i, i+8):
            for j1 in range(j, j+8):
                print(mat[i1][j1], end='')
            print()
        print()

    p_print(mat)
    ok = False
    while not ok:
        ok = True
        ans1, ans2 = 0,0
        for i, line in enumerate(mat):
            for j, el in enumerate(line):
                if el != '.': continue
                # I guess try method2, if it fails, then resort to trying the second one
                ckey = method2(i, j, mat)
                if ckey != None:
                    mat[i][j] = ckey
                    ok = False
                elif '?' in c:
                    ret = method3(i, j, mat)
                    if not ret: continue
                    c_deduced, (iq, jq) = ret
                    mat[i][j] = c_deduced
                    mat[iq][jq] = c_deduced
                    ok = False
    # Now compute the answer
    res = 0
    for i, line in enumerate(mat):
        for j, el in enumerate(line):
            if (i % 6, j % 6) == (2, 2):
                C = Counter(mat[i1][j1] for i1 in range(i, i+4) for j1 in range(j, j+4))
                if '?' in C or '.' in C: continue
                k = 1
                ans = 0
                for i1 in range(i, i+4):
                    for j1 in range(j, j+4):
                        ans += (ord(mat[i1][j1]) - ord('A') + 1) * k
                        k += 1
                res += ans
    print(f'{res=}')

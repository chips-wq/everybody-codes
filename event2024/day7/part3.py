"""

5 actions of  + 
3 actions of  - 
and the remaining 3 as  = 

5 times 0
3 times 1
3 times 2

11! / (5! * 3! * 3!) <- definitely brute-forceable


what did 3! represent ? (how many ways to arrange these numbers)

0, 1, 2
0, 2, 1
1, 0, 2
2, 0, 1
2, 0, 1
2, 1, 2

"""

def fact(n: int):
    assert n >= 0
    if n == 0: return 1
    return n * fact(n-1)

options = fact(11) / (fact(5) * fact(3) * fact(3))
print(f"{options=}")

import sys

assert len(sys.argv) > 2

trackfile = sys.argv[1]
infile = sys.argv[2]

def parse_track():
    with open(trackfile, "r") as f:
        lines = f.read().splitlines()
        n, m = len(lines), max(len(line) for line in lines)
        
        i, j = 0, 1
        pi, pj = 0, 0
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        # move in all dirs, except the parent
        # make sure that you only have one element
        # take that element, and move there
        
        output = []
        output.append(lines[i][j])
        while output[-1] != 'S':
            cel = None
            ni, nj = -1, -1
            # print(f"{i=}, {j=}")
            for di, dj in dirs:
                r, c = i + di, j + dj
                if (r, c) == (pi, pj): continue
                # print(f"{r=}, {c=}")
                # print("hi")
                # print(f"{n=}, {m=}, {len(lines[r])=}")
                if r < 0 or r >= n or c < 0 or c >= len(lines[r]): continue
                # print("hi1")
                if lines[r][c] == ' ': continue
                # print("hi2")
                assert cel == None
                cel = lines[r][c]
                ni, nj = r, c
            assert (ni, nj) != (-1, -1)
            output.append(cel)
            pi, pj = i, j
            i, j = ni, nj
        return "".join(output)

PLAN_SIZE = 11

def bkt(i, solution: list[str]):
    if i == PLAN_SIZE:
        yield list(solution)
        return

    for el in ['+', '-', '=']:
        solution[i] = el
        app = 1
        for k in range(i):
            if solution[k] == el: app += 1
        if el == '+' and app > 5: continue
        if el in ['-', '='] and app > 3: continue
        yield from bkt(i+1, solution)

def winning_plan(candidate: list[str], adversary: list[str], track: list[str]):
    n = len(track)
    participants = [candidate, adversary]
    for ff in participants:
        assert len(ff) == PLAN_SIZE

    scores = [0, 0]
    # a loop is p0, p1, p2, ... p_{n-1}
    for k, participant in enumerate(participants):
        D = {}
        ans2 = 0
        power2 = 10
        for kk in range(2024):
            # loop number kk * n
            # it is defined by kk*n%PLAN_SIZE
            tdx = 0
            cd2x = 0
            if (kk * n)%PLAN_SIZE in D:
                tdx = D[kk*n%PLAN_SIZE]
            else:
                for ii in range(n):
                    idx = kk * n + ii
                    # (idx % n == 0)
                    # idx % PLAN_SIZE (the entire loop is determined by this)

                    # execute instruction, add power go to the next one
                    if (idx%n) == n-1: assert track[(idx%n)] == 'S'
                    if track[idx%n] == '+':
                        cd2x += 1
                    elif track[idx%n] == '-':
                        cd2x -= 1
                    else:
                        if participant[idx%PLAN_SIZE] == '+':
                            cd2x += 1
                        elif participant[idx%PLAN_SIZE] == '-':
                            cd2x -= 1
                    # tdx += cd2x
                    tdx += cd2x
                D[kk*n%PLAN_SIZE] = tdx
            # what's the last power ?
            ans2 += power2 * n + tdx
            power2 += cd2x
            # print(f"{ans2=}, {ans=}")
            # ans += 10*n + tdx
        scores[k] = ans2

    # scores[0] > scores[1]
    # assert scores[0] != scores[1]
    return scores[0] > scores[1]

with open(infile, "r") as f:
    track = parse_track()
    n = len(track)

    itt = bkt(0, [''] * PLAN_SIZE)
    plans = [el for el in itt]

    print(f"{len(plans)=}")

    _, adversary = f.read().strip().split(":")
    adversary = adversary.split(",")

    print(f"{adversary=}")

    ans = 0
    for i, candidate in enumerate(plans):
        print(f"{i=}")
        if winning_plan(candidate, adversary, track):
            ans += 1
    print(f"{ans=}")

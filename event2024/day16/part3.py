from math import gcd, lcm
from collections import Counter
from functools import reduce, cache
import sys

"""
Q: When do we hit a cycle ?

lcm = lowest common multiple ?

2, 3

it's clear that if I do a 6 on both, I get to the exact same thing -> false

gcd(a, b)


say you run for k rounds

DENOTE: len(lines[0]) = n0
the first one gets rotated
amounts[0] + amounts[0] + ... + amounts[0] = amounts[0] * k (MOD n0)

the second one gets rotated
amounts[1] * k (MOD n1)

the third one gets rotated
amounts[2] * k (MOD n2)

for which k are these equal ?

amounts[0] * k (MOD n0)
amounts[1] * k (MOD n1)
amounts[2] * k (MOD n2)

I think this is chinese remainder theorem

(r1, r2, r3)

dp(rounds, r1, r2, r3)
    # at first (r1, r2, r3) = (0, 0, 0)
    # apply one of the rotations, understand how much you won

    # apply the move and have a function that tells you how much you won
    # for each possible move
    AM = fun(r1, r2, r3)
    AM + dp(rounds-1, r1+x1, r2+x2, r3+x3)

"""

infile = sys.argv[1]

def F(T, lines):
    lines = [list(line) for line in lines]
    # rotate lines[0] by T[0]
    # rotate lines[1] by T[1]
    def reverse(start: int, ll: int, line: list[int]):
        l, r = start, start + ll - 1
        while l < r:
            line[l], line[r] = line[r], line[l]
            l += 1
            r -= 1
    
    for line, am in zip(lines, T):
        n = len(line)
        assert 0 <= am < n

        reverse(0, n, line)
        reverse(0, n-am, line)
        reverse(n-am, am, line)

    # In this current particular state, how many coins do we win ?
    # Do I need to add line[0][1] ?
    S = "".join(line[0][0] + line[0][2] for line in lines)
    C = Counter(S)
    won = sum(max(0, V-2) for V in C.values())
    return won

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

    assert len(lines) == n
    @cache
    def dp_max(rounds, T):
        if rounds == 0: return 0
        ans = float('-inf')
        for dx in [-1, 0, 1]:
            T2 = tuple((cr+cam+dx)%len(lines[i]) for i, (cr, cam) in enumerate(zip(T, amounts)))
            won = F(T2, lines)
            ans = max(ans, won + dp_max(rounds-1, T2))
        return ans

    @cache
    def dp_min(rounds, T):
        if rounds == 0: return 0
        ans = float('inf')
        for dx in [-1, 0, 1]:
            T2 = tuple((cr+cam+dx)%len(lines[i]) for i, (cr, cam) in enumerate(zip(T, amounts)))
            won = F(T2, lines)
            ans = min(ans, won + dp_min(rounds-1, T2))
        return ans

    res_max = dp_max(256, (0,)*n)
    res_min = dp_min(256, (0,)*n)
    print(f"{res_max} {res_min}")

from math import gcd, lcm
from collections import Counter
from functools import reduce
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


amounts[0] + 1 --> 
amounts[1] + 1 --> 
amounts[2] + 1 -->

(amounts[0] - 1) MOD n0
(amounts[1] - 1) MOD n1
(amounts[2] - 1) MOD n2

(amounts[0]) MOD n0
(amounts[1]) MOD n1
(amounts[2]) MOD n2

(amounts[0] + 1) MOD n0
(amounts[1] + 1) MOD n1
(amounts[2] + 1) MOD n2

(r1, r2, r3)

# r1 < n0
# r2 < n1
# r3 < n3
dp(rounds, r1, r2, r3)
    # at first (r1, r2, r3) = (0, 0, 0)
    # apply one of the rotations, understand how much you won

    # apply the move and have a function that tells you how much you won
    # for each possible move
    AM = fun(r1, r2, r3)
    AM + dp(rounds-1, r1+x1, r2+x2, r3+x3)

"""

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

def byte_coins_won_in_range(lines, amounts, l: int, r: int):
    n = len(amounts)
    total = 0
    for rround in range(l, r):
        for line, am in zip(lines, amounts):
            rotate_left(line, am)
        S = "".join(lines[i][0][0] + lines[i][0][2] for i in range(n))
        C = Counter(S)
        won = sum(max(0, V-2) for V in C.values())
        total += won
        # print(f"{rround=}, {total=}")
    return total

TARGET = 202420242024


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

    nn = [len(line) for line in lines]
    LCM = lcm(*nn)
    print(f"{LCM=}")
    lines2 = [list(line) for line in lines]
    
    # Ok how many coins do we win in one cycle ?
    one_cycle = byte_coins_won_in_range(lines, amounts, 0, LCM)
    # how many cycles are there
    num_cycles = TARGET // LCM
    remainder = TARGET % LCM
    print(f"{one_cycle=}")

    final_push = byte_coins_won_in_range(lines, amounts, 0, remainder)
    print(f"{final_push=}")
    
    # real_ans = byte_coins_won_in_range(lines2, amounts, 0, TARGET)
    # print(f"{real_ans=}")
    print(f"{one_cycle*num_cycles+final_push=}")

    res = " ".join(lines[i][0] for i in range(n))
    print(res)

import sys
from bisect import bisect_left

infile = "part3.txt" if len(sys.argv) < 2 else sys.argv[1]

"""
(   )  (
1000   ^
      1000

every single novice in the middle (so that's 998 segments) has mentors on the right and on the left

(pattern) pattern (pattern)
          ^
        count for this one

for a novice at  index `i` ('a'), i'm interested in the number of A's in the range [i-1000, i+1000]

take some index in that big string `i`

"""

def compute_novice_mentors(s: str, letter: str, repeat: int, limit: int):
    s = s * repeat
    assert len(letter) == 1

    l_letter = letter.lower()
    u_letter = letter.upper()

    n = len(s)
    ps = [0] * n
    ps[0] = 1 if s[0] == u_letter else 0
    for i in range(1, n):
        ps[i] = ps[i-1] + (1 if s[i] == u_letter else 0)

    ans = 0

    for i, el in enumerate(s):
        if el != l_letter: continue
        # Go in the range [i-limit, i+limit]
        l_ptr = max(0, i-limit)
        r_ptr = min(n-1, i+limit)
        
        l_val = 0 if l_ptr == 0 else ps[l_ptr-1]
        r_val = ps[r_ptr]
        
        vv = r_val - l_val
        ans += vv

    return ans

def inter(s: str, letter: str, start: int, end: int):
    assert len(letter) == 1

    l_letter = letter.lower()
    u_letter = letter.upper()

    n = len(s)
    ps = [0] * n
    ps[0] = 1 if s[0] == u_letter else 0
    for i in range(1, n):
        ps[i] = ps[i-1] + (1 if s[i] == u_letter else 0)

    ans = 0
    for i in range(start, end):
        el = s[i]
        if el != l_letter: continue
        # Go in the range [i-limit, i+limit]
        l_ptr = max(0, i-limit)
        r_ptr = min(n-1, i+limit)
        
        l_val = 0 if l_ptr == 0 else ps[l_ptr-1]
        r_val = ps[r_ptr]
        
        vv = r_val - l_val
        ans += vv

    return ans

"""
cl * repeat

but we now have

cl*f1 * (what) = cl*repeat

(what) = cl*repeat / cl*f1 = repeat/f1
# increase f1 s.t repeat % f1 == 0


repeat, f1

f1 to be a divisor of repeat

7 3 -> add two to it which 3 - 7 % 3 = 3-1 = 2
9 7 -> 7 - 9 % 7 = 7-2 = 5

"""

def get_divs(n: int):
    ans = []
    for i in range(1, n+1):
        if (n % i == 0):
            ans.append(i)
    return ans

def compute_novice_mentors2(s: str, letter: str, repeat: int, limit: int):
    t = s
    f1 = 1
    while (n := len(s)) < limit:
        s = s + t
        f1 += 1
    
    divs = get_divs(repeat)
    f_big = divs[bisect_left(divs, f1)]

    diff = f_big - f1
    s = s + t*diff
    f1 += diff

    # assert s * r2 == t * repeat
    repeat = repeat//f1

    n = len(s)
    assert (n >= limit)

    # First only interested in the first `n`
    # Then only interested in the last `n`
    two_s = s * 2
    assert len(letter) == 1

    first_ans = inter(two_s, letter, 0, 2 * n)
    three_s = s * 3
    second_ans = (inter(three_s, letter, n, 2*n)) * (repeat - 2)
    return first_ans + second_ans

repeat = 1000
limit = 1000

with open(infile, "r") as f:
    s = f.read().strip()

    ra = compute_novice_mentors(s, 'a', repeat, limit)
    rb = compute_novice_mentors(s, 'b', repeat, limit)
    rc = compute_novice_mentors(s, 'c', repeat, limit)
    ra2 = compute_novice_mentors2(s, 'a', repeat, limit)
    rb2 = compute_novice_mentors2(s, 'b', repeat, limit)
    rc2 = compute_novice_mentors2(s, 'c', repeat, limit)

    v1 = ra + rb + rc
    v2 = ra2 + rb2 + rc2
    # assert (v1 == v2)
    print(f"{v1=}")
    print(f"{v2=}")

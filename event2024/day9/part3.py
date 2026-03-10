import sys

"""
The problem goes around talking about some sort of system like, given some `target`, find x, y s.t

S = {f(x) + f(y) | x + y = target, |x-y| <= 100}

and f(x) + f(y) is minimum, where f(z) means the smallest number of coins to get to some amount
you can compute f(z) for pretty much all numbers and then look "around it" for candidates

Bad example:
    let's say i just run the program now, so I get the output something like
    x = target-1
    y = 12

    suppose f(x) + f(y) is the minimum, yet it doesn't satisfy |x-y| <= 100


suppose x >= y and that x is known

N = 2 * 10^5

try all possible x'es
1. do a for loop over all x
2. compute the equivalent y
3. test the condition
4. see if f(x) + f(y) is minimized

"""

coins = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

infile = sys.argv[1]

with open(infile, "r") as f:
    targets = list(map(int, f.read().splitlines()))
    N = max(targets)
    print(f"{N=}")
    print(f"{len(targets)=}")
    
    dp = [float('inf')] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for coin in coins:
            dp[i] = min(dp[i], dp[i-coin] + 1)
    # print(dp)

    ans = 0
    for target in targets:
        cans = float('inf')
        bx, by = -1, -1
        # x + y = target
        # x > 0, y > 0, x < target, y < target
        for x in range(1, target):
            y = target - x
            assert 0 < y < target
            if abs(x-y) > 100: continue
            if dp[x] + dp[y] < cans:
                cans = dp[x] + dp[y]
                bx, by = x, y
        print(f"{target=}, {bx=}, {by=}, {dp[bx]=}, {dp[by]=}")
        ans += dp[bx] + dp[by]
    print(f"{ans=}")


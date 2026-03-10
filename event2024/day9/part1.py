import sys

coins = [1,3,5,10]

infile = sys.argv[1]

"""
dp[i] = minimum number of coins to get to `i`


S = {dp[i-coin] | coin is a beetle that you can use}
dp[i] = min(S) + 1

--> 17 (in y+1) coins

1, 3, 5, 10

--> 12 (say in y coins)
"""

with open(infile, "r") as f:
    targets = list(map(int, f.read().splitlines()))
    N = max(targets)
    
    dp = [float('inf')] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for coin in coins:
            dp[i] = min(dp[i], dp[i-coin] + 1)
    print(dp)
        

    ans = sum(dp[target] for target in targets)
    print(f"{ans=}")


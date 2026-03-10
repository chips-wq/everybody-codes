import sys

coins = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

infile = sys.argv[1]

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


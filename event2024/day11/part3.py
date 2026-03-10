from collections import defaultdict, deque
from functools import cache
import sys

infile = sys.argv[1]

"""
maybe try memoizing this in some sort of function
"""

with open(infile, "r") as f:
    lines = f.read().splitlines()
    graph = defaultdict(list)

    S = set()
    for line in lines:
        src, ll = line.split(":")
        neighs = ll.split(",")
        S.add(src)
        S.update(neighs)
        assert src not in graph
        graph[src] = neighs
    
    @cache
    def dp(node: str, rounds: int):
        assert rounds >= 0
        if rounds == 0: return 1
        ans = 0
        for neigh in graph[node]:
            ans += dp(neigh, rounds-1)
        return ans

    res = 0 
    for el in S:
        print(f"{el=}, {dp(el, 20)=}")

    Y = [dp(el, 20) for el in S]
    print(f"{max(Y)=}")
    print(f"{min(Y)=}")
    ans = max(Y) - min(Y)
    print(f"{ans=}")

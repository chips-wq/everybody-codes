from collections import defaultdict, deque
import sys

infile = sys.argv[1]

with open(infile, "r") as f:
    lines = f.read().splitlines()
    graph = defaultdict(list)

    for line in lines:
        src, ll = line.split(":")
        neighs = ll.split(",")
        assert src not in graph
        graph[src] = neighs
    
    q = deque(['A'])
    i = 0
    while q and i < 4:
        rng = len(q)
        for _ in range(rng):
            C = q.popleft()
            for neigh in graph[C]:
                q.append(neigh)
        i += 1
    print(q)
    print(f"{len(q)=}")


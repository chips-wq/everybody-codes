import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else "part1.in"

ROOT_NODE = 'RR'

with open(infile, "r") as f:
    lines = f.read().splitlines()
    parents = {}
    parents[ROOT_NODE] = ROOT_NODE

    k = 0
    for line in lines:
        node, children = line.split(':')
        children = children.split(',')

        for child in children:
            assert child != ROOT_NODE
            if child == '@':
                child = child + str(k)
                k += 1
            parents[child] = node
    
    results = []
    for i in range(k):
        nd = f"@{i}"
        path = ["@"]
        ans = 1
        while parents[nd] != ROOT_NODE:
            path.append(parents[nd])
            ans += 1
            nd = parents[nd]
        path.append(ROOT_NODE)

        path.reverse()
        print((ans, path))
        results.append((ans, path))
    
    D = defaultdict(list)
    # D maps length -> all paths
    for ll, path in results:
        D[ll].append(path)

    for ll, paths in D.items():
        assert len(paths) > 0
        if len(paths) > 1: continue
        print(f"{ll=}, {paths[0]=}")

        answer = "".join(node[0] for node in paths[0])
        print(f"{answer=}")

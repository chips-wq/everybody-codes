

import sys

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

        res = "".join(reversed(path))
        print((ans, res))
        results.append((ans, res))
    
    answer = min(results)
    print(f"{answer=}")

    
    

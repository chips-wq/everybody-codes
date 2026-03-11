import sys
from collections import deque

infile = "part1.in" if len(sys.argv) < 2 else sys.argv[1]

# make sure this is an acyclic graph -> run dfs cycle detection


"""
- tree edges (those the dfs goes from a -> b)
- back edges (going back to something you are visiting now)
- cross edges (name is intuitive, they point to something black)
- forward edges

detect the back edges

"""

def dfs(node: int, color: list[bool], G):
    color[node] = 1
    ans = False
    for (neigh, _) in G[node]:
        if color[neigh] == 2: continue
        if color[neigh] == 1:
            return True
        ans = (ans | dfs(neigh, color, G))
    color[node] = 2
    return ans

def run_tc(tc, free_plants, in_edges: list[int], G):
    tc = list(map(int, tc.split()))
    in_edges = list(in_edges)
    for p_idx in free_plants:
        assert V[p_idx] == 1
        in_edges[p_idx] += 1
    B = [0] * n
    B[0] = 1

    trick_edges = [(p_idx, typ) for p_idx, typ in zip(free_plants, tc)]
    G[0] = trick_edges

    # Run Kahn's algorithm on this graph
    Q = deque([0])
    while Q:
        node = Q.popleft()
        
        for (neigh, cost) in G[node]:
            in_edges[neigh] -= 1
            cB = 0 if B[node] < V[node] else B[node]
            B[neigh] += cB * cost

            if in_edges[neigh] == 0:
                Q.append(neigh)

    return B[-1] if B[-1] >= V[-1] else 0


with open(infile, "r") as f:
    plants = f.read().split('\n\n')
    test_cases = plants[-1]
    plants = plants[:-1]
    n = len(plants) + 1
    V = [0] * n
    V[0] = 1

    G = [[] for _ in range(n)]
    in_edges = [0] * n

    # G[x] is a tuple of (y, cost)
    free_plants = []
    
    for i, plant in enumerate(plants):
        plant = plant.split('\n')
        plant_idx = int(plant[0].split()[1])
        assert plant_idx == i + 1
        thickness = int(plant[0].split()[-1].replace(":", ""))
        V[plant_idx] = thickness

        print(plant)
        if "free" in plant[1]:
            assert len(plant) == 2
            assert plant[1].split()[-1] == '1'
            free_plants.append(plant_idx)
        else:
            for branch in plant[1:]:
                if not branch: continue
                branch = branch.split()
                print(branch)
                from_idx, cost = int(branch[4]), int(branch[-1])
                assert branch[3] == 'Plant'
                G[from_idx].append((plant_idx, cost))
                in_edges[plant_idx] += 1

    color = [0] * n
    assert dfs(0, color, G) == False

    ans = 0
    test_cases = test_cases.strip().splitlines()
    for tc in test_cases:
        res = run_tc(tc, free_plants, in_edges, G)
        print(res)
        ans += res
    print(f"{ans=}")

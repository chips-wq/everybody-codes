from collections import deque
import sys

def is_child(child: str, p1: str, p2: str):
    assert len(child) == len(p1)
    assert len(p1) == len(p2)
    for el, z1, z2 in zip(child, p1, p2):
        if el not in [z1, z2]:
            return False
    return True

def cnt(child: str, p1: str):
    assert len(child) == len(p1)
    ans = 0
    for el, z1 in zip(child, p1):
        if el == z1: ans += 1 
    return ans


def bfs(start: int, graph: list[list[int]], vis: set[int]):
    q = deque([start])
    vis.add(start)

    ans = 0
    scale_sum = 0
    while q:
        c = q.popleft()
        ans += 1
        scale_sum += (c+1)
        
        for neigh in graph[c]:
            if neigh in vis: continue
            vis.add(neigh)
            q.append(neigh)

    return (ans, scale_sum)
    
if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    with open(infile, "r") as f:

        contents = f.read().splitlines()
        dnas = [line.split(":")[1].strip() for line in contents]

        n = len(dnas)
        graph = [[] for _ in range(n)]

        for i in range(n):
            print(f"{i=}")
            for j in range(n):
                for k in range(j+1, n):
                    if i == j: continue
                    if j == k: continue
                    if i == k: continue
                    # Assume dnas[i] is child:
                    if is_child(dnas[i], dnas[j], dnas[k]):
                        # there is an edge [dnas[i], dnas[j]]
                        # there is an edge [dnas[i], dnas[k]]
                        graph[i].append(j)
                        graph[j].append(i)

                        graph[i].append(k)
                        graph[k].append(i)

                        # print(f"{i=}, {j=}, {k=}")
                        # cnt1 = cnt(dnas[i], dnas[j])
                        # cnt2 = cnt(dnas[i], dnas[k])

        print(f"Graph parsed!")
        vis = set()

        ans = -1
        b_scale_sum = -1
        # Now do bfs on c.c
        for i in range(n):
            if not graph[i]: continue
            if i in vis: continue
            c_ans, scale_sum = bfs(i, graph, vis)
            if c_ans > ans:
                b_scale_sum = scale_sum
                ans = c_ans
        print(f"{ans=}")
        print(f"{b_scale_sum=}")

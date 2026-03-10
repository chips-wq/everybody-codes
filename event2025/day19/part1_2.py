"""
Keep in a bfs Q:

(i, j, wing_flaps, wall_idx)

wall_idx represents the wall i'm currently trying to get into:

(add all possible ways into the Q:)
1. if i'm in the opening of the wall, move wall_idx forwards
2. if i'm in the wall itself, don't continue down this path

walls:

(x_idx, y_idx, gap)

i have (x, y)

if x == x_idx:
    # either i'm inside it or in the gap
    if y_idx <= y < y_idx+gap:
        # you can continue going forward, just move wall_idx forward aswell
    else:
        # you lost

Idea 2:
    Go through every single possible destination in the gap and add that to the bfs
    (esentially "teleporting there")
"""
import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else "part1.in"

# we should probably be doing dijkstra
# we are interested in the fastest possible way to getting to a new location and we know the cost of getting there
def bfs(walls):
    q = deque([(0, 0, 0, 0)])

    while q:
        x, y, wf, w_idx = q.popleft()

        x_idx, y_idx, gap = walls[w_idx]

        dist = x_idx - x
        # Go through every possible position we can reach in this gap
        for ny in range(y_idx, y_idx+gap):
            # Can you reach (x_idx, ny) ?
            if y-dist <= ny <= y+dist and (ny-(y-dist)) % 2 == 0:
                # you can actually reach in (ny-y+dist) // 2 wing flaps
                if w_idx+1 < len(walls):
                    q.append((x_idx, ny, wf+((ny-y+dist)//2), w_idx+1))
                else:
                    print(f"reaching ({x_idx}, {ny}) in {wf+((ny-y+dist)//2)}")

with open(infile, "r") as f:
    walls = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]
    # walls = walls[:3]
    # print(walls)
    bfs(walls)



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

def bfs(walls):
    q = deque([(0, 0, 0, 0)])

    while q:
        x, y, wf, w_idx = q.popleft()

        x_idx, y_idx, gap = walls[w_idx]

        # dist = x_idx - x
        # Go through every possible position we can reach in this gap
        # for ny in range(y_idx, y_idx+gap):
            # Can you reach (x_idx, ny) ?
            # if y-dist <= ny <= y+dist:

                # q.append((
        if x == x_idx:
            if y_idx <= y < y_idx+gap:
                w_idx += 1
                print(f"at wall {w_idx}")
                if w_idx == len(walls):
                    print(f"got to wall_idx = {w_idx} with wing flaps = {wf}")
                    continue

            else:
                continue


        # is it stil possible to get to the next one ?
        # i can get to anything in a particular range (by keep on jumping, by not jumping at all)
        # distnace to next
        dist = x_idx - x
        rng = (y-dist, y + dist)
        # I have to make sure that this closed range intersects the next gap
        
        # [y_idx, y_idx+gap-1]
        # [y-dist, y+dist]
        def no_intersection(x1, y1, x2, y2):
            # fix (x1, y1) in your head
            if y2 < x1: return True
            if x2 > y1: return True
            return False
        if no_intersection(y-dist,y+dist,y_idx,y_idx+gap-1): continue
        
        # (x+1, y+1, wf+1, w_idx)
        # (max(x-1, 0), y+1, wf, w_idx)
        
        q.append((x+1, y+1,         wf+1, w_idx))
        q.append((x+1, max(y-1, 0), wf,   w_idx))


with open(infile, "r") as f:
    walls = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]
    # walls = walls[:3]
    # print(walls)
    bfs(walls)



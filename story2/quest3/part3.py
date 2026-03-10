import sys
from collections import deque
from itertools import tee

infile = "example.in" if len(sys.argv) == 1 else sys.argv[1]

# Just do a big bfs

def parse_line(line : str):
    cid = int(line.split(":")[0])
    rest = line.split(":")[1].strip()
    faces_str, seed_str = rest.split()
    faces_str = faces_str.split("=")[1]
    faces_str = faces_str[1:]
    faces_str = faces_str[:-1]

    seed_str = seed_str.split("=")[1].strip()

    faces = [int(el) for el in faces_str.split(",")]
    seed = int(seed_str)
    return cid, faces, seed

def roll_die(faces : list[int], seed: int):
  pulse = seed
  roll_number = 1

  n = len(faces)
  c_pos = 0
  while True:
    spin = roll_number * pulse
    c_pos = (c_pos + spin) % n

    pulse = (pulse + spin) % seed
    pulse = pulse + 1 + roll_number + seed
    roll_number += 1
    yield faces[c_pos]

def get_locations(grid : list[list[int]], target : int):
  ans = []
  for i, row in enumerate(grid):
    for j, el in enumerate(row):
      if el == target: ans.append((i, j))
  return ans

def pretty_print(grid : list[list[int]], visited : set[tuple[int, int]]):
  for i, row in enumerate(grid):
    for j, el in enumerate(row):
      if (i, j) in visited:
        print("x", end="")
      else:
        print(el, end="")
    print()
  print()

def copy_generators(generator, num_copies : int):
  ans = [generator]
  for _ in range(num_copies-1):
    lg = ans.pop()
    t1, t2 = tee(lg)
    ans.append(t1)
    ans.append(t2)

  return ans

with open(infile, "r") as f:
  lines, grid = f.read().split("\n\n")
  lines = lines.splitlines()
  grid = grid.strip().splitlines()
  grid = [[int(el) for el in row] for row in grid]

  dies = []
  for line in lines:
    cid, faces, seed = parse_line(line)

    print(f"{cid=}")
    print(f"{faces=}")
    print(f"{seed=}")
    dies.append((cid, seed, faces))
  
  # Roll all of them once and then initialize your Q

  # Create generators for all of them and roll them all together
  generators = [[roll_die(faces, seed), faces, seed, cid] for cid, seed, faces in dies]

  q = deque([])
  for g, faces, seed, cid in generators:
    res = next(g)
    # find all of their locations and put that up as a starting point
    for (i, j) in get_locations(grid, res):
      n_g = roll_die(faces, seed)
      next(n_g)
      q.append((i, j, cid, 0, n_g))

  # Now we have all of the possible starting locations and we can roll the dies (using the generators)
  # Do a really nice multi-source bfs until we visited everything, this is self-ending and you don't need the visited set
  dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
  n, m = len(grid), len(grid[0])
  visited = set()

  seen = set()
  # In order to prune, I could probably use a hash over (i, j, cid) ->
  # (id of the iterator, know that if I have been here before with a particular iterator, then I know how it will end)
  # i.e my pieces of interest are already in visited
  while q:
    i, j, cid, point, g = q.popleft()
    if (i, j, cid, point) in seen: continue

    seen.add((i, j, cid, point))
    visited.add((i, j))
    
    pos_next = next(g)

    new_positions = []
    for di, dj in dirs:
      r, c = i + di, j + dj
      if r < 0 or r >= n or c < 0 or c >= m: continue
      if grid[r][c] != pos_next: continue
      # actually these are all supposed to be different generators
      new_positions.append((r, c))

    if new_positions:
      new_generators = copy_generators(g, len(new_positions))
      assert len(new_generators) == len(new_positions)
      for p, (r, c) in enumerate(new_positions):
        q.append((r, c, cid, point + 1, new_generators[p]))

  pretty_print(grid, visited)
  print(len(visited))
    
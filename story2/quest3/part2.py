import sys

infile = "example.in" if len(sys.argv) == 1 else sys.argv[1]

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

with open(infile, "r") as f:
  lines, track = f.read().split("\n\n")
  lines = lines.splitlines()
  track = track.strip()

  print(f"{lines=}")
  print(f"{track=}")

  dies = []
  for line in lines:
    cid, faces, seed = parse_line(line)

    print(f"{cid=}")
    print(f"{faces=}")
    print(f"{seed=}")
    dies.append((cid, seed, faces))
  
  # Create generators for all of them and roll them all together
  generators = [[cid, roll_die(faces, seed), 0] for cid, seed, faces in dies]

  finished = [False] * (len(dies) + 1)
  finished[0] = True

  ans = []
  while not all(finished):
    # Go through all generators and roll them once
    for j, (cid, g, idx) in enumerate(generators):
      if finished[cid]: continue
      want = int(track[idx])
      have = next(g)
      if want == have:
        generators[j][2] += 1
        if idx + 1 == len(track):
          ans.append(cid)
          finished[cid] = True
  print(",".join(str(el) for el in ans))

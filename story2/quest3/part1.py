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
  lines = f.read().splitlines()
  dies = []
  for line in lines:
    cid, faces, seed = parse_line(line)

    print(f"{cid=}")
    print(f"{faces=}")
    print(f"{seed=}")
    dies.append((cid, seed, faces))
  
  first_die = dies[0]
  cid, seed, faces = first_die

  # Create generators for all of them and roll them all together
  generators = [roll_die(faces, seed) for cid, seed, faces in dies]

  points = 0
  i = 1
  while points < 10_000:
    # Go through all generators and roll them once
    for g in generators:
      points += next(g)
    print(f"{i=}, {points=}")
    i += 1

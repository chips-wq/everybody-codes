import sys

infile = "example22.in" if len(sys.argv) < 2 else sys.argv[1]

"""
256 * 100000

it starts out even

Maybe there is some sort of cycle

RGG

012345
RGGRGG

6 // 2

01 23 45
RG RG RG

5
01234
GRGRG

4 <- at the exact same point as before
RGRG


if after our length has decreased by 256, 

how many steps to decrease our length by 256

it also depends on the `j`
j % 3

How long to decrease by (256, 0) 
                              ^
                              j
(256, 0)

n -> n-1 -> n-1-2 >- 

256 * 100
256 * 99
256 * 98 <- n is even, you expect to perform the same right

256 * 4
256 * 3
256 * 2
256 * 1 <- n is odd

a state depends on 

they are the same % 256
256 
"""


def part1(line : str):
  i = 0
  j = 0
  n = len(line)
  ballons = ['R', 'G', 'B']
  # Start going through each ballon and popping
  while True:
    ballon = ballons[j % 3]
    # Go through as many as you can
    while i < n and line[i] == ballon:
      i += 1

    i += 1
    if i >= n:
      return j + 1

    j += 1

def part2(ll : str):
  # When we arrange them, can the second one hit something
  """
  4
  0 1 2 3

  4 // 2

  6
  0 1 2 3 4 5
  6 // 2
  """
  ballons = ['R', 'G', 'B']
  # If it's not even, just remove the first one
  line = [el for el in ll]
  n = len(line)
  j = 0

  removed = 0
  p = 0
  sj = 0

  
  while n > 0:
    ballon = ballons[j%3]
    
    if n % 2 == 0 and line[0] == ballon:
      assert n % 2 == 0
      idx = n // 2
      line = line[:idx] + line[(idx+1):]
      removed += 1

    line = line[1:]
    removed += 1
     
    # for el in line:
    #   print(el, end=" ")
    # print()
    n = len(line)

    j += 1
  return j

def part3(ll : str):
  # When we arrange them, can the second one hit something
  """
  4
  0 1 2 3

  4 // 2

  6
  0 1 2 3 4 5
  6 // 2
  """
  ballons = ['R', 'G', 'B']
  # If it's not even, just remove the first one
  line = [el for el in ll]
  n = len(line)
  j = 0
  sj = 0
  p = 0
  removed = 0

  lj = 0
  k = 0
  while n > 0:
    ballon = ballons[j%3]

    if n % 2 == 0 and line[0] == ballon:
      assert n % 2 == 0
      idx = n // 2
      removed += 1
      line = line[:idx] + line[(idx+1):]

    line = line[1:]
    removed += 1

    n = len(line)

    k += 1

    if n % 256 == 0:
      print(f"{n=}, {p%2=}, {sj=} -> {k=}")

      p += 1
      removed = 0
      sj = (j + 1) % 3
      lj = (j)
      k = 0

    j += 1

  return j


with open(infile, "r") as f:
  line = f.read().strip()

  n = len(line)
  print(f"{n=}")

  res = part3(line * 100)
  print(res)

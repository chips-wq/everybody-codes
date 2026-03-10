import sys

"""
Part II.

For any (x,y) look at the equation

Under the group MOD x + y + 1

y - u == 0

u == y

but you look first under mod 1, then under mod2, then under mod3

under mod1, u == y

there is precisely one unique y, for each, call them y1, y2, y3 ... y_k

u1 = y1 MOD 1
u2 = y2 MOD 2

...
u_k = yk MOD k

find such a `y_k`

example:

y = 0, MOD 3
y = 8  MOD 11
y = 4  MOD 5
y = 9  MOD 13
y = 3  MOD 7

find a number s.t 
u % 3 = 0
u % 11 = 8
u % 5 = 4
u % 13 = 9
u % 7 = 3

smallest number that respects this
option1. just guess them

Part III.
There is probably a math theorem allowing you do this without brute forcing it.

First idea lcm:

is all `y`'s were 0, then we could take lcm(m1, m2, m3 ... m_k)

So we need a math trick similar to this lcm.

u = 11 * k + 8 (teorema impartiirii cu rest, exista k si r)
u-8 e divizibil prin 11

"""

def jump(x : int, y : int, amount : int) -> tuple[int, int]:
  sz_diag = x + y + 1
  return ((x + amount) % sz_diag , (y - amount) % sz_diag)

def coprime(x : int, y : int):
  # They share no commond divisor
  for i in range(2, min(x, y)):
    if (x % i == 0 and y % i == 0): return False
  return True


"""
if n and and m are coprime 
then n^(m-1) = 1

therefore n * (n ^ (m-2)) = 1
therefore n ^ (m-2) is the inverse

"""
def fast_expo(n : int, m : int):
  if m == 0: return 1
  if (m % 2): return (n * fast_expo(n, m-1))
  half = fast_expo(n, m//2)
  return (half * half)

def test_fast_expo():
  print(f"fast_expo(3, 0) = {fast_expo(3, 0)}")
  print(f"fast_expo(3, 1) = {fast_expo(3, 1)}")
  print(f"fast_expo(3, 2) = {fast_expo(3, 2)}")
  n = 3
  m = 5
  inv = fast_expo(n, m-2) % m
  print(f"inv = {inv}")
  print(f"{n} * {inv} = {n * inv % m}")


if __name__ == "__main__":
  test_fast_expo()
  infile = "example_notes.txt" if len(sys.argv) < 2 else sys.argv[1]
  sz = 0
  points = []

  mods = []
  remainders = []
  for line in open(infile):
    a, b = line.split(" ")
    x_val = int(a.split("=")[1]) - 1
    y_val = int(b.split("=")[1]) - 1
    points.append((x_val, y_val))

    sz = max(sz, x_val + y_val + 1)

    mods.append(x_val + y_val + 1)
    remainders.append(y_val)

  # Check that all moduli are coprime
  everything_coprime = all([coprime(mod1, mod2) for mod1 in mods for mod2 in mods if mod1 != mod2])
  print(f"Everything coprime: {everything_coprime}")

  
  with open("part3_data.txt", "w") as f:
    for (mod, remainder) in zip(mods, remainders):
      f.write(f"u % {mod} = {remainder}\n")

  ans = 0
  prod_all = 1
  for mod in mods: prod_all *= mod

  for (mod, remainder) in zip(mods, remainders):
    M_i = prod_all // mod
    N_i = pow(M_i, -1, mod)
    # N_i = fast_expo(M_i, mod-2) % mod

    ans += remainder * M_i * N_i

  print(f"M = {prod_all}")
  print(f"ans = {ans % prod_all}")

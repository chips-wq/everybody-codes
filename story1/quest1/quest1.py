import sys

def eni(n : int, exp : int, mod : int):
  remainders = []

  score = 1
  for _ in range(exp):
    score = (score * n) % mod
    remainders.append(score)

  remainders.reverse()
  fin_str = "".join(str(el) for el in remainders)

  return int(fin_str)

# O(log(n))
def fast_pow(n : int, exp : int, mod : int):
  if exp == 0:
    return 1

  if (exp % 2):
    return n * (fast_pow(n, exp-1, mod)) % mod
  half = fast_pow(n, exp/2, mod) % mod
  return (half * half) % mod

def big_eni(n : int, exp : int, mod : int) -> int:
  remainders = []
  for i in range(exp, max(0, exp-5), -1):
    remainders.append(fast_pow(n, i, mod))
  
  return int("".join(str(el) for el in remainders))

if __name__ == '__main__':

  ans = 0
  while (line := sys.stdin.readline().strip()):
    arr = line.split(" ")
    a = int(arr[0][2:])
    b = int(arr[1][2:])
    c = int(arr[2][2:])

    x = int(arr[3][2:])
    y = int(arr[4][2:])
    z = int(arr[5][2:])

    mod = int(arr[6][2:])

    
    print(f"big_eni({a}, {x}, {mod}) + big_eni({b}, {y}, {mod}) + big_eni({c}, {z}, {mod}) = {big_eni(a, x, mod)} + {big_eni(b, y, mod)} + {big_eni(c, z, mod)} = {big_eni(a,x,mod) + big_eni(b,y,mod) + big_eni(c,z,mod)}")

    ans = max(ans, big_eni(a,x,mod) + big_eni(b,y,mod) + big_eni(c,z,mod))

  print(ans)

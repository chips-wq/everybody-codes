from itertools import tee

def gen():
  i = 1
  while True:
    yield i
    i += 1
  
def copy_generators(generator, num_copies : int):
  ans = [generator]
  for _ in range(num_copies-1):
    lg = ans.pop()
    t1, t2 = tee(lg)
    ans.append(t1)
    ans.append(t2)

  return ans

a = gen()
print(next(a))
print(next(a))
print(next(a))

a, b, c = copy_generators(a, 3)
print(f"{a=}, {b=}, {c=}")
print(f"{next(a)=}, {next(b)=}, {next(c)=}")

a, b, c, d = copy_generators(a, 4)
print(f"{a=}, {b=}, {c=}, {d=}")
print(f"{next(a)=}, {next(b)=}, {next(c)=}, {next(d)=}")

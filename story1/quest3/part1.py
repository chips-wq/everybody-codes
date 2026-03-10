import sys

"""
x = 1
* * * * * *
* * * * *
* * * *
* * *
* *
*


y <= (sz) + 1 - x


for a given (x,y) there exists the diagonal (x + z, y - z)

take it such that z = -x +1 so you can get to (1,        y + x - 1) <- that's how big the first row can get
take it such that z = y-1 so you can get to   (x + y -1, 1)         <- that's how big the first column can get

(x + y - 1) -> size of the matrix

for a single snail at (x1, y1) -> (x1 + z, y1 - z) and then maybe take some mod so you see where you end up

examples:

y <= (sz) - x + 1

x + y <= sz + 1


sz = 8

(3, 4) -> (13, 14) -> 

sz-1 == 5   x
0 1 2 3 4 5
1 2 3 4 5
2 3 4 5
3 4 5 
4 5
5

modul cu size-ul diagonalei asteia
(2, 1) -> (3, 0) -> (4, -1)

(0, 3)

(4, 5)


(5, 0) -> (6, -1) 

Look at
(6 - 6, -1 + 6) = (0, 5)

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

"""

def jump(x : int, y : int, amount : int) -> tuple[int, int]:
  sz_diag = x + y + 1
  return ((x + amount) % sz_diag , (y - amount) % sz_diag)

if __name__ == "__main__":
  infile = "example_notes.txt" if len(sys.argv) < 2 else sys.argv[1]
  sz = 0
  points = []
  for line in open(infile):
    a, b = line.split(" ")
    x_val = int(a.split("=")[1]) - 1
    y_val = int(b.split("=")[1]) - 1
    points.append((x_val, y_val))

    sz = max(sz, x_val + y_val + 1)

  ans = 0
  for (x,y) in points:
    new_x, new_y = jump(x, y, 100)
    print(f"[x={new_x + 1}, y={new_y + 1}]")
    ans += (new_x + 1) + 100 * (new_y + 1)

  print(f"ans = {ans}")
    

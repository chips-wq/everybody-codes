import sys

"""
0, 2, 4, 6, 8 .. <- input slots

0123456789
*.*.*.*.*.*.*.*.*
.*.*.*.*.*.*.*.*.
*.*.*...*.*...*..
.*.*.*.*.*...*.*.
*.*.....*...*.*.*
.*.*.*.*.*.*.*.*.
*...*...*.*.*.*.*
.*.*.*.*.*.*.*.*.
*.*.*...*.*.*.*.*
.*...*...*.*.*.*.
*.*.*.*.*.*.*.*.* <- n-1
.*.*.*.*.*.*.*.*. <- n

0 2 4 6
1 2 3 4

// 2 + 1

Observation, the number of paths is = 6, therefore you can backtrack by appointing each one of them

Problem reformulation:

there exists a permutation of the numbe [0..5] s.t you reach the minimum and s.t you reach the maximum

that's bad it actually makes no sense

you have 6 paths

p1 p2 p3 p4 p5 p6

there are 20 slots you can place these into

brute-forcing would mean

A_20^6 ~ 38.000, which is feasible

A_19^6 = 19! / (19-6)! ~ 19'000'000 (feasible but we will sit here for a long time)

bkt(i, ans):
  if i == 6:
    # try it with ans
    simulate_with_ans()


  # you need to pick from [0, 2, 4, 6 .. 38]
  for j in range(0, m, 2):
    if `j` in ans: continue
    ans.append(j)
    bkt(i + 1, ans)
    ans.pop()

try dropping the first token from any of [0, 2, 4, 6 ... 38]

|
[am1, am2, ... am38]

second token drop from everywhere
[am1, am2, .... am38]

select i1, i2 with i1 != i2 s.t arr1[i1] + arr[i2] is minimal


more general i1, i2 ... i6 all different s.t arr[i1] + arr[i2] + ... + arr[i6] is minimal

take lowest one from all arrays
second lowerst from all arrays

3 5 11
3 0 4
|
we can resee minimum here
(0, 1) (3,0) (3,1) (4, 1), (5, 0), (11, 0)

a1 = 
a1 = [(profit1, 0), (profit2, 2), (profit3, 4) ... ]
a2 = [(profit1, 0), (profit2, 2), (profit3, 4) ... ]
a3 = [(profit1, 0), (profit2, 2), (profit3, 4) ... ]
a4 = [(profit1, 0), (profit2, 2), (profit3, 4) ... ]
a5 = [(profit1, 0), (profit2, 2), (profit3, 4) ... ]
a6 = [(profit1, 0), (profit2, 2), (profit3, 4) ... ]

pick maximum from first column, maximum from second column

take the first one (never take from (_, 1)) again
take the second one (never take from (_, 0)) again


"""

def drop_from_all(board: list[str], path: str):
  ans = []
  _, m = len(board), len(board[0])
  for start_point in range(0, m, 2):
    end_point = simulate(start_point, board, path)

    s, e = start_point // 2 + 1, end_point // 2 + 1
    profit = max(0, e * 2 - s)

    ans.append((profit, start_point))
  assert(len(ans) == (m+1) // 2)
  return ans
  
def simulate(idx : int, board : list[str], path : str):
  k = 0

  n, m = len(board), len(board[0])
  i = 0
  while i < n:
    # if we are on a star, go left or right depengind on what you can
    if board[i][idx] == '*':
      d = path[k]
      k += 1
      if idx == 0: d = 'R'
      elif idx == m-1: d = 'L'

      if d == 'R': idx += 1
      elif d == 'L': idx -= 1

    else:
      i += 1
  return idx

def maximum_profit(board : list[str], path : str):
  start_idx = 0
  n, m = len(board), len(board[0])

  ans = 0
  while start_idx < m:
    end_idx = max(ans, simulate(start_idx, board, path))

    s, e = start_idx // 2 + 1, end_idx // 2 + 1
    
    coins_won = max(0, e * 2 - s)
    ans = max(ans, coins_won)

    start_idx += 2
  return ans

infile = "part3_example.in" if len(sys.argv) < 2 else sys.argv[1]

with open(infile, "r") as f:
  board, tokens = f.read().split("\n\n")
  board = board.strip().splitlines()
  tokens = tokens.strip().splitlines()

  matrix = []
  for i,path in enumerate(tokens):
    c_ans = drop_from_all(board, path)
    matrix.append(c_ans)

  n1, m1 = len(matrix), len(matrix[0])

  min_ans = 0
  t = []
  for j in range(m1):
    m = matrix[0][j][0]
    for i in range(n1):
      m = min(m, matrix[i][j][0])

    t.append(m)

  t.sort()
  min_ans = sum(t[:6])
  print(t)


  
  print(f"{min_ans=}")


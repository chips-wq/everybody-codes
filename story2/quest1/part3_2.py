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
"""

def simulate_with_ans(ans : list[int], tokens: list[str], board: list[str]):
  assert len(tokens) == len(ans)
  res = 0
  # ans[i], means drop token i from ans[i]
  for i, drop_point in enumerate(ans):
    assert drop_point % 2 == 0
    end_point = simulate(drop_point, board, tokens[i])

    s, e = drop_point // 2 + 1, end_point // 2 + 1
    profit = max(0, e * 2 - s)

    res += profit
  return res

INF = 10 ** 18

min_ans = INF
max_ans = 0

it = 0
def bkt(i : int, ans : list[int], board : list[str], tokens : list[str]):
  if i == 6:
    assert len(ans) == 6
    global min_ans
    global max_ans
    global it
    print(ans)
    it += 1
    print(f"{it=}")
    c_ans = simulate_with_ans(ans, tokens, board)
    min_ans = min(min_ans, c_ans)
    max_ans = max(max_ans, c_ans)
    return

  _, m = len(board), len(board[0])
  for j in range(0, m, 2):
    if j in ans: continue
    ans.append(j)
    bkt(i + 1, ans, board, tokens)
    ans.pop()
  
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

  ans = []
  bkt(0, ans, board, tokens)

  print(f"{min_ans=}")
  print(f"{max_ans=}")

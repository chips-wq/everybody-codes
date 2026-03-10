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

/2 + 1
"""

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

infile = "part2_example.in" if len(sys.argv) < 2 else sys.argv[1]

with open(infile, "r") as f:
  board, tokens = f.read().split("\n\n")
  board = board.strip().splitlines()
  tokens = tokens.strip().splitlines()

  # Brute force it by dropping it in each
  ans = 0
  start_idx = 0
  for path in tokens:
    profit = maximum_profit(board, path)
    print(f"{profit=}")
    ans += profit

  print(ans)



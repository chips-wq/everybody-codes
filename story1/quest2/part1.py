import sys
from typing import Optional
from collections import deque

infile = "part1.txt" if len(sys.argv) < 2 else sys.argv[1]

class Node:
  def __init__(self, rank : int, symbol : str, left = None, right = None):
    self.rank = rank
    self.symbol = symbol
    self.left = left
    self.right = right

def add_node(root : Optional[Node], node : Node):
  if root is None:
    return node

  assert(node.rank != root.rank)
  if node.rank < root.rank:
    root.left = add_node(root.left, node)
  if node.rank > root.rank:
    root.right = add_node(root.right, node)
  return root

def dfs(root : Optional[Node]):
  if root is None:
    return
  # This is in-order traversal
  print(root.rank)
  dfs(root.left)
  dfs(root.right)

def bfs(root : Node) -> str:
  max_sz = 0
  q = deque([root])
  while q:
    # Explore the entire level first
    qsz = len(q)
    current_str = ""
    for _ in range(qsz):
      top = q.popleft()
      current_str += top.symbol
      if (top.left): q.append(top.left)
      if (top.right): q.append(top.right)

    if qsz > max_sz:
      max_sz = qsz
      ans = current_str

  return ans

if __name__ == "__main__":
  left_tree = None
  right_tree = None

  for line in open(infile):
    _, _, l, r = line.strip().split(" ")
    left_rank, left_symbol = l[6:-1].strip().split(",")
    left_rank = int(left_rank)

    right_rank, right_symbol = r[7:-1].strip().split(",")
    right_rank = int(right_rank)

    left_tree = add_node(left_tree, Node(left_rank, left_symbol))
    right_tree = add_node(right_tree, Node(right_rank, right_symbol))

  left_ans = bfs(left_tree)
  right_ans = bfs(right_tree)
  print(f"left_ans = {left_ans}")
  print(f"right_tree = {right_ans}")

  print(left_ans + right_ans)
  
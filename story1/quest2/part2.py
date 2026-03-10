import sys
from typing import Optional
from collections import deque

infile = "part1.txt" if len(sys.argv) < 2 else sys.argv[1]

d1 = {}
d2 = {}

class Node:
  def __init__(self, rank : int, symbol : str, left = None, right = None):
    self.rank = rank
    self.symbol = symbol
    self.left = left
    self.right = right
    self.parent = None

def add_node(root : Optional[Node], node : Node):
  if root is None:
    return node

  assert(node.rank != root.rank)
  if node.rank < root.rank:
    root.left = add_node(root.left, node)
    root.left.parent = root
  if node.rank > root.rank:
    root.right = add_node(root.right, node)
    root.right.parent = node

  return root

def swap_nodes(n1 : Node, n2 : Node):
  n1.rank, n2.rank = n2.rank, n1.rank
  n1.symbol, n2.symbol = n2.symbol, n1.symbol

def swap_trees(n1 : Node, n2 : Node):
  assert(n1.parent != None)
  assert(n2.parent != None)
  # Look at the parent of n1
  # Look at the parent of n2
  is_left_n1 = (n1.parent.left == n1)
  is_left_n2 = (n2.parent.left == n2)

  if is_left_n1:
    if is_left_n2:
      n1.parent.left, n2.parent.left = n2, n1
    else:
      n1.parent.left, n2.parent.right = n2, n1
  else:
    if is_left_n2:
      n1.parent.right, n2.parent.left = n2, n1
    else:
      n1.parent.right, n2.parent.right = n2, n1

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
  left_tree = Node(0, "dummy")
  right_tree = Node(0, "dummy")

  for line in open(infile):
    line = line.strip()
    if line[:3] == "ADD":
      cmd, cid, l, r = line.split(" ")
      cid = int(cid.split("=")[1])

      left_rank, left_symbol = l[6:-1].strip().split(",")
      left_rank = int(left_rank)

      right_rank, right_symbol = r[7:-1].strip().split(",")
      right_rank = int(right_rank)

      assert(left_rank != 0)
      assert(right_rank != 0)

      left_node = Node(left_rank, left_symbol)
      right_node = Node(right_rank, right_symbol)


      print(f"For id = {cid}, we have id(left_node) = {id(left_node)}, id(right_node) = {id(right_node)}")
      d1[cid] = (left_node, right_node)

      left_tree = add_node(left_tree, left_node)
      right_tree = add_node(right_tree, right_node)
    else:
      _, cid =  line.split(" ")
      cid = int(cid)
      
      swap_nodes(d1[cid][0], d1[cid][1])
      

  left_ans = bfs(left_tree)
  right_ans = bfs(right_tree)
  print(f"left_ans = {left_ans}")
  print(f"right_tree = {right_ans}")

  print(left_ans + right_ans)
  
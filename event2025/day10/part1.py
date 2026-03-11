import sys
from collections import deque

def find_dragon(board: list[list[str]]):
    di, dj = -1, -1
    for i, line in enumerate(board):
        for j, el in enumerate(line):
            if el == 'D':
                di, dj = i, j
    return di, dj

def bfs(si: int, sj: int, max_moves: int, board: list[list[str]]):
    n, m = len(board), len(board[0])
    dirs = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
    print(len(dirs))

    visited = set()
    q = deque([(si, sj, 0)])
    visited.add((si, sj))
    
    while q:
        ci, cj, moves = q.popleft()

        assert moves <= max_moves

        for di, dj in dirs:
            r, c = ci + di, cj + dj
            if r < 0 or c < 0 or r >= n or r >= m: continue
            if (r, c) in visited: continue
            if moves + 1 > max_moves: continue
            # Now moves+1 <= max_moves
            visited.add((r, c))
            q.append((r, c, moves+1))
    return visited

MAX_MOVES = 4
if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    with open(infile, "r") as f:
        board = [list(line) for line in f.read().splitlines()]

        ci, cj = find_dragon(board)
        visited = bfs(ci, cj, MAX_MOVES, board)
        
        ans = 0
        for i, line in enumerate(board):
            for j, el in enumerate(line):
                if el == 'S' and (i, j) in visited:
                    ans += 1
        print(f"{ans=}")

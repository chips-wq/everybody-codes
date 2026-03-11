import sys
from collections import deque

def find_dragon(board: list[list[str]]):
    di, dj = -1, -1
    for i, line in enumerate(board):
        for j, el in enumerate(line):
            if el == 'D':
                di, dj = i, j
    return di, dj

def move_dragon(dragon_positions: set[tuple[int, int]], n: int, m: int):
    dirs = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
    new_dragon_positions = set()
    for (i, j) in dragon_positions:
        for di, dj in dirs:
            r, c = i + di, j + dj
            if r < 0 or c < 0 or r >= n or c >= m: continue
            new_dragon_positions.add((r, c))

    return new_dragon_positions

def move_sheep(board: list[list[str]]):
    # Go on colomouns from bottom upwards
    n, m = len(board), len(board[0])
    for j in range(m):
        for i in range(n-1, -1, -1):
            if board[i][j] == 'S':
                board[i][j] = '.'
                if i+1 < n:
                    board[i+1][j] = 'S'

def eat_sheep(dragon_positions: set[tuple[int, int]], board: list[list[str]], hideouts: set[tuple[int, int]]) -> int:
    ans = 0
    for i, line in enumerate(board):
        for j, el in enumerate(line):
            if (i, j) in hideouts: continue
            if el == 'S' and (i, j) in dragon_positions:
                ans += 1
                board[i][j] = '.'
    return ans

def simulate_rounds(si: int, sj: int, rounds: int, board: list[list[str]], hideouts: set[tuple[int, int]]):
    dragon_positions = set([(si, sj)])

    n, m = len(board), len(board[0])
    ans = 0
    for _ in range(rounds):
        round_sheep = 0
        # dragon moves
        dragon_positions = move_dragon(dragon_positions, n, m)
        # eats all possible sheep it can (go through board and turn them off)
        round_sheep += eat_sheep(dragon_positions, board, hideouts)
        # sheeps move
        move_sheep(board)
        # dragon eats all possible sheep it can (go through board and turn them off)
        round_sheep += eat_sheep(dragon_positions, board, hideouts)
        print(f"{round_sheep=}")
        ans += round_sheep
    print(f"{ans=}")


def get_hideouts(board: list[list[str]]):
    hideouts = set()
    for i, line in enumerate(board):
        for j, el in enumerate(line):
            if el == '#':
                board[i][j] = '.'
                hideouts.add((i, j))
    return hideouts

def print_board(board: list[list[str]]):
    print()
    for line in board:
        print(line)
    print()

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    with open(infile, "r") as f:
        board = [list(line) for line in f.read().splitlines()]
        hideouts = get_hideouts(board)

        ci, cj = find_dragon(board)
        board[ci][cj] = '.'


        # print_board(board)
        # move_sheep(board)
        # print_board(board)
        ROUNDS = 20
        simulate_rounds(ci, cj, ROUNDS, board, hideouts)


        # print(f"{hideouts=}")
        
        


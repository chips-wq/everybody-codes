import sys
from collections import deque
from functools import cache

def find_dragon(board: list[list[str]]):
    di, dj = -1, -1
    for i, line in enumerate(board):
        for j, el in enumerate(line):
            if el == 'D':
                di, dj = i, j
    return di, dj

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

# Looks like dp with memoization maybe

def get_sheep_positions(board: list[list[str]]):
    n, m = len(board), len(board[0])
    sheep_positions = [-1] * m
    for j in range(m):
        for i in range(n):
            if board[i][j] == 'S':
                sheep_positions[j] = i
                break
    return tuple(sheep_positions)

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    with open(infile, "r") as f:
        board = [list(line) for line in f.read().splitlines()]
        hideouts = get_hideouts(board)
        print(hideouts)

        dragon_si, dragon_sj = find_dragon(board)
        board[dragon_si][dragon_sj] = '.'


        print_board(board)
        start_sheep = get_sheep_positions(board)
        print(f"{start_sheep=}")
        n, m = len(board), len(board[0])
        dirs = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]

        # n * n * n * ... * n = n ^ m
        @cache
        def dp(ci: int, cj: int, sheep_positions):
            assert len(sheep_positions) == m
            for sj in range(m):
                si = sheep_positions[sj]
                if (si, sj) == (ci, cj):
                    assert (si, sj) in hideouts

            if all(el == -1 for el in sheep_positions):
                return 1

            if any(el == n for el in sheep_positions):
                return 0
            # First simulate the eating part here

            # The sheep move, if they can
            # At most one sheep moves, they don't move into the dragon
            # Generate all possible moves, without budging into the dragon

            def eat(r: int, c: int, n_sheep_position):
                assert len(n_sheep_position) == m
                for sj in range(m):
                    si = n_sheep_position[sj]
                    if (si, sj) == (r, c) and (si, sj) not in hideouts:
                        return n_sheep_position[:sj] + (-1,) + n_sheep_position[(sj+1):]
                return n_sheep_position

            ans = 0

            can = False
            # We move here only if the sheep moves
            # Try moving each possible sheep
            for sj in range(m):
                si = sheep_positions[sj]
                if si == -1: continue
                # You will try moving to [si+1]
                # In case this sheep can escape, then you defintely won't be able to eat them all
                assert 0 <= si < n
                assert 1 <= si+1 <= n
                if (si+1, sj) == (ci, cj) and (si+1, sj) not in hideouts: continue

                can = True
                n_sheep_position = sheep_positions[:sj] + (si+1,) + sheep_positions[(sj+1):]

                # Now try moving the dragon in all possible dirs, and also update n_sheep_position based on that
                ok = False
                for di, dj in dirs:
                    r, c = ci + di, cj + dj
                    if r < 0 or c < 0 or r >= n or c >= m: continue
                    ok = True
                    # is there a sheep here that we can eat (there can be at most one), then update n_sheep_position
                    n_sheep_position2 = eat(r, c, n_sheep_position)
                    ans += dp(r, c, n_sheep_position2)
                assert ok

            if can == False:
                assert ans == 0
                for di, dj in dirs:
                    r, c = ci + di, cj + dj
                    if r < 0 or c < 0 or r >= n or c >= m: continue
                    # is there a sheep here that we can eat (there can be at most one), then update n_sheep_position
                    n_sheep_position3 = eat(r, c, sheep_positions)
                    ans += dp(r, c, n_sheep_position3)

            # print(f"{can=}")
            return ans
        
        res = dp(dragon_si, dragon_sj, start_sheep)
        print(f"{res=}")
        

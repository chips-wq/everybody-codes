from collections import deque
import sys

assert len(sys.argv) > 1

infile = sys.argv[1]

def print_mat(matrix: list[list[int]]):
    for line in matrix: 
        print(line)

# Find the number of barrels you kill if you start from (i_start) and already visited (i_visited)
def bfs(i_start: tuple[int, int], i_visited: set[tuple[int, int]], matrix: list[list[int]]):
    assert i_start not in i_visited

    q = deque([i_start])
    visited = set([i_start])
    n, m = len(matrix), len(matrix[0])

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        ci, cj = q.popleft()

        for di, dj in dirs:
            r, c = ci + di, cj + dj
            if r < 0 or r >= n or c < 0 or c >= m: continue
            if (r, c) in visited: continue
            if (r, c) in i_visited: continue

            if matrix[r][c] > matrix[ci][cj]: continue
            assert matrix[r][c] <= matrix[ci][cj]
            visited.add((r, c))
            q.append((r, c))

    return (len(visited), visited)


def take_best(visited: set[tuple[int, int]], matrix: list[list[int]]):
    b_start, b_visited, b_score = None, None, -1

    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if (i, j) in visited: continue
            (c_score, c_visited) = bfs((i, j), visited, matrix)
            if c_score > b_score:
                b_score = c_score
                b_visited = c_visited
                b_start = (i, j)

    n_visited = visited | b_visited
    return (b_start, n_visited)

with open(infile, "r") as f:
    content = f.read().strip().splitlines()
    matrix = [list(map(int, line)) for line in content]
    n, m = len(matrix), len(matrix[0])
    print(f"{n=}, {m=}")
    # To find max you'll do n * m * n * m = n^2 * m^2
    # To find all maxes you n^2 * m^2 * 3
    f_start, f_visited = take_best(set(), matrix)
    print("Finished first")
    s_start, s_visited = take_best(f_visited, matrix)
    print("Finished second")
    t_start, t_visited = take_best(s_visited, matrix)
    print(len(t_visited))

    print(f_start)
    print(s_start)
    print(t_start)

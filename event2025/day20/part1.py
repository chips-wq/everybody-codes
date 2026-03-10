import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "part1.in"

with open(infile, "r") as f:
    matrix = f.read().splitlines()

    n, m = len(matrix), len(matrix[0])
    
    ans = 0
    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if j-i < 0: continue
            if j+i >= m: continue
            # `j-i` is the index into the triangle
            idx = j-i
            if el != 'T': continue

            # [0, m-i)
            # idx-1, idx+1, (i-1, idx)
            if idx-1 >= 0 and matrix[i][j-1] == 'T':
                ans += 1
            if idx+1 < m-i and matrix[i][j+1] == 'T':
                ans += 1
            
            # there are two types of triangles
            if idx % 2 == 0:
                if i > 0 and matrix[i-1][j] == 'T':
                    # idx2 = j - (i-1)
                    assert (j - (i-1)) >= 0
                    assert (j - (i-1)) < m-(i-1)
                    ans += 1
            else:
                if i+1 < n and matrix[i+1][j] == 'T':
                    # idx2 = j - (i+1)
                    assert (j - (i+1)) >= 0
                    assert (j - (i+1)) < m-(i+1)
                    ans += 1
    #fdsfd
    print(f"{ans//2=}")



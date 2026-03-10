
infile = "part1.in"

with open(infile, "r") as f:
    M = [list(line) for line in f.read().splitlines()]
    for line in M:
        print(line)

    ans = []
    # (2, 2)
    for i in range(2, 2 + 4):
        for j in range(2, 2 + 4):
            s1 = set(el for el in M[i] if el != '.')
            s2 = set(M[ii][j] for ii in range(8) if M[ii][j] != '.')
            s3 = s1 & s2
            ans.append(list(s3)[0])
    print("".join(ans))


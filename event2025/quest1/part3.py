import sys

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    with open(infile, "r") as f:
        names, ops = f.read().split('\n\n')
        names = names.strip().split(",")
        ops = ops.strip().split(",")
        ops = [(op[0], int(op[1:])) for op in ops]
        print(ops)

        i = 0
        n = len(names)
        for d, am in ops:
            am = am if d == 'R' else -am
            ni = am % n
            names[0], names[ni] = names[ni], names[i]
        print(names[0])

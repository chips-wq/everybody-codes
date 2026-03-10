import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "part1.in"

ALPHABET_SIZE = 26

with open(infile, "r") as f:
    data = []
    lines = f.read().splitlines()
    for line in lines:
        letter, instructions = line.split(":")
        instructions = instructions.split(",")
        ans = 0
        power = 10
        for ii in range(10):
            if instructions[ii%len(instructions)] == '+':
                power += 1
            elif instructions[ii%len(instructions)] == '-':
                power -= 1
            power = max(power, 0)
            ans += power
        data.append((ans, letter))
    data.sort()
    data.reverse()
    print(data)
    ans = "".join(letter for _, letter in data)
    print(f"{ans=}")



    

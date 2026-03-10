import sys

assert len(sys.argv) > 2

trackfile = sys.argv[1]
infile = sys.argv[2]

def parse_track():
    with open(trackfile, "r") as f:
        lines = f.read().splitlines()
        track = lines[0]
        out = []
        for line in lines[1:-1]:
            out.append(line[0])
            track += line[-1]
        lines[-1] = "".join(list(reversed(lines[-1])))
        track += lines[-1]

        out.reverse()
        track += "".join(out)
        assert track[0] == 'S'
        return track[1:] + "S"



with open(infile, "r") as f:
    track = parse_track()
    n = len(track)

    print(f"{track=}")

    data = []
    lines = f.read().splitlines()

    for line in lines:
        letter, instructions = line.split(":")
        instructions = instructions.split(",")
        ans = 0
        power = 10
        for ii in range(10*n):
            # execute instruction, add power go to the next one
            if (ii%n) == n-1: assert track[(ii%n)] == 'S'
            if track[ii%n] == '+':
                power += 1
            elif track[ii%n] == '-':
                power -= 1
            else:
                if instructions[ii%len(instructions)] == '+':
                    power += 1
                elif instructions[ii%len(instructions)] == '-':
                    power -= 1
            assert power >= 0
            power = max(power, 0)
            ans += power
        data.append((ans, letter))

    data.sort()
    data.reverse()
    print(data)
    ans = "".join(letter for _, letter in data)
    print(f"{ans=}")



    

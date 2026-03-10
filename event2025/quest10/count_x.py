
with open("count_x.txt", "r") as f:
    content = f.read().splitlines()

    lines_x = sum(1 for line in content for el in line if el == 'X')
    print(lines_x)

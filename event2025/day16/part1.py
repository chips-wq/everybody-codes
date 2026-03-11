import sys

COLUMNS = 90

if __name__ == '__main__':
    infile = sys.argv[1]
    with open(infile, "r") as f:
        nums = [int(el) for el in f.read().split(",")]
        ans = sum(COLUMNS // el for el in nums)
        print(f"{ans=}")

        

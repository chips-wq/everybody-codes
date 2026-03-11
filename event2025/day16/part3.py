import sys

"""
Given X = [1, 2, 3, 5, 9]
X = pattern

And a COLUMNS number, you can get the number of blocks using 

f(COLUMNS) = COLUMNS // X[0] + COLUMNS // X[1] + COLUMNS // X[2] + ... + COLUMNS // X[N] = number of blocks


This function is increasing in columns, so binary search COLUMNS s.t f(COLUMNS) <= TARGET

and columns is maximum


"""

INF = 10**18
TARGET = 202520252025000

def get_pattern(nums: list[int]):
    ans = []
    candidate = 1
    while any(el > 0 for el in nums):
        n_nums = [el-1 if i % candidate == (candidate-1) else el for i, el in enumerate(nums)]
        if all(el >= 0 for el in n_nums):
            nums = n_nums
            ans.append(candidate)
        candidate += 1 
    return ans

if __name__ == '__main__':
    infile = sys.argv[1]
    with open(infile, "r") as f:
        nums = [int(el) for el in f.read().split(",")]

        pattern = get_pattern(nums)
        print(f"{pattern=}")

        def get_blocks(columns: int):
            return sum(columns // el for el in pattern)

        l, r = 1, INF
        ans = -1
        while l <= r:
            mid = (r-l)//2 + l
            if get_blocks(mid) <= TARGET:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        print(f"{ans=}")







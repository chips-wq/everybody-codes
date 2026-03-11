import sys

COLUMNS = 90

if __name__ == '__main__':
    infile = sys.argv[1]
    with open(infile, "r") as f:
        nums = [int(el) for el in f.read().split(",")]

        ans = []
        candidate = 1
        while any(el > 0 for el in nums):
            n_nums = [el-1 if i % candidate == (candidate-1) else el for i, el in enumerate(nums)]
            if all(el >= 0 for el in n_nums):
                nums = n_nums
                ans.append(candidate)
            candidate += 1 
        print(f"{ans=}")
        res = 1
        for el in ans:
            res *= el
        print(f"{res=}")

        

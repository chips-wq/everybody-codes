import sys


if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    
    with open(infile, "r") as f:
        arr = list(map(int, f.read().strip().split(",")))
        arr.sort(reverse=True)
        print(arr)

        unique_arr = []
        
        n = len(arr)
        for i in range(1, n):
            if arr[i] != arr[i-1]:
                unique_arr.append(arr[i-1])

        unique_arr.append(arr[-1])
        print(unique_arr)
        print(f"{sum(unique_arr)=}")

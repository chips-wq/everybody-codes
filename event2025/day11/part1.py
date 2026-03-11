import sys

ROUNDS = 10

def is_increasing(arr: list[int]):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def get_checksum(arr: list[int]):
    ans = 0
    for i, el in enumerate(arr):
        ans += (i+1) * el
    return ans


if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]

    with open(infile, "r") as f:
        arr = list(map(int, f.read().splitlines()))
        n = len(arr)


        rr = 0
        first_part = True
        while rr < ROUNDS:
            # Do either first part or the second part
            if first_part:
                for i in range(n-1):
                    if arr[i] > arr[i+1]:
                        arr[i] -= 1
                        arr[i+1] += 1

                if is_increasing(arr):
                    first_part = False
            else:
                for i in range(n-1):
                    if arr[i] < arr[i+1]:
                        arr[i] += 1
                        arr[i+1] -= 1
            rr += 1

        
        print(f"{get_checksum(arr)=}")
        print(arr)





import random

def is_sorted(nums: list[int]):
    n = len(nums)
    for i in range(1, n):
        if nums[i] < nums[i-1]: return False
    return True

def play_round(nums: list[int]):
    n = len(nums)
    for i in range(n-1):
        if nums[i+1] > nums[i]:
            nums[i] += 1
            nums[i+1] -= 1


# Generate some random number
def play_game():
    cols = random.randint(2, 20)
    nums = [random.randint(1, 7)]
    for i in range(cols-2):
        nums.append(nums[-1] + random.randint(1,7))

    # Get some number > nums[-1] that is divisible by cols
    # s.t sum(nums) + k === 0 (MOD cols)
    # k === -sum(nums) (MOD cols)
    # 
    # But we need k > nums[-1]
    # 
    k = (-sum(nums)) % cols
    while k < nums[-1]:
        k += cols
    nums.append(k)
    assert len(nums) == cols
    assert sum(nums) % cols == 0
    return nums


def tc1():
    # 15 / 5 = 3
    nums = [1,2,3,4,5]
    print(nums)
    play_round(nums)
    print(nums)
    play_round(nums)
    print(nums)
    play_round(nums)
    print(nums)

def test_nums(nums: list[int]):
    rounds2 = sum(nums) // len(nums)
    rounds3 = sum(nums) - sum(nums)//len(nums)
    # 35 / 5 = 7
    print(f"{rounds2=}")
    print(f"{rounds3=}")

    rr = 0
    while True:
        if all(el == nums[0] for el in nums):
            print(f"{rr=}")
            break
        play_round(nums)
        rr += 1

n1 = play_game()
test_nums(n1)


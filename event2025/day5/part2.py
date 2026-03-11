from dataclasses import dataclass
from typing import Optional
import sys

@dataclass
class Part:
    spine: int
    left: Optional[int]
    right: Optional[int]

    def add_num(self, num: int):
        if num < self.spine and self.left is None:
            self.left = num
            return True
        if num > self.spine and self.right is None:
            self.right = num
            return True
        return False
            

def get_fishbone_value(nums: list[int]):
    fishbone = []
    for el in nums:
        ok = False
        for part in fishbone:
            if part.add_num(el):
                ok = True
                break
        if not ok:
            fishbone.append(Part(el, None, None))

    ans = "".join(str(part.spine) for part in fishbone)
    return int(ans)

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]

    with open(infile, "r") as f:
        content = f.read().strip().splitlines()
        min_sword_id, min_value = -1, float('inf')
        max_sword_id, max_value = -1, float('-inf')

        for line in content:
            sword_id, nums = line.split(":")
            nums = list(map(int, nums.split(",")))
            
            fishbone_value = get_fishbone_value(nums)
            print(f"{sword_id=}, {fishbone_value=}")

            if fishbone_value < min_value:
                min_value = fishbone_value
                min_sword_id = sword_id

            if fishbone_value > max_value:
                max_value = fishbone_value
                max_sword_id = sword_id

        print(f"{min_sword_id=}, {min_value=}")
        print(f"{max_sword_id=}, {max_value=}")
        
        print(f"{max_value-min_value=}")



from dataclasses import dataclass
from typing import Optional
import sys

# < means that it's better

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
    
    def get_num(self):
        aa = [self.left, self.spine, self.right]
        aa = [el for el in aa if el is not None]
        return int("".join(str(el) for el in aa))

@dataclass
class Sword:
    sword_id: int
    fishbone: list[Part]

    def __lt__(self, other):
        f1, f2 = get_fishbone_value(self.fishbone), get_fishbone_value(other.fishbone)
        if f1 != f2:
            return f1 > f2            # higher quality = better

        for p1, p2 in zip(self.fishbone, other.fishbone):
            n1, n2 = p1.get_num(), p2.get_num()
            if n1 != n2:
                return n1 > n2        # higher level score = better

        return self.sword_id > other.sword_id  # higher id = better

    def __repr__(self):
        return f"Sword({self.sword_id})"

def get_fishbone_value(fishbone):
    ans = "".join(str(part.spine) for part in fishbone)
    return int(ans)

def get_fishbone(nums: list[int]):
    fishbone = []
    for el in nums:
        ok = False
        for part in fishbone:
            if part.add_num(el):
                ok = True
                break
        if not ok:
            fishbone.append(Part(el, None, None))
    return fishbone

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]

    with open(infile, "r") as f:
        content = f.read().strip().splitlines()
        min_sword_id, min_value = -1, float('inf')
        max_sword_id, max_value = -1, float('-inf')

        swords = []
        for line in content:
            sword_id, nums = line.split(":")
            nums = list(map(int, nums.split(",")))
            sword_id = int(sword_id)

            fishbone = get_fishbone(nums)
            sword = Sword(sword_id, fishbone)
            swords.append(sword)
            
        swords.sort()
        ans = [(i+1) * sword.sword_id for i, sword in enumerate(swords)]
        print(f"{sum(ans)=}")
        # print(swords)

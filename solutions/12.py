from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product, repeat
from pathlib import Path


def dprint(fn):
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        print(f"{fn.__name__}({args}, {kwargs}) = {val}")
        return val
    return wrapper

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "12"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

inp = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

inp = inp.strip().splitlines()

def solve(line):
    arr, nums = line.split(" ")
    nums = list(map(int, nums.split(",")))
    arr = arr.strip()

    # part 2
    nums = nums * 5
    arr = "?".join(repeat(arr, 5))
    print(arr, nums)

    # @dprint
    @cache
    def rec(i, j, cur, needs_space):
        if j >= len(nums) and cur == 0:
            for k in range(i, len(arr)):
                if arr[k] == "#":
                    return 0
            return 1
        if i >= len(arr) or j >= len(nums):
            return 0
        if cur > nums[j]:
            return 0
        
        if needs_space:
            if arr[i] not in [".", "?"]:
                return 0
            else:
                return rec(i+1, j, cur, False)

        ans = 0
        if arr[i] == "#" or arr[i] == "?":
            if cur + 1 == nums[j]:
                ans += rec(i+1, j+1, 0, True)
            else:
                ans += rec(i+1, j, cur + 1, False)
        if arr[i] == "." or arr[i] == "?":
            if cur == 0:
                ans += rec(i+1, j, 0, False)

        return ans
    
    return rec(0, 0, 0, False)


ans = 0
for line in inp:
    ans += solve(line)

print(ans)
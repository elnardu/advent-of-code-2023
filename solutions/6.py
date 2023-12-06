from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path
from numba import njit

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "6"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()
# inp = """Time:      7  15   30
# Distance:  9  40  200"""

# lines = inp.splitlines()
# times = list(map(int, lines[0].split()[1:]))
# dist = list(map(int, lines[1].split()[1:]))

# ans = 1
# for t, d in zip(times, dist):
#     a = 0
#     for h in range(1, t):
#         dt = t - h
#         if dt * h > d:
#             a += 1
#     print(t, d, a)
#     ans *= a
# print(ans)

lines = inp.splitlines()
times = int("".join(lines[0].split()[1:]))
dist = int("".join(lines[1].split()[1:]))

print(times, dist)

@njit
def ans():
    a = 0
    t, d = times, dist
    for h in range(1, t):
        dt = t - h
        if dt * h > d:
            a += 1
    return a
print(ans())

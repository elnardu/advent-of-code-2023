from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "9"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()
# inp = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

# lines = inp.splitlines()
# lines = list(map(str.split, lines))
# lines = [list(map(int, line)) for line in lines]

# def solve_line(line):
#     diff = [line]
#     while True:
#         cur = []
#         for i in range(1, len(diff[-1])):
#             cur.append(diff[-1][i] - diff[-1][i-1])

#         if all(map(lambda x: x == 0, cur)):
#             break
            
#         diff.append(cur)
    
#     ans = 0
#     for d in diff:
#         ans += d[-1]
#     return ans

# ans = 0
# for line in lines:
#     ans += solve_line(line)
# print(ans)


lines = inp.splitlines()
lines = list(map(str.split, lines))
lines = [list(map(int, line)) for line in lines]

def solve_line(line):
    diff = [line]
    while True:
        cur = []
        for i in range(1, len(diff[-1])):
            cur.append(diff[-1][i] - diff[-1][i-1])

        if all(map(lambda x: x == 0, cur)):
            break
            
        diff.append(cur)
    
    ans = 0
    for d in reversed(diff):
        ans = d[0] - ans
    return ans

ans = 0
for line in lines:
    # print(line, solve_line(line))
    ans += solve_line(line)
print(ans)


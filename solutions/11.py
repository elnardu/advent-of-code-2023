from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path
from pprint import pprint

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "11"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# inp = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""

inp = inp.strip().splitlines()
inp = [list(line) for line in inp]

# to_expand_rows = []
# to_expand_cols = []

# for i in range(len(inp)):
#     free = True
#     for j in range(len(inp[0])):
#         if inp[i][j] == "#":
#             free = False
#             break
    
#     if free:
#         to_expand_rows.append(i)

# for j in range(len(inp[0])):
#     free = True
#     for i in range(len(inp)):
#         if inp[i][j] == "#":
#             free = False
#             break
    
#     if free:
#         to_expand_cols.append(j)

# exinp = []
# new_row_len = len(inp[0]) + len(to_expand_cols)
# for i in range(len(inp)):
#     if i in to_expand_rows:
#         exinp.append(["."] * new_row_len)
#         exinp.append(["."] * new_row_len)
#         continue

#     new_row = []
#     for j in range(len(inp[0])):
#         if j in to_expand_cols:
#             new_row.append(".")
#         new_row.append(inp[i][j])
#     exinp.append(new_row)

# locs = []
# for i in range(len(exinp)):
#     for j in range(len(exinp[0])):
#         if exinp[i][j] == "#":
#             locs.append((i, j))

# ans = 0
# for a, b in combinations(locs, 2):
#     ans += abs(a[0] - b[0]) + abs(a[1] - b[1])

# print(ans)

to_expand_rows = []
to_expand_cols = []

for i in range(len(inp)):
    free = True
    for j in range(len(inp[0])):
        if inp[i][j] == "#":
            free = False
            break
    if free:
        to_expand_rows.append(i)

for j in range(len(inp[0])):
    free = True
    for i in range(len(inp)):
        if inp[i][j] == "#":
            free = False
            break
    if free:
        to_expand_cols.append(j)

locs = []
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == "#":
            locs.append((i, j))

# pprint(inp)
# print(to_expand_rows)
# print(to_expand_cols)
exp_ratio = 1000000 - 1
ans = 0
for a, b in combinations(locs, 2):
    max_i = max(a[0], b[0])
    min_i = min(a[0], b[0])
    max_j = max(a[1], b[1])
    min_j = min(a[1], b[1])

    row_exp = 0
    for row in to_expand_rows:
        if min_i <= row < max_i:
            row_exp += 1
    col_exp = 0
    for col in to_expand_cols:
        if min_j <= col < max_j:
            col_exp += 1
    
    ans += abs(a[0] - b[0]) + abs(a[1] - b[1]) + row_exp * exp_ratio + col_exp * exp_ratio
print(ans)




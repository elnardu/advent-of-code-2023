from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from functools import cache, reduce
from itertools import combinations, permutations, product
from pathlib import Path

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "3"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# print(inp)

# inp = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

# l = inp.splitlines()
# ans = 0
# for i in range(len(l)):
#     number = ""
#     valid = False
#     for j in range(len(l[i])):
#         if l[i][j].isdigit():
#             number += l[i][j]

#             if not valid:
#                 for di in [-1, 0, 1]:
#                     for dj in [-1, 0, 1]:
#                         if (
#                             0 <= i + di < len(l)
#                             and 0 <= j + dj < len(l[i])
#                             and (not l[i + di][j + dj].isdigit() and l[i + di][j + dj] != ".")
#                         ):
#                             print(number, l[i + di][j + dj])
#                             valid = True
#                             break

#                     if valid: break

#         else:
#             if valid and len(number) > 0:
#                 ans += int(number)

#             number = ""
#             valid = False

#     if valid and len(number) > 0:
#         ans += int(number)

# print(ans)

gears = defaultdict(list)

l = inp.splitlines()
ans = 0
for i in range(len(l)):
    number = ""
    valid = False
    gear_slot = None
    for j in range(len(l[i])):
        if l[i][j].isdigit():
            number += l[i][j]

            if not valid:
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if (
                            0 <= i + di < len(l)
                            and 0 <= j + dj < len(l[i])
                            and l[i + di][j + dj] == "*"
                        ):
                            gear_slot = (i + di, j + dj)
                            valid = True
                            break

                    if valid: break

        else:
            if valid and len(number) > 0:
                gears[gear_slot].append(int(number))

            number = ""
            valid = False
            gear_slot = None

    if valid and len(number) > 0:
        gears[gear_slot].append(int(number))

ans = 0
print(gears)
for gear_slot in gears:
    if len(gears[gear_slot]) > 1:
        ans += reduce(lambda x, y: x * y, gears[gear_slot])
print(ans)

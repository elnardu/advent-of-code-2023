from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product, repeat, chain
from pathlib import Path
from pprint import pprint
from copy import deepcopy

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "14"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# inp = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#...."""

inp = inp.splitlines()
inp = list(map(list, inp))

# def find_top(i, j):
#     for k in reversed(range(i)):
#         if inp[k][j] != ".":
#             return k + 1
#     return 0

# for i in range(len(inp)):
#     for j in range(len(inp[0])):
#         if inp[i][j] == "O":
#             k = find_top(i, j)
#             inp[k][j] = "O"
#             if i != k:
#                 inp[i][j] = "."

# pprint(inp)

# ans = 0
# for i in range(len(inp)):
#     for j in range(len(inp[0])):
#         if inp[i][j] == "O":
#             ans += len(inp) - i
# print(ans)


def move(i, j, di, dj):
    assert inp[i][j] == "O"
    while True:
        if not (0 <= i + di < len(inp)): break
        if not (0 <= j + dj < len(inp[0])): break
        if inp[i + di][j + dj] == ".":
            inp[i][j] = "."
            i += di
            j += dj
            inp[i][j] = "O"
        else:
            break

def print_map(inp):
    for row in inp:
        print("".join(row))

def to_str(inp):
    return "".join(chain.from_iterable(inp))

def run_round(inp):
    # up
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == "O": move(i, j, -1, 0)

    # left
    for j in range(len(inp[0])):
        for i in range(len(inp)):
            if inp[i][j] == "O": move(i, j, 0, -1)

    # down
    for i in reversed(range(len(inp))):
        for j in range(len(inp[0])):
            if inp[i][j] == "O": move(i, j, 1, 0)

    # right
    for j in reversed(range(len(inp[0]))):
        for i in range(len(inp)):
            if inp[i][j] == "O": move(i, j, 0, 1)

cycles = {}
cycles[to_str(inp)] = 0

cycle_start = None
cycle_period = None

for round in range(1000000000):
    run_round(inp)

    inps = to_str(inp)
    if inps in cycles:
        print("cycle", cycles[inps], round + 1)
        cycle_start = cycles[inps]
        cycle_period = round + 1 - cycle_start
        break
    cycles[inps] = round + 1

print(cycle_start, cycle_period)

round += ((1000000000 - round) // cycle_period) * cycle_period

while round < 1000000000 - 1:
    run_round(inp)
    round += 1

ans = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == "O":
            ans += len(inp) - i
print(ans)
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path
from pprint import pprint

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "13"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

inp1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

inp = inp.strip().splitlines()
pats = []
cur = []
for line in inp:
    if line == "":
        pats.append(cur)
        cur = []
    else:
        cur.append(list(line))
if cur:
    pats.append(cur)

def find_row_reflection(pat):
    for i in range(len(pat)):
        j = 0
        while i + j < len(pat) and i - j - 1 >= 0 and pat[i + j] == pat[i - j - 1]:
            j += 1
        if (i + j == len(pat) or i - j == 0) and j > 0:
            return i
    return None

def find_row_reflection_p2(pat):
    for i in range(len(pat)):
        j = 0
        fixed = False

        def diff_with_smudge(l1, l2):
            nonlocal fixed
            for a, b in zip(l1, l2):
                if a == b: continue
                if not fixed:
                    fixed = True
                    continue
                return False
            return True

        valid = False
        while i + j < len(pat) and i - j - 1 >= 0 and diff_with_smudge(pat[i + j], pat[i - j - 1]):
            valid = True
            j += 1

        if (i + j == len(pat) or i - j == 0) and valid and fixed:
            return i
    return None

def transpose(pat):
    new_pat = [[None] * len(pat) for _ in range(len(pat[0]))]
    for i in range(len(pat)):
        for j in range(len(pat[0])):
            new_pat[j][i] = pat[i][j]
    return new_pat

def print_pat(pat):
    for row in pat:
        print("".join(row))

# ans = 0
# for pat in pats:
#     print_pat(pat)
#     print()
#     print_pat(transpose(pat))
#     print(find_row_reflection(pat))
#     print(find_row_reflection(transpose(pat)))
#     print()
#     row = find_row_reflection(pat)
#     if row is not None: ans += 100 * row
#     col = find_row_reflection(transpose(pat))
#     if col is not None: ans += col

# print(ans)

ans = 0
for pat in pats:
    print_pat(pat)
    print()
    print_pat(transpose(pat))
    print(find_row_reflection_p2(pat))
    print(find_row_reflection_p2(transpose(pat)))
    print()

    row = find_row_reflection_p2(pat)
    if row is not None: ans += 100 * row
    col = find_row_reflection_p2(transpose(pat))
    if col is not None: ans += col
print(ans)
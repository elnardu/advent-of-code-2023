from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path
from pprint import pprint

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "10"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# inp = """7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ"""
# print(inp)
# inp = inp.strip().splitlines()

connections = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}

# s = set()
# q = deque()

# for i in range(len(inp)):
#     for j in range(len(inp[i])):
#         if inp[i][j] == "S":
#             q.append((0, i, j))

# ans = 0

# while q:
#     dist, i, j = q.popleft()
#     print(i, j, inp[i][j])
#     if (i, j) in s:
#         continue
#     s.add((i, j))

#     if inp[i][j] == "S":
#         for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < len(inp) and 0 <= nj < len(inp[ni]):
#                 if inp[ni][nj] not in connections: continue
#                 deltas = connections[inp[ni][nj]]
#                 for di, dj in deltas:
#                     if ni + di == i and nj + dj == j:
#                         q.append((dist+1, ni, nj))
#                         ans = max(ans, dist+1)
#     else:
#         deltas = connections[inp[i][j]]
#         for di, dj in deltas:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < len(inp) and 0 <= nj < len(inp[ni]):
#                 if (ni, nj) not in s:
#                     q.append((dist+1, ni, nj))
#                     ans = max(ans, dist+1)

# print(ans)

# inp = """
# ...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ..........."""

inp = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
inp = inp.strip().splitlines()
inp = [list(line) for line in inp]

m = [[0] * len(inp[0]) for _ in range(len(inp))]

start = None
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "S":
            start = (i, j)
            break
    if start is not None:
        break

def guess_s_dir(i, j):
    valid_dirs = []

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < len(inp) and 0 <= nj < len(inp[ni])): continue
        if inp[ni][nj] not in connections: continue
        deltas = connections[inp[ni][nj]]

        for ndi, ndj in deltas:
            if ni + ndi == i and nj + ndj == j:
                valid_dirs.append((di, dj))
    
    for key in connections:
        deltas = connections[key]
        if set(deltas) == set(valid_dirs):
            return key
    assert False

s_dir = guess_s_dir(*start)
inp[start[0]][start[1]] = s_dir

def pprinti(inp):
    for line in inp:
        print("".join(map(str, line)))
    print()

pprinti(inp)

q = deque()
q.append(start)
while q:
    i, j = q.popleft()
    if m[i][j] != 0:
        continue
    m[i][j] = 1

    deltas = connections[inp[i][j]]
    for di, dj in deltas:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(inp) and 0 <= nj < len(inp[ni]):
            if m[ni][nj] == 0:
                q.append((ni, nj))


from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product, repeat, chain
from pathlib import Path
from pprint import pprint

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "16"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# inp = """.|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|...."""

inp = inp.splitlines()
inp = [list(line) for line in inp]

reflect_mapping = {
    ( 1,  0): ( 0, -1),
    (-1,  0): ( 0,  1),
    ( 0,  1): (-1,  0),
    ( 0, -1): ( 1,  0),
}

reflect_mapping2 = {
    ( 0,  1): ( 1,  0),
    ( 0, -1): (-1,  0),
    ( 1,  0): ( 0,  1),
    (-1,  0): ( 0, -1),
}

def is_in_bounds(s):
    i, j, _, _ = s
    if not (0 <= i < len(inp)): return False
    if not (0 <= j < len(inp[0])): return False
    return True

def solve(i, j, di, dj):
    seeds = deque()
    seeds.append((i, j, di, dj))
    tiles = [[0] * len(inp[0]) for _ in range(len(inp))]
    ray_s = set()

    while seeds:
        ray = seeds.popleft()
        if ray in ray_s: continue
        ray_s.add(ray)
        i, j, di, dj = ray
        tiles[i][j] = 1

        if inp[i][j] == ".":
            nxt = (i + di, j + dj, di, dj)
            if is_in_bounds(nxt): seeds.append(nxt)
        elif inp[i][j] == "|" and di == 0:
            nxt1 = (i + 1, j, 1, 0)
            nxt2 = (i - 1, j, -1, 0)
            if is_in_bounds(nxt1): seeds.append(nxt1)
            if is_in_bounds(nxt2): seeds.append(nxt2)
        elif inp[i][j] == "-" and dj == 0:
            nxt1 = (i, j + 1, 0, 1)
            nxt2 = (i, j - 1, 0, -1)
            if is_in_bounds(nxt1): seeds.append(nxt1)
            if is_in_bounds(nxt2): seeds.append(nxt2)
        elif inp[i][j] == "/":
            ndi, ndj = reflect_mapping[(di, dj)]
            nxt = (i + ndi, j + ndj, ndi, ndj)
            if is_in_bounds(nxt): seeds.append(nxt)
        elif inp[i][j] == "\\":
            ndi, ndj = reflect_mapping2[(di, dj)]
            nxt = (i + ndi, j + ndj, ndi, ndj)
            if is_in_bounds(nxt): seeds.append(nxt)
        elif inp[i][j] in ("|", "-"):
            nxt = (i + di, j + dj, di, dj)
            if is_in_bounds(nxt): seeds.append(nxt)
        else:
            assert False, "invalid input"

    return sum(chain.from_iterable(tiles))

ans = 0
for i in range(len(inp)):
    ans = max(ans, solve(i, 0, 0, 1))
    ans = max(ans, solve(i, len(inp[0]) - 1, 0, -1))

for j in range(len(inp[0])):
    ans = max(ans, solve(0, j, 1, 0))
    ans = max(ans, solve(len(inp) - 1, 0, -1, 0))
    
print(ans)

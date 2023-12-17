from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product, repeat, chain
from pathlib import Path
from pprint import pprint
from heapq import heappop, heappush

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "17"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# inp = """2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533"""

# inp = """111111111111
# 999999999991
# 999999999991
# 999999999991
# 999999999991"""

inp = inp.splitlines()
inp1 = []
for line in inp:
    l = []
    for ch in line:
        l.append(int(ch))
    inp1.append(l)
inp = inp1

def solve():
    dist = {}
    v = set()
    q = []
    l1 = (0, 0, 1, 0, 0)
    l2 = (0, 0, 0, 1, 0)
    heappush(q, (0, l1))
    heappush(q, (0, l2))

    while q:
        d, loc = heappop(q)
        if loc in v: continue
        v.add(loc)
        i, j, di, dj, cons = loc
        if i == len(inp) - 1 and j == len(inp[0]) - 1:
            return d

        for ndi, ndj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + ndi, j + ndj

            if not (0 <= ni < len(inp)): continue
            if not (0 <= nj < len(inp[0])): continue
            if ndi == -di and ndj == -dj: continue

            ncons = 1
            if ndi == di and ndj == dj: ncons = cons + 1
            if ncons > 3: continue

            nd = d + inp[ni][nj]
            nloc = (ni, nj, ndi, ndj, ncons)
            if nloc not in v and (nloc not in dist or dist[nloc] >= nd):
                dist[nloc] = nd
                heappush(q, (nd, nloc))

def solve2():
    dist = {}
    v = set()
    q = []
    l1 = (0, 0, 1, 0, 0)
    l2 = (0, 0, 0, 1, 0)
    heappush(q, (0, l1))
    heappush(q, (0, l2))
    back = {}

    while q:
        d, loc = heappop(q)
        if loc in v: continue
        v.add(loc)
        i, j, di, dj, cons = loc
        if i == len(inp) - 1 and j == len(inp[0]) - 1:
            # pprint(inp)
            # print("back")
            # cur_loc = loc
            # while cur_loc:
            #     print(cur_loc, inp[cur_loc[0]][cur_loc[1]])
            #     cur_loc = back.get(cur_loc)
            return d

        for ndi, ndj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + ndi, j + ndj

            if not (0 <= ni < len(inp)): continue
            if not (0 <= nj < len(inp[0])): continue
            if ndi == -di and ndj == -dj: continue

            is_turn = True
            if ndi == di and ndj == dj: is_turn = False

            if cons < 4 and is_turn: continue
            if cons >= 10 and not is_turn: continue

            ncons = 1
            if not is_turn: ncons = cons + 1

            nd = d + inp[ni][nj]
            nloc = (ni, nj, ndi, ndj, ncons)
            if nloc not in v and (nloc not in dist or dist[nloc] >= nd):
                dist[nloc] = nd
                back[nloc] = loc
                heappush(q, (nd, nloc))

print(solve2())


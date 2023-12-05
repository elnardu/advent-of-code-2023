from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path
from numba import njit, jit

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "5"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# inp = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

# lines = inp.splitlines()

# seeds = lines[0].split(": ")[1].split()
# seeds = list(map(int, seeds))

# i = 2
# while i < len(lines):
#     if "map" not in lines[i]:
#         i += 1
#         continue

#     i += 1
#     mapping = []
#     while i < len(lines) and lines[i]:
#         mapping.append(list(map(int, lines[i].split())))
#         i += 1
    
#     print(seeds, mapping)
#     new_seeds = []
#     for seed in seeds:
#         found = False
#         for s1, s2, r in mapping:
#             if s2 <= seed < s2 + r:
#                 new_seeds.append(s1 + seed - s2)
#                 found = True 
#                 break
#         if not found:
#             new_seeds.append(seed)
#     seeds = new_seeds

# print(seeds)
# print(min(seeds))
    

lines = inp.splitlines()

seeds = lines[0].split(": ")[1].split()
seeds = list(map(int, seeds))

new_seeds = []
i = 0
while i < len(seeds):
    s = seeds[i]
    r = seeds[i + 1]
    i += 2
    new_seeds.append((s, r))
seeds = new_seeds
# print(seeds)

i = 2
while i < len(lines):
    if "map" not in lines[i]:
        i += 1
        continue

    i += 1
    mapping = []
    while i < len(lines) and lines[i]:
        mapping.append(list(map(int, lines[i].split())))
        i += 1
    
    # print(seeds, mapping)
    new_seeds = []
    q = deque(seeds)
    while q:
        s, r = q.popleft()
        found = False
        for s1, s2, nr in mapping:
            if s2 <= s < s2 + nr:
                if s + r <= s2 + nr:
                    new_seeds.append((s1 + s - s2, r))
                else:
                    d = s2 + nr - s
                    assert r > d
                    new_seeds.append((s1 + s - s2, d))
                    q.append((s + d, r - d))
                found = True
                break
        if not found:
            new_seeds.append((s, r))
    seeds = new_seeds

print(seeds)
print(min(seeds, key=lambda x: x[0]))
    
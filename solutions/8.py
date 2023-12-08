from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product, cycle
from pathlib import Path
from timeit import repeat
import math

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "8"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)

inp = open(inp_file).read()

# # inp = """LLR

# # AAA = (BBB, BBB)
# # BBB = (AAA, ZZZ)
# # ZZZ = (ZZZ, ZZZ)"""

# lines = inp.splitlines()
# steps = lines[0]

# nodes = {}
# for line in lines[2:]:
#     start, other = line.split(" = ")
#     nxt = other[1:-1].split(", ")

#     nodes[start] = nxt

# ans = 0
# cur = "AAA"
# it = cycle(steps)
# while cur != "ZZZ":
#     st = next(it)
#     if st == "L":
#         cur = nodes[cur][0]
#     else:
#         cur = nodes[cur][1]
#     # print(st, cur)
#     ans += 1
# print(ans)

# inp = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

lines = inp.splitlines()
steps = lines[0]

nodes = {}
for line in lines[2:]:
    start, other = line.split(" = ")
    nxt = other[1:-1].split(", ")

    assert start not in nodes
    nodes[start] = nxt

ans = 0
it = 0
cur = [key for key in nodes if key[-1] == 'A']


def find_cycle(node):
    s = {}
    i = 0
    anss = []
    cyci = 0
    while True:
        st = steps[cyci]

        if node[-1] == "Z":
            anss.append(i)

        if (node, cyci) in s:
            return s[(node, cyci)], i, anss
        s[(node, cyci)] = i


        if st == "L":
            node = nodes[node][0]
        else:
            node = nodes[node][1]

        i += 1
        cyci = (cyci + 1) % len(steps)



cycles = []
a = 1
for node in cur:
    c = find_cycle(node)
    print(node, c)
    cycles.append(c) 
    a = math.lcm(a, c[2][0]) # this only works cuz their data is nice
print(a)
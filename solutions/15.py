from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product, repeat, chain
from pathlib import Path
from pprint import pprint

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "15"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# inp = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
inp = inp.split(",")
inp = list(map(str.strip, inp))
print(inp)

def hhash(line):
    cur = 0
    for ch in line:
        cur += ord(ch)
        cur *= 17
        cur %= 256
    return cur

# ans = 0
# for c in inp:
#     ans += hhash(c)
# print(ans)

def split_op(line: str):
    label = ""
    op = None
    for i, ch in enumerate(line):
        if ch in "-=":
            op = ch
            break
        elif ch.isalpha():
            label += ch
    value = line[i+1:]
    return label, op, value

inp = list(map(split_op, inp))
print(inp)

m = [list() for _ in range(256)]
for key, op, value in inp:
    h = hhash(key)
    if op == "=":
        done = False
        for val in m[h]:
            if val[0] == key:
                val[1] = int(value)
                done = True
                break
        if not done:
            m[h].append([key, int(value)])
    else:
        for i in range(len(m[h])):
            if m[h][i][0] == key:
                del m[h][i]
                break
print(m)

ans = 0
for i, box in enumerate(m):
    for j, slot in enumerate(box):
        ans += (i + 1) * (j + 1) * slot[1]
print(ans)


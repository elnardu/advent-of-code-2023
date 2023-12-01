from functools import cache
from collections import defaultdict, Counter
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right
from pathlib import Path

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "$day_id"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

print("Hi world!")
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "2"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# inp = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# red = 12
# green = 13
# blue = 14

# ans = 0
# for line in inp.splitlines():
#     s = line.split(":")[0]
#     game_id = int(s.split(" ")[1])

#     s = line.split(":")[1]
#     possible = True
#     for game in s.split(";"):
#         r, g, b = 0, 0, 0

#         for t in game.split(","):
#             if "blue" in t:
#                 b += int(t.split(" ")[1])
#             elif "red" in t:
#                 r += int(t.split(" ")[1])
#             elif "green" in t:
#                 g += int(t.split(" ")[1])

    
#         if r <= red and g <= green and b <= blue:
#             pass
#         else: possible = False
    
#     if possible:
#         ans += game_id

# print(ans)

red = 12
green = 13
blue = 14

ans = 0
for line in inp.splitlines():
    s = line.split(":")[0]
    game_id = int(s.split(" ")[1])

    s = line.split(":")[1]
    possible = True
    mr, mg, mb = 0, 0, 0
    for game in s.split(";"):
        r, g, b = 0, 0, 0

        for t in game.split(","):
            if "blue" in t:
                b += int(t.split(" ")[1])
            elif "red" in t:
                r += int(t.split(" ")[1])
            elif "green" in t:
                g += int(t.split(" ")[1])

        mr = max(mr, r)
        mb = max(mb, b)
        mg = max(mg, g)

    ans += mr * mb * mg

print(ans)

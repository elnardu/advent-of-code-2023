from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "1"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

def p1():
    lines = inp.split()
    s = 0
    for line in lines:
        first = None
        last = None
        for ch in line:
            if ch.isdigit():
                if first is None:
                    first = ch
                last = ch
        s += int(first + last)
        # print(line, first, last)
    print(s)


def p2():
    mapping = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    lines = inp.split()
    s = 0
    for line in lines:
        first = None
        last = None

        for i, ch in enumerate(line):
            if ch.isdigit():
                if first is None:
                    first = int(ch)
                last = int(ch)
            else:
                for word in mapping:
                    if line[i:].startswith(word):
                        if first is None:
                            first = int(mapping[word])
                        last = int(mapping[word])
                        break
        
        s += int(f"{first}{last}")

    print(s)
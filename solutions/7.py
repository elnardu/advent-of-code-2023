from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path

repo_dir = Path(__file__).parent.parent.absolute()
day_id = "7"
inp_file = repo_dir / "input" / f"{day_id}"

inpf = open(inp_file)
inp = open(inp_file).read()

# inp = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

# hands = inp.strip().split("\n")
# hands = list(map(str.split, hands))
# hands = [(x[0], int(x[1])) for x in hands]

# cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

# def get_ordering(hand):
#     c = Counter(hand)
#     mul = None
#     if mul is None and 5 in c.values():
#         mul = 1

#     if mul is None and 4 in c.values():
#         mul = 2
    
#     if mul is None and 3 in c.values() and 2 in c.values():
#         mul = 3
    
#     if mul is None and 3 in c.values():
#         mul = 4
    
#     if mul is None and Counter(c.values())[2] == 2:
#         mul = 5

#     if mul is None and 2 in c.values():
#         mul = 6

#     if mul is None:
#         mul = 7

#     ordering = [cards.index(x) for x in hand]
#     print(hand, mul, ordering)
    
#     return (mul, ordering)

# # print(hands)
# hands.sort(key=lambda x: get_ordering(x[0]))
# print(hands)
# ans = 0
# for i, val in enumerate(reversed(hands)):
#     ans += val[1] * (i+1)
            
# print(ans)

hands = inp.strip().split("\n")
hands = list(map(str.split, hands))
hands = [(x[0], int(x[1])) for x in hands]

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def get_ordering(hand):
    c = Counter(hand)
    mul = None
    if mul is None and 5 in c.values():
        mul = 1

    if mul is None and 4 in c.values():
        mul = 2
    
    if mul is None and 3 in c.values() and 2 in c.values():
        mul = 3
    
    if mul is None and 3 in c.values():
        mul = 4
    
    if mul is None and Counter(c.values())[2] == 2:
        mul = 5

    if mul is None and 2 in c.values():
        mul = 6

    if mul is None:
        mul = 7

    ordering = [cards.index(x) for x in hand]
    return (mul, ordering)

def get_ordering_adv(hand):
    mul, ordering = get_ordering(hand)
    n_jokers = hand.count("J")
    
    nhand = [x for x in hand if x != "J"]
    for p in product(cards[:-1], repeat=n_jokers):
        nnhand = nhand + list(p)
        # print(nnhand)
        nmul, _ = get_ordering(nnhand)
        mul = min(mul, nmul)
    # print(hand, mul)
    return mul, ordering

# print(hands)
hands.sort(key=lambda x: get_ordering_adv(x[0]))
print(hands)
ans = 0
for i, val in enumerate(reversed(hands)):
    ans += val[1] * (i+1)
            
print(ans)
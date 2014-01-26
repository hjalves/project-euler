#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 54
Poker hands
"""

from collections import Counter
from operator import itemgetter

h = "6H 6C 6S 6D 9D".split()
h = "4D 6S 9H QH QC".split()

def rank(c):
    v = c[0]
    d = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return d[v] if v in d else int(v)

def suit(c):
    return c[1]

def ranks(h):
    return map(value, h)

def suits(h):
    return map(suit, h)

def rank_counter(h):
    return Counter(map(rank, h))

def suit_counter(h):
    return Counter(map(suit, h))

def straight(h):
    l = sorted(ranks(h))
    is_straight = all(y == x+1 for x, y in zip(l, l[1:]))
    return is_straight and l[-1]

def flush(h):
    is_flush = len(set(suits(h))) == 1
    return is_flush and max(ranks(h))

def full_house(h):
    vc = rank_counter(h)
    is_full_house = 3 in vc.values() and 2 in vc.values()
    return is_full_house and vc.most_common(1)[0][0]

def four_kind(h):
    vc = rank_counter(h)
    is_four_kind = 4 in vc.values()
    return is_four_kind and vc.most_common(1)[0][0]

def three_kind(h):
    vc = rank_counter(h)
    is_three_kind = 3 in vc.values()
    return is_three_kind and vc.most_common(1)[0][0]

def two_pair(h):
    vc = rank_counter(h)
    pass
    

print( rank_counter(h) )

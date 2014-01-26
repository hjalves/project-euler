#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 54
Poker hands
"""

from collections import Counter, defaultdict

(NONE, ONEPAIR, TWOPAIR, THREEKIND, STRAIGHT,
 FLUSH, FULLHOUSE, FOURKIND, STRFLUSH) = range(9)

def rank(c):
    d = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return d[c[0]] if c[0] in d else int(c[0], 0)

def suit(c):
    return c[1]

def kinds(h):
    l = defaultdict(list)
    for k, v in Counter(map(rank, h)).items():
        l[v].append(k)
    return l

def handkey(h):
    k, l = kinds(h), tuple(sorted(map(rank, h), reverse=True))
    straight = all(x == y+1 for x, y in zip(l, l[1:]))
    flush = len(set(map(suit, h))) == 1
    
    if straight and flush:      return STRFLUSH, l
    if k[4]:                    return FOURKIND, k[4][0], l
    if k[3] and k[2]:           return FULLHOUSE, k[3][0], l
    if flush:                   return FLUSH, l
    if straight:                return STRAIGHT, l
    if k[3]:                    return THREEKIND, k[3][0], l
    if len(k[2]) == 2:          return TWOPAIR, max(k[2]), min(k[2]), l
    if k[2]:                    return ONEPAIR, k[2][0], l
    return NONE, l

with open("problem54/poker.txt") as textf:
   games = [[line[:5], line[5:]] for line in map(str.split, textf)]

gameswon = sum(1 for p1, p2 in games if handkey(p1) > handkey(p2))
print(gameswon)

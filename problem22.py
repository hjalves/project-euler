#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 22
Names scores
"""

with open("problem22/names.txt") as textf:
    names = [n[1:-1] for n in textf.read().split(',')]

def alph_value(name):
    cvalue = lambda c: ord(c) - ord('A') + 1
    return sum(map(cvalue, name))

print(sum(pos * alph_value(name) for pos, name in enumerate(sorted(names), 1)))

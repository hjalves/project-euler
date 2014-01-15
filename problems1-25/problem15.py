#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 15
Lattice paths
"""

d = {}
def paths(h, v):
    if (h, v) in d:
        return d[(h, v)]
    if 0 in (h, v):
        return 1
    return d.setdefault((h, v), paths(h-1, v) + paths(h, v-1))

print(paths(20, 20))


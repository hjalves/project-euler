#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 53
Combinatoric selections
"""

def pascal_triangle(n):
    pos = lambda i, j: i * (i + 1) // 2 + j     # triangle indexing
    l = [1] * pos(n+1, 0)
    for i in range(n+1):
        for j in range(1, i):
            l[pos(i, j)] = l[pos(i-1, j-1)] + l[pos(i-1, j)]
    return l

print(len([n for n in pascal_triangle(100) if n > 1000000]))

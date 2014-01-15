#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 24
Lexicographic permutations
"""

from math import factorial

def perm_i(digits, num):
    digits = list(digits)
    permutation = []
    while digits:
        perms = factorial(len(digits))
        pos, num = divmod(num, perms//len(digits))
        permutation.append(digits.pop(pos))
    return permutation
    
print("".join(map(str, perm_i(range(10), 1000000-1))))

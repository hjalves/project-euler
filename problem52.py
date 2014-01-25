#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 52
Permuted multiples
"""

# Most significant digit sequences (1x-6x):
# 1, 2, 3, 4, 5, 6 (% 3 = 0)
# 1, 2, 3, 4, 5, 7 (% 3 = 1)
# 1, 2, 3, 4, 6, 7 (% 3 = 2)
# 1, 2, 3, 5, 6, 7 (% 3 = 0)
# 1, 2, 4, 5, 6, 8 (% 3 = 2)
# 1, 2, 4, 5, 7, 8 (% 3 = 0)
# 1, 3, 4, 6, 7, 9 (% 3 = 0)
# 1, 3, 4, 6, 8, 9 (% 3 = 1)
# ----------------
# Least significant digit sequences:
# 0, 0, 0, 0, 0, 0 (% 3 = 0) (ignore)
# 1, 2, 3, 4, 5, 6 (% 3 = 0)
# 2, 4, 6, 8, 0, 2 (% 3 = 1)
# 3, 6, 9, 2, 5, 8 (% 3 = 0)
# 4, 8, 2, 6, 0, 4 (% 3 = 0)
# 5, 0, 5, 0, 5, 0 (% 3 = 0)
# 6, 2, 8, 4, 0, 6 (% 3 = 2)
# 7, 4, 1, 8, 5, 2 (% 3 = 0) 
# 8, 6, 4, 2, 0, 8 (% 3 = 1) 
# 9, 8, 7, 6, 5, 4 (% 3 = 0) (n tem 1/2/3)
# ----------------
# * digit sum must be divisible by 3
# * must contain a 5 or 0 (divisible by 5)
# * must contain at least one of [0, 2, 4, 6, 8] (divisibility by 2)
# ----------------
# will assume that it has 7 digits:
# MSD possible sequences:
# 1, 2, 3, 4, 5, 6 (% 3 = 0)  +[0, 3, 6, 9]
# 1, 2, 3, 4, 5, 7 (% 3 = 1)  +[2, 5, 8]
# 1, 2, 3, 4, 6, 7 (% 3 = 2)  impossible (cannot add 5 or 0)
# 1, 2, 3, 5, 6, 7 (% 3 = 0)  +[0, 3, 6, 9]
# 1, 2, 4, 5, 6, 8 (% 3 = 2)  +[1, 4, 7]
# 1, 2, 4, 5, 7, 8 (% 3 = 0)  +[0, 3, 6, 9]
# 1, 3, 4, 6, 7, 9 (% 3 = 0)  +[0, 3, 6, 9]
# 1, 3, 4, 6, 8, 9 (% 3 = 1)  +5
#


from itertools import product

def multiply(digits, n):
    rem, mul = 0, [0] * len(digits)
    for i, dig in enumerate(reversed(digits)):
        rem, mul[i] = divmod(dig * n + rem, 10)
    return mul, rem

def test_multiply_(digits):
    s = set(digits)
    for n in range(2, 7):
        mul, rem = multiply(digits, n)
        if set(mul) != s:
            return False
    return True

def test_multiply(num):
    s = set(split(num))
    for n in range(2, 7):
        mul = num * n
        if set(split(mul)) != s:
            return False
    return True

def split(n):
    return map(int, str(n))

for n in range(100002, 1000000//6+1, 3):
    #digits = list(split(n))
    if test_multiply(n):
        print(n)

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 14
Longest Collatz sequence
"""

import sys
from collections import defaultdict
from operator import itemgetter as iget

def collatz(nums):
    d = [1] * (nums+1)
    for n in range(2, nums+1):
        i, m = 0, n
        while m >= n:
            m = m // 2 if m % 2 == 0 else 3 * m + 1
            i += 1
        d[n] = i + d[m]
    return d

print(max(enumerate(collatz(1000000)), key=iget(1)))

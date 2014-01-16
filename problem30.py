#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 30
Digit fifth powers
"""

from functools import reduce
from math import log10

def concat(l):
    return reduce(lambda a, b: a * 10 + b, l, 0)

def split(n):
    return map(int, str(n))

def sumpower(l, power):
    return sum(d**power for d in l)

def equal_sumpower(l, power):
    return concat(l) == sumpower(l, power)

def digsize(n):
    return int(log10(n))+1 if n > 0 else 0

def build_num(num, csum, power):
    if num == csum and num > 9:
        yield num
    #if digsize(csum + 9**power) < digsize(num) + 1:
    if csum + 9**power < num * 10 + 9:
        return
    digits = range(10) if num != 0 else range(1, 10)
    for digit in digits:
        for n in build_num(num * 10 + digit, csum + digit**power, power):
            yield n


print(sum(build_num(0 , 0,  5)))

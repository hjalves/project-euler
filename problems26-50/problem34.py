#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 34
Digit factorials
"""
from math import factorial

def build_num(num=0, fsum=0):
    if num == fsum and num > 2:
        yield num
    # if adding a nine to the number results in a sum < num
    # it is impossible to continue building this number
    if fsum + factorial(9) < num*10 + 9:
        return          # backtrack
    digits = range(10) if num != 0 else range(1, 10)
    for d in digits:
        for n in build_num(num*10 + d, fsum + factorial(d)):
            yield n     # (yield from)

print(sum(build_num()))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 30
Digit fifth powers
"""

from functools import reduce

def build_num(power, num=0, psum=0):
    if num == psum and num > 9:
        yield num
    # if adding a nine to the number results in a sum < num
    # it is impossible to continue building this number
    if psum + 9**power < num*10 + 9:
        return
    digits = range(10) if num != 0 else range(1, 10)
    for d in digits:
        for n in build_num(power, num*10 + d, psum + d**power):
            yield n     # (yield from)


print(sum(build_num(5)))

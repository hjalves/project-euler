#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 40
Champernowne's constant
"""

# 9     1-digit numbers (1-9)          d = 1.......1+9*1
# 90    2-digit numbers (10-99)        d = 10......10+90*2
# 900   3-digit numbers (100-999)      d = 190.....190+900*3
# 9000  4-digit numbers (1000-9999)    d = 2890....2890+9000*4
# 90000 5-digit numbers (10000-99999)  d = 38890...38890+90000*5
# 900000 6-digit numbers .....         d = 488890..488890+900000*6

from functools import reduce
from itertools import count
from operator import mul

def i_dig(nth):
    end = 1
    for digit in count(1):
        start, end = end, 9*digit * 10**(digit-1) + end
        if start <= nth < end:
            return nth - start, digit

def dn(i, digits):
    num = i//digits + 10**(digits-1)
    pos = digits-1 - i%digits
    digit = (num//10**pos) % 10
    return digit

print( reduce(mul, (dn(*i_dig(10**p)) for p in range(7))) )

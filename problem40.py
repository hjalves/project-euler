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

# 12 ---> 12 - 9 - 1 --> 2

from itertools import count
from operator import mul
from functools import reduce

def nth_ends(digit):
    if digit == 0:
        return 1
    numbers = 9 * 10 ** (digit-1)
    return numbers * digit + nth_ends(digit-1)

def i_dig(nth):
    end = 0
    for digit in count():
        start, end = end, nth_ends(digit)
        if start <= nth < end:
            return nth - start, digit

def dn(i, digits):
    num = i//digits + 10**(digits-1)
    pos = digits-1 - i%digits
    digit = (num//10**pos) % 10
    #return num, pos, digit
    return digit

print( reduce(mul, (dn(*i_dig(10**p)) for p in range(7))) )

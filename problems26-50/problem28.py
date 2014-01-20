#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 28
Number spiral diagonals
"""

# 1x1: 1
# 3x3: 3 5 7 9        (distance: 2, first: 3,  last: 9)
# 5x5: 13 17 21 25    (distance: 4, first: 13, last: 25)
# 7x7: 31 37 43 49    (distance: 6, first: 31, last: 49)

# sequence sum: sum = (1/2) * (last + first) * n
# last element: l(n) = l(n-2) + 4*(n-1) = n**2
# spiral sum :  s(n) = s(n-2) + 4*l(n-2) + 10*(n-1) 

def spiralsum(n):
    assert n % 2 == 1
    if n == 1:
        return 1
    return spiralsum(n-2) + 4*(n-2)**2 + 10*(n-1)

print(spiralsum(1001))


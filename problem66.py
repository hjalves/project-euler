#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 66
Diophantine equation
"""

s = set(range(1001))

for i in set(s):
    if int(i**0.5)**2 == i:
        s.remove(i)

print(s)

def j_function(i, d):
    return int((i**2//d)**.5)

for i in range(2, 1000000):
    #minj = int((i**2//max(s))**.5) or 1
    #maxj = int((i**2//min(s))**.5)+1
    for d in set(s):
        j = int((i**2//d)**.5) or 1
        if i**2 % j**2 == 1 or j == 1:
            d = i**2-1 if j==1 else i**2 // j**2
            if d in s:
                print('x:', i, 'y:', j, '\td:', d, 'len', len(s))
                s.remove(d)
print(s)

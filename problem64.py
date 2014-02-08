#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 64
Odd period square roots
"""

# r, n/(sqrt(x)-d)

def expand(x, r, n, d):
    xrt = int(x**.5)
    den = (x - d*d) // n
    rem = (d + xrt) // den
    num = xrt - (d + xrt) % den
    return rem, den, num

def fraction_representation(x):
    xrt = int(x**.5)
    assert x != xrt * xrt, "Not irrational square root."
    
    sequence = []
    r, n, d = xrt, 1, xrt
    while (r, n, d) not in sequence:
        sequence.append((r, n, d))
        r, n, d = expand(x, r, n, d)
    
    return [e[0] for e in sequence]

def irrational_sqrt(max):
    return (x for x in range(max) if int(x**.5)**2 != x)


print(sum(1 for x in irrational_sqrt(10001)
            if len(fraction_representation(x)) % 2 == 0))

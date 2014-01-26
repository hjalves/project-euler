#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 55
Lychrel numbers
"""

MAXITER = 50

def reverse(n):
    m = 0
    while n != 0:
        m = m * 10 + n % 10
        n //= 10
    return m

def palindrome(n):
    return n == reverse(n)

def memoize_firstarg(f):
    dx = {}
    return lambda *a: dx[a[0]] if a[0] in dx else dx.setdefault(a[0], f(*a))

@memoize_firstarg
def test_lynchrel(n, it=0):
    n = n + reverse(n)
    if palindrome(n):
        return False
    if it >= MAXITER:
        return True
    return test_lynchrel(n, it+1 if n > 10000 else it)

print(sum(1 for n in range(10000) if test_lynchrel(n)))

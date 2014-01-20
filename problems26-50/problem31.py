#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 31
Coin sums
"""

def memoize(f):
    dx = {}
    return lambda *a: dx[a] if a in dx else dx.setdefault(a, f(*a))

@memoize
def change(total, coins):
    if not coins or total < 0:
        return 0
    elif total == 0:
        return 1
    return change(total - coins[0], coins) + change(total, coins[1:])

print(change(200, (200, 100, 50, 20, 10, 5, 2, 1)))

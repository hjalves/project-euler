#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 26
Reciprocal cycles
"""

def unit_fraction(d):
    div, mod = 0, 1
    while True:
        yield div, mod
        div, mod = divmod(mod * 10, d)
        
def recurring(d):
    digs, rems = [], {}
    for dig, rem in unit_fraction(d):
        digs.append(dig)
        if rem in rems:
            return digs[rems[rem]:]
        rems[rem] = len(digs)

d_recurring = [(d, len(recurring(d))) for d in range(2, 1000)]
print(max(d_recurring, key=lambda x: x[1]))

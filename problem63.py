#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 63
Powerful digit counts
"""

from math import log10, ceil
from itertools import count, takewhile

# I left the following commented functions to show the reasoning :)

#def digitlen(b, p):
#    return int(p*log10(b)+1)

#def is_ndigit_npower_alt(b, p):
#    return (p-1)/p <= log10(b) < 1

#def is_ndigit_npower(b, p):
#    return 10**((p-1)/p) <= b < 10

def lower_base(p):
    return ceil(10**((p-1)/p))

def lower_bases():
    return map(lower_base, count(1))

def ndigit_npower_integers():
    return sum(10 - b for b in takewhile(lambda x: x < 10, lower_bases()))

print(ndigit_npower_integers())


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 36
Double-base palindrome
"""

doublepal = lambda n: palindrom(str(n)) and palindrom(bin(n)[2:])
palindrom = lambda s: s == s[::-1]
print(sum(filter(doublepal, range(1000000))))

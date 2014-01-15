#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 4
Largest palindrome product
"""

def digits(n):
    return digits(n//10) + [n%10] if n else []

def equal_ends(l):
    return [l[0] == l[-1]] + equal_ends(l[1:-1]) if l else []

def is_palindrome(n):
    return all(equal_ends(digits(n)))

def all_3dig_comb():
    return ((i, j) for i in range(100, 1000) for j in range(i, 1000))

def all_3dig_mult():
    return (i * j for i, j in all_3dig_comb())

palproducts = filter(is_palindrome, all_3dig_mult())
print(max(palproducts))

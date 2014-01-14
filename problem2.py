#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 2
"""

def fibonacci(max):
    a, b = 1, 2
    while a <= max:
        yield a
        a, b = b, a+b

print(sum(a for a in fibonacci(4000000) if a%2==0))

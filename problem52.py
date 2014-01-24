#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 52
Permuted multiples
"""

for i in range(10):
    print(i, end=': ')
    for n in range(1,7):
        print(i*n%10, end=' ')
    print()

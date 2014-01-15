#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 20
Factorial digit sum
"""

from math import factorial
print(sum(map(int, str(factorial(100)))))

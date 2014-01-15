#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 6
Sum square difference
"""

def sum_squares(n):
    return sum(map(lambda x:x**2, range(1, n+1)))

def square_sums(n):
    return sum(range(1, n+1))**2

print(square_sums(100) - sum_squares(100))

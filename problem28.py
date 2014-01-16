#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 28
Number spiral diagonals
"""

def spiral_last(n):
    assert n % 2 == 1
    if n == 1:
        return 1
    return spiral_last(n-2) + (n-1)*4

def sum_seq(first, last, n):
    return n * (last + first) // 2

def spiral_sum(n):
    assert n % 2 == 1
    if n == 1:
        return 1
    first = spiral_last(n-2) + (n-1)
    last = first + (n-1) * 3
    return spiral_sum(n-2) + sum_seq(first, last, 4)

print(spiral_last(7))

#print( sum_seq(3, 9, 4) )

for i in range(1,10,2):
    print( i, spiral_sum(i) )


def ln(n):
    assert n % 2 == 1
    if n == 1:
        return 1
    return ln(n-2) + (n-1)*4

def sn(n):
    assert n % 2 == 1
    if n == 1:
        return 1
    return sn(n-2) + 4 * ln(n-2) + (n-1) * 10

print(sn(101))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 42
Coded triangle numbers
"""

with open("problem42/words.txt") as textf:
    s = textf.read()

words = [s[1:-1] for s in s.split(',')]

def wordvalue(w):
    return sum(ord(c) - ord('A') + 1 for c in w)

def triangle(n):
    return n * (n+1) // 2

# a funcao inversa real: (Sqrt(1+8n)-1)/2
def triangle_inv(t):
    return int((2*t)**0.5)

def is_triangle(t):
    return t == triangle(triangle_inv(t))

print(len([w for w in words if is_triangle(wordvalue(w))]))

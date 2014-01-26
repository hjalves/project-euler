#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 56
Powerful digit sum
"""

print(max(sum(map(int, str(a**b))) for a in range(100) for b in range(100)))

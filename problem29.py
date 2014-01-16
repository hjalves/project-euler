#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 29
Distinct powers
"""

print(len(set(a**b for a in range(2, 101) for b in range(2, 101))))

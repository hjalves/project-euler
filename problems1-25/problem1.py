#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 1
"""

print(sum(i for i in range(1000) if 0 in (i%3, i%5)))

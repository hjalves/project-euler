#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 48
Self powers
"""

print( str(sum(n**n for n in range(1,1001)))[-10:] )

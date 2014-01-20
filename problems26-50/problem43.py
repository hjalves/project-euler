#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 43
Sub-string divisibility
"""

def join(nl):
    return sum(b * 10**p for p, b in enumerate(reversed(nl)))

def testdiv(nl):
    firstprimes = (2, 3, 5, 7, 11, 13, 17)
    test = (join(nl[i+1:i+4]) % firstprimes[i] == 0 for i in range(len(nl)-3))
    return all(test)

def buildnum(nl, digits):
    if not testdiv(nl):
        return
    if not digits:
        yield join(nl)
    for d in digits:
        for n in buildnum(nl + [d], digits - {d}):
            yield n

def findsubstringdiv():
    return buildnum([], set(range(10)))

print(sum(findsubstringdiv()))

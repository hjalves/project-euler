#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 19
Counting Sundays
"""

from itertools import accumulate as acc

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"]

def leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def yeardays(year):
    return 366 if leap(year) else 365

def monthdays(year, month):
    assert 0 <= month < 12
    d = [0, 31, 29 if leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return list(acc(d))[month]

def firstday(year, month):
    assert 0 <= month < 12 and year >= 1900
    jan1900 = 1     # 1 = Monday: 1 Jan 1900 was a Monday.
    days = jan1900 + sum(yeardays(y) for y in range(1900, year))
    return (days + monthdays(year, month)) % 7

print(sum(1 for y in range(1901, 2001) for m in range(12)
            if firstday(y, m) == 0))

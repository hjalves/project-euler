#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 7
10001st prime
"""

from itertools import count, islice

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def primes():
    return filter(is_prime, count(2))

print(next(islice(primes(), 10000, 10001)))

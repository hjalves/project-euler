#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 47
Distinct primes factors
"""

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def primes(max):
    return filter(is_prime, range(2, max))

def prime_factors_counter(size):
    counter = [0] * size
    for p in primes(size):
        for i in range(p, size, p):
            counter[i] += 1
    return counter

def find_consecutive(l, number, times):
    count = 0
    for i, n in enumerate(l):
        if n == number:
            count += 1
        else:
            count = 0
        if count == times:
            return i-times+1

counter = prime_factors_counter(200000)
print(find_consecutive(counter, 4, 4))


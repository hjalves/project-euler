#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 50
Consecutive prime sum
"""

from itertools import accumulate

def prime_sieve(size):
    sieve = [0, 0] + [1] * (size-2)
    for i, isprime in enumerate(sieve):
        if isprime:
            for j in range(i+i, size, i):
                sieve[j] = 0
    return sieve

psieve = prime_sieve(size=1000000)

def is_prime(n):
    return bool(psieve[n])

def primes(max):
    return filter(is_prime, range(2, max))

def max_consecutive_sum_primes(max=1000000):
    ap = [0] + list(accumulate(primes(max)))
    mini, maxj = 0, 0
    
    for i in range(len(ap)):
        j = i + (maxj-mini)
        while j < len(ap) and ap[j]-ap[i] < max:
            if is_prime(ap[j]-ap[i]) and j-i > maxj-mini:
                maxj, mini = j, i
            j += 1
    
    return ap[maxj]-ap[mini]

print(max_consecutive_sum_primes())
    

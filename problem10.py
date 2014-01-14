#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 10
Summation of primes
"""

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def primes(max):
    return filter(is_prime, range(2, max))

print(sum(primes(2000000)))

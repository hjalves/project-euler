#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 3
Largest prime factor
"""

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def primes(max):
    return filter(is_prime, range(2, max+1))

def factors(n):
    return (p for p in primes(n) if n % p == 0)

def factorize(n):
    f = next(factors(n)) # lowest factor
    return [f] if f == n else [f] + factorize(n//f)

print(factorize(600851475143))

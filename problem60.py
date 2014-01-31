#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 60
Prime pair sets
"""

# Slow :(

from collections import defaultdict

def prime_sieve(size):
    sieve = [0, 0] + [1] * (size-2)
    for i, prime in enumerate(sieve):
        if prime:
            for j in range(i+i, size, i):
                sieve[j] = 0
    return sieve

print("prime sieve")
psieve = prime_sieve(size=100000000)
print("done")

def isprime_slow(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def isprime(n):
    return bool(psieve[n]) #if n < len(psieve) else isprime_slow(n)

def primes(max):
    return filter(isprime, range(2, max))

def revcat(m, n):
    while n != 0:
        m = m * 10 + n % 10
        n //= 10
    return m

def concat(n1, n2):
    rev = revcat(revcat(0, n2), n1)
    return revcat(0, rev)

def pair_prime_concats(a, b):
    return isprime(concat(a, b)) and isprime(concat(b, a))

def pairs_of_prime_concats(max):
    pairs = defaultdict(set)
    for p in primes(max):
        for q in primes(p):
            if pair_prime_concats(p, q):
                pairs[q].add(p)
    return pairs

def make_multipairs(pairs):
    return {(k,): v for k, v in pairs.items()}

def intersectpairs(pairs, mpairs):
    return {ps + (q,): mpairs[ps] & pairs[q]
            for ps, qs in mpairs.items() for q in qs}

def pairset_n_primes(pairs, n):
    mpairs = make_multipairs(pairs)
    for i in range(n-1):
        mpairs = intersectpairs(pairs, mpairs)
    return mpairs

pairs = pairs_of_prime_concats(9999)
vpairs = pairset_n_primes(pairs, 5)

for k, v in sorted(vpairs.items()):
    print(k, v, "sum:", sum(k))

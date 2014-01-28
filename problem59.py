#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Euler - Problem 59
XOR decryption
"""

from collections import Counter
from itertools import cycle

with open("problem59/cipher1.txt") as textf:
    data = bytes(map(int, textf.read().split(',')))

keya = Counter(data[0::3]).most_common(1)[0][0] ^ ord(' ')
keyb = Counter(data[1::3]).most_common(1)[0][0] ^ ord(' ')
keyc = Counter(data[2::3]).most_common(1)[0][0] ^ ord(' ')
key = bytes([keya, keyb, keyc])

unencrypted = bytes(x^k for x, k in zip(data, cycle(key)))

print(unencrypted)
print("sum:", sum(unencrypted))

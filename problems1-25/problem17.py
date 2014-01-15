#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Project Euler - Problem 17
Number letter counts
"""

fst20 = ["zero", "one", "two", "three", "four", "five",
         "six", "seven", "eight", "nine", "ten", 
         "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
mul10 = ["zero", "ten", "twenty", "thirty", "forty", "fifty",
         "sixty", "seventy", "eighty", "ninety"]

def say(n):
    assert 0 <= n <= 1000
    if n < 20:      return fst20[n]
    if n < 100:     return mul10[n//10] + ("-" + say(n%10) if n % 10 != 0 else '')
    if n < 1000:    return (say(n//100) + " hundred" + (" and " +
                            say(n%100) if n % 100 > 0 else ''))
    if n == 1000:   return "one thousand"

def countletters(s):
    return sum(1 for c in s if c not in (' ', '-'))

print(sum(countletters(say(i)) for i in range(1, 1001)))

#for i in range(0, 1001):
#    print(say(i) + "[%d]" % countletters(say(i)))

def tests():
    assert say(0) == "zero"
    assert say(1) == "one"
    assert say(5) == "five"
    assert say(9) == "nine"
    assert say(11) == "eleven"
    assert say(12) == "twelve"
    assert say(15) == "fifteen"
    assert say(20) == "twenty"
    assert say(30) == "thirty"
    assert say(50) == "fifty"
    assert say(90) == "ninety"
    assert say(21) == "twenty-one"
    assert say(25) == "twenty-five"
    assert say(37) == "thirty-seven"
    assert say(48) == "forty-eight"
    assert say(81) == "eighty-one"
    assert say(99) == "ninety-nine"
    assert say(100) == "one hundred"
    assert say(200) == "two hundred"
    assert say(400) == "four hundred"
    assert say(900) == "nine hundred"
    assert say(110) == "one hundred and ten"
    assert say(115) == "one hundred and fifteen"
    assert say(140) == "one hundred and forty"
    assert say(370) == "three hundred and seventy"
    assert say(520) == "five hundred and twenty"
    assert say(850) == "eight hundred and fifty"
    assert say(111) == "one hundred and eleven"
    assert say(219) == "two hundred and nineteen"
    assert say(521) == "five hundred and twenty-one"
    assert say(789) == "seven hundred and eighty-nine"
    assert say(999) == "nine hundred and ninety-nine"
tests()

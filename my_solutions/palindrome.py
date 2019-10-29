'''
Palindrome
==========

To help Beta Rabbit crack the lock, write a function answer(n) which returns the
smallest positive integer base b, at least 2, in which the integer n is a
palindrome. The input n will satisfy "0 <= n <= 1000".


Test cases
==========

Inputs:
    (int) n = 0
Output:
    (int) 2

Inputs:
    (int) n = 42
Output:
    (int) 4

Given a number n, return a base b where the number represented in that base is a palindrome.
'''


def answer1(n):
    base = 2
    while str(n) != str(n)[::-1]:
        base += 1
        n = n // base
    
    return base


for i in range(0, 43):
    print(answer1(i))
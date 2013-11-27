"""
 Problem: Cutting recipes 
 URL: http://www.codechef.com/problems/RECIPE

 Note: I know that euclidean algorithm is faster than this.
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


import math


def solve(numbers):
    n = len(numbers)
    for i in range(2, int(round(max(numbers)/2.0) + 1) + 1):
        while True:
            if len(list(filter(lambda x: x % i == 0, numbers))) == n:
                numbers = list(map(lambda x: int(x/i), numbers))
            else:
                break

    # cause it may have a list of primes after all
    return [1]*n if len(set(numbers)) == 1 else numbers


tests = int(input())
for test_case in range(tests):
    numbers = list(map(int, input().split()))[1:]
    print(' '.join(map(str, solve(numbers))))

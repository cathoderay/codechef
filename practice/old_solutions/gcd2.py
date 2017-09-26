"""
 Problem: GCD2 
 URL: http://www.codechef.com/problems/GCD2
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"

def gcd(a, b):
    if a < b:
        a, b = b, a
    return a if b == 0 else gcd(b, a % b)


for i in range(int(input())):
    a, b = input().split()
    print(gcd(int(a), int(b)))

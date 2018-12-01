"""
    Url: https://www.codechef.com/problems/GCD2
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b) 


for _ in range(int(input())):
    B, A = list(map(int, input().split()))
    print(gcd(A, B))


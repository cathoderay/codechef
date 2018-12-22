"""
  Url: https://www.codechef.com/problems/APPROX
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def divide(a, b, k):
    r = ''
    for i in range(k):
        if a < b: a *= 10
        r += str(a // b)
        a = a % b 
    return r


for _ in range(int(input())):
    K = int(input())

    if K == 0:
        print(3)
    else:
        print("3." + divide(4687, 33102, K))

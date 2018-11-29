
"""
  Url: https://www.codechef.com/problems/DIVIDING
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"



from math import sqrt


def is_prime(n): 
    if n == 2: return True
    lim = int(sqrt(n)) + 1
    k = 2
    while k <= lim:
        if n % k == 0:
            return False 
        k += 1
    return True


for _ in range(int(input())):
    x, y = list(map(int, input().split()))

    n = 1
    while not is_prime(x+y+n):
        n += 1
    print(n)


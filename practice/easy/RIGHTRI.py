"""
  Url: https://www.codechef.com/problems/RIGHTRI/
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


import math


def distance(x, y):
    s = (x[0] - y[0])**2
    t = (x[1] - y[1])**2
    return math.sqrt(s + t)

        
def is_right(a, b, c):
    ab = distance(a, b)
    bc = distance(b, c)
    ac = distance(c, a)
    sides = [ab, bc, ac]
    hypo = max(sides)
    cats = sides[:]; cats.remove(hypo)
    sum_squares = cats[0]**2 + cats[1]**2
    if (abs(hypo**2 - sum_squares) < 0.0000000001):
        return True
    return False


count = 0
for _ in range(int(input())):
    ns = list(map(int, input().split()))
    for i in range(0, len(ns), 6):
        a = ns[i:i+2] 
        b = ns[i+2:i+4]
        c = ns[i+4:i+6]
        if is_right(a, b, c):
            count += 1
print(count)



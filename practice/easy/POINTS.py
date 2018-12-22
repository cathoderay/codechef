"""
  Url: https://www.codechef.com/problems/POINTS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from operator import itemgetter
from functools import reduce
from math import sqrt


def distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    


for _ in range(int(input())):
    input()
    n = int(input())
    points = [tuple(map(int, input().split())) for i in range(n)]

    mpoints = [(i, -j) for i, j in points]
    s = sorted(mpoints, key=itemgetter(0, 1))
    points = [(i, -j) for i, j in s]

    d = sum([distance(points[i], points[i+1]) 
             for i in range(len(points)-1)])
    print(format("%.2f" % d))

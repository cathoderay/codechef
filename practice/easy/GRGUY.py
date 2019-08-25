"""
  Url: https://www.codechef.com/problems/GRGUY
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    
from math import inf
import sys


for _ in range(int(input())):
    l1, l2 = input(), input()

    cl1, cl2 = l1, l2
    s1 = s2 = 0
    ol = lambda l, l1, l2: l1 if l == l2 else l2
    for i in range(len(l1)):
        if l1[i] == l2[i] == '#':
            print("No")
            break
        if cl1[i] == '#':
            cl1 = ol(cl1, l1, l2)
            s1 += 1
        if cl2[i] == '#':
            cl2 = ol(cl2, l1, l2)
            s2 += 1
    else:
        print("Yes")
        print(min(s1, s2))

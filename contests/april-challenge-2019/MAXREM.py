"""
  Url: https://www.codechef.com/problems/MAXREM
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

from heapq import nlargest


int(input())
print(nlargest(2, set([0]).union(set(map(int, input().split()))))[1])

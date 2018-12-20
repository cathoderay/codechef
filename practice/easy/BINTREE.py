"""
  Url: https://www.codechef.com/problems/BINTREE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


import sys


for _ in range(int(input())):
    i, j = list(map(int, sys.stdin.readline().split()))
    
    count = 0
    while i != j:
        if i > j:
            i >>= 1
            count += 1
        else:
            j >>= 1
            count += 1
    sys.stdout.write(str(count) + " \n")

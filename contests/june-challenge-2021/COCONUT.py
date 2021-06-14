"""
  Url: https://www.codechef.com/problems/COCONUT
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

from math import ceil


def solve(xa, xb, Xa, Xb):
    return ceil(Xa / xa) + ceil(Xb / xb)


def main():
    for _ in range(int(input())):
        xa, xb, Xa, Xb = list(map(int, input().split()))
        print(solve(xa, xb, Xa, Xb))


main()

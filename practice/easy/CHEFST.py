"""
  Url: https://www.codechef.com/problems/CHEFST
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from sys import stdin


for _ in range(int(input())):
    n1, n2, m = map(int, stdin.readline().split())
    mi = ((1 + m)*m)//2
    if n2 > n1: n2, n1 = n1, n2
    print(n1 - n2 if mi >= n2 else n1 + n2 - 2*mi)


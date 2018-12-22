"""
  Url: https://www.codechef.com/problems/KINGSHIP
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    P = list(map(int, input().split()))
    mini = min(P)
    print(sum([i*mini for i in P]) -  mini**2)

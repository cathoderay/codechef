"""
  Url: https://www.codechef.com/problems/CHFINTRO
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


N, r = list(map(int, input().split()))
for _ in range(N):
    print("Good boi" if (int(input())) >= r else "Bad boi")

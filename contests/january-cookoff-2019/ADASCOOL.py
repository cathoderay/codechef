"""
  Url: https://www.codechef.com/problems/ADASCOOL
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    print("YES" if (N % 2 == 0 or M % 2 == 0) else "NO")

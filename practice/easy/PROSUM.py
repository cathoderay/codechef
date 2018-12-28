"""
  Url: https://www.codechef.com/problems/PROSUM
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().strip().split()))
    s = list(filter(lambda x: x > 1, A))
    sl = len(s)
    t = s.count(2)
    print(sl*(sl-1)//2 - t*(t-1)//2)

"""
  Url: https://www.codechef.com/problems/THREEDIF
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    n = list(map(int, input().split()))
    n.sort()
    print((n[0]*(n[1]-1)*(n[2]-2)) % (10**9+7))
    

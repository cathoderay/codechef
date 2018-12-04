"""
  Url: https://www.codechef.com/problems/WALK
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

for _ in range(int(input())):
    N = int(input())
    W = list(map(int, input().split()))
    
    maxi = 0
    for i, v in enumerate(W):
        if v + i >= maxi:
            maxi = i + v
    print(maxi)




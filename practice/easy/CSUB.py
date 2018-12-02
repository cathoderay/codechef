"""
  Url: https://www.codechef.com/problems/CSUB
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    _ = int(input())
    S = input()
    
    N = S.count('1')
    print(int(N*(N + 1)//2))

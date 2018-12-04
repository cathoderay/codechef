"""
  Url: https://www.codechef.com/problems/ANUWTA
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    
    print(N + (N + 1)*N//2) 

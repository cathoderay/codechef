"""
  Url: https://www.codechef.com/problems/CONFLIP/
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


 
for _ in range(int(input())):
    for _ in range(int(input())):
        I, N, Q = list(map(int, raw_input().split()))
                         
        if (N % 2 == 0):
            print(int(N/2))
        elif Q == I:
            print(int(N/2))
        else:
            print(int(N/2)+1) 

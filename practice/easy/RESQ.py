"""
  Url: https://www.codechef.com/problems/RESQ
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import sqrt


for _ in range(int(input())):
    N = int(input())
   
    i = int(sqrt(N)) + 1
    while True:
        if N % i == 0:
            break
        i-=1
    print(abs(N//i-i))

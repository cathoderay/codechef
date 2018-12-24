"""
  Url: https://www.codechef.com/problems/CAMPON
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    D = int(input())
    d = [0]*32
    for i in range(D):
        j, p = list(map(int, input().split()))
        d[j] = p
        
    Q = int(input())
    for i in range(Q):
        dl, p = list(map(int, input().split()))
        print("Go Camp" if sum(d[:dl+1]) >= p else "Go Sleep")

        

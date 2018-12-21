"""
  Url: https://www.codechef.com/problems/CHEFSTON
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    print(max([K//A[i]*B[i] for i in range(N)]))

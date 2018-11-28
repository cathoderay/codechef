"""
  Url: https://www.codechef.com/problems/JOHNY/
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    _ = input()
    A = [0] + list(map(int, raw_input().split()))
    K = int(input())
                 
    p = A[K]
    A.sort()
    print(A.index(p)) 

"""
  Url: https://www.codechef.com/problems/CHEFA
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))    

    A = sorted(A, reverse=True)
    print(sum(A[::2]))

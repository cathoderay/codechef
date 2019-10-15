"""
  Url: https://www.codechef.com/problems/MARM
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:]
    
    for i in range(N):
        a = A[i%N]
        b = A[N - (i%N) - 1]
        if (i + 1) <= N // 2:
            l = [a, a ^ b, b]
        else:
            l = [a, b, a ^ b]
        p = K // N 
        if (i + 1) <= K % N:
            p += 1
        if N % 2 == 1 and p >= 1 and i == (N // 2):
            B[i] = 0
        else:
            B[i] = l[p%3]
    print(*B)

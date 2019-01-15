"""
  Url: https://www.codechef.com/problems/MGAME
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, P = list(map(int, input().split()))
    
    k = N % (N//2 + 1)

    if N <= 2:
        print(P**3)
    else:
        a = (P - k)**2
        if N == P:
            print(a)
        else:
            print(a + (P - N)*((P - k) + (P - N)))


"""
  Url: https://www.codechef.com/problems/CHEFK1
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    if N == 1 and M == 0:
        print(0)
    elif (N == 1 and N == M) or N == 2 and M == 1:
        print(1)
    elif M < (N - 1) or M > N * (N + 1)/2:
        print(-1)
    elif N - 1 <= M <= N + 1:
        print(2) 
    elif N + 2 <= M <= (N << 1):
        print(3)
    else:
        x = 4 + int((M/N - 2) // .5)
        if (M/N - 2) % .5 == 0:
            x -= 1
        print(x)

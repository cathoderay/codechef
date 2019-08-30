"""
  Url: https://www.codechef.com/problems/DBOY
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"    


from math import inf


def solve(H, K):
    N = 2 * max(H) + 1
    dp = [0] + [inf for _ in range(N-1)]
    
    for i in range(1, N):
        for j in K:
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + 1)
            else:
                break
    return sum([dp[2*h] for h in H])
             

for _ in range(int(input())):
    N = int(input())
    H = list(map(int, input().split()))
    K = list(set(map(int, input().split())))
    K.sort()
    print(solve(H, K))


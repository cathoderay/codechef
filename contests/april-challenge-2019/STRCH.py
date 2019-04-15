"""
  Url: https://www.codechef.com/problems/STRCH
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    S, X = input().split()    

    dp = [0]*(N+2)
    for i in range(1, N+1):
        dp[i] = i if S[i-1] == X else dp[i-1]

    print(sum(dp))

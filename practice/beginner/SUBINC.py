"""
  Url: https://www.codechef.com/problems/SUBINC
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    count = 0
    dp = [1] + [0 for i in range(len(A) - 1)]
    for i in range(1, len(A)):
        if A[i] >= A[i - 1]:
            dp[i] = dp[i-1] + 1 
        else:
            dp[i] = 1
    print(sum(dp))

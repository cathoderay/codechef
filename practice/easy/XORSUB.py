"""
  Url: https://www.codechef.com/problems/XORSUB
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

def solve(A, K):
    m, n = len(A), 2**len(bin(max(max(A), K))[2:])
    dp = [[False for _ in range(n)] for _ in range(m)]
    dp[0][0] = True
    maxi = 0
    
    for i in range(1, m):
        for j in range(n):
            dp[i][j] = dp[i - 1][j] or dp[i - 1][A[i] ^ j]
            if dp[i][j]: maxi = max(j ^ K, maxi)
    return maxi
 

for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print(solve([0] + A, K))

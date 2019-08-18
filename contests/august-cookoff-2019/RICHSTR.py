"""
  Url: https://www.codechef.com/problems/RICHSTR
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

for _ in range(int(input())):
    N, Q = list(map(int, input().split()))
    S = input()
    dp = [-1 for i in range(len(S))]
    for i in range(len(S) - 3, -1, -1):
        if len(set(S[i:i+3])) <= 2:
            dp[i] = i + 2
        elif dp[i+1] != -1:
            dp[i] = dp[i+1]

    for _ in range(Q):
        L, R = list(map(int, input().split()))
        L -= 1; R -= 1
        print("YES" if dp[L] != -1 and dp[L] <= R else "NO")

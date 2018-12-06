"""
  Url: https://www.codechef.com/problems/LUCKYSTR
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"

    
K, N = list(map(int, input().split()))
A = [input().strip() for _ in range(K)]
B = [input().strip() for _ in range(N)]

for b in B:
    if len(b) > 46:
        print("Good")
        continue
    for a in A:
        if a in b:
            print("Good")
            break
    else:
        print("Bad")


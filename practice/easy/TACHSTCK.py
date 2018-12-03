"""
  Url: https://www.codechef.com/problems/TACHSTCK
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


N, D = list(map(int, input().split()))
L = []
for _ in range(N):
    L.append(int(input()))

L.sort()

count = 0
i = 0
while i < N - 1:
    if abs(L[i] - L[i+1]) <= D:
        count += 1
        i += 2
        continue
    i += 1
print(count)


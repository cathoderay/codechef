
"""
  Url: https://www.codechef.com/problems/LEPERMUT/
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    ns = list(map(int, input().split()))

    local = 0
    total = 0
    for i in range(N-1):
        for j in range(i + 2, N):
            if ns[i] > ns[j]:
                total += 1
                if i == j - 1:
                    local += 1 

    if local == total:
        print('YES')
    else:
        print('NO')

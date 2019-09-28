"""
  Url: https://www.codechef.com/problems/PAIRSUM2
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, Q = map(int, input().split())
    B = list(map(int, input().split()))
    se = [0 for _ in range(N)]
    so = [0 for _ in range(N)]
    se[0], so[1] = B[0], B[1]
 
    for i in range(2, N - 1, 2):
        se[i] += se[i - 2] + B[i]

    for j in range(3, N - 1, 2):
        so[j] += so[j - 2] + B[j]

    for _ in range(Q):
        p, q = map(int, input().split())
        p, q = max(p, q), min(p, q)
        if p - q == 1:
            print(B[min(p, q)-1])
            continue
        if (p - q) % 2 == 1 and (p - q) >= 3:
            a, b = (se, so) if p % 2 == 0 else (so, se)
            s = a[p - 2] - (a[q - 3] if q - 3 >= 0 else 0)
            s -= b[p - 3] - (b[q - 2] if q - 2 >= 0 else 0)
            print(s)
        else:
            print("UNKNOWN")

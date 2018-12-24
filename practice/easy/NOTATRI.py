"""
  Url: https://www.codechef.com/problems/NOTATRI
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


while input().strip() != '0':
    L = list(map(int, input().split()))

    L.sort()
    count = 0
    for k in range(len(L)-1, 1, -1):
        a = 0
        b = k - 1
        while a < b:
            if L[a] + L[b] < L[k]:
                count += b - a
                a += 1
            else:
                b -= 1
    print(count)
    

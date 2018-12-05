"""
  Url: https://www.codechef.com/problems/NOCODING
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    L = input().strip()

    prev = ord(L[0]) - 97 
    count = 2
    cur = 0
    for l in L[1:]:
        cur = ord(l) - 97
        if cur > prev:
            count += cur - prev
        elif cur < prev:
            count += (26 - prev) + cur
        count += 1
        prev = cur
    print("YES") if count <= 11 * len(L) else print("NO")

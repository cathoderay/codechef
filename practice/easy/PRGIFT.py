"""
  Url: https://www.codechef.com/problems/PRGIFT
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    evens = len(list(filter(lambda x: x % 2 == 0, a)))
    odds = len(a) - evens
    
    if k == 0:
        print("YES" if odds > 0 else "NO")
    elif evens >= k:
        print("YES")
    else:
        print("NO")


"""
  Url: https://www.codechef.com/problems/RRCODE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from operator import xor, and_, or_
from functools import reduce 


f = {"XOR": xor, "AND": and_, "OR": or_}
for _ in range(int(input())):
    N, K, ans = list(map(int, input().split()))
    A = list(map(int, input().split()))
    o = input().strip()
    if K == 0 or (o == "XOR" and K % 2 == 0):
        print(ans)
        continue
    print(reduce(f[o], A, ans))

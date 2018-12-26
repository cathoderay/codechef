"""
  Url: https://www.codechef.com/problems/ANUARM
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    Ms = list(map(int, input().split()))
    mini = min(Ms)
    maxi = max(Ms)
    s = map(lambda x: str(max(abs(x - mini), abs(x - maxi))), range(N))
    print(' '.join(s))

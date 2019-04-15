"""
  Url: https://www.codechef.com/problems/FENCE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    _, _, K = list(map(int, input().split()))
    P, S = set(), 4*K
    for k in range(K):
        r, c = list(map(int, input().split()))
        P.add((r, c))
        adjacents = [(r, c + 1), (r, c - 1),
                     (r + 1, c), (r - 1, c)]
        S -= sum([2 for nr, nc in adjacents 
                        if (nr, nc) in P])
    print(S)

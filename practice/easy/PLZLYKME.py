"""
  Url: https://www.codechef.com/problems/PLZLYKME
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

for _ in range(int(input())):
    L, D, S, C = list(map(int, input().split()))
    k = 1
    x = 0
    while x < D:
        if S*k >= L:
            print("ALIVE AND KICKING")
            break
        k *= (1 + C)
        x += 1
    else:
        print("DEAD AND ROTTING")

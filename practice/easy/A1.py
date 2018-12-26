"""
  Url: https://www.codechef.com/problems/A1
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def solve(l, m):
    if m == 0:
        return True
    if len(l) == 0 or m < 0:
        return False

    return solve(l[:-1], m - l[-1]) or solve(l[:-1], m)


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    bn = [int(input()) for i in range(n)]
    print("Yes" if solve(bn, m) else "No")

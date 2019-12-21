"""
  Url: https://www.codechef.com/problems/CHFRAN
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from sys import stdin, stdout
from math import inf
from bisect import bisect_left


def solve():
    global n, pairs

    if n == 1: return -1

    begins = sorted([pair[0] for pair in pairs])
    ends = sorted([pair[1] for pair in pairs])

    mini = inf
    for i, end in enumerate(ends):
        p = bisect_left(begins, end + 1, lo=i)
        if n - p: mini = min(p - i - 1, mini)

    return mini if mini != inf else -1


def read_input():
    global n, pairs

    n = int(input())
    pairs = []
    for _ in range(n):
        l, r = map(int, stdin.readline().split())
        pairs.append((l, r))


def write_output(s):
    stdout.write('\n'.join(map(str, s)))


def main():
    s = []
    for _ in range(int(input())):
        read_input()
        answer = solve()
        s.append(answer)
    write_output(s)


main()


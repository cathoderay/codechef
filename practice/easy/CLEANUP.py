"""
  Url: https://www.codechef.com/problems/CLEANUP/
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    done = map(int, raw_input().split())

    to_do = list(set(range(1, n + 1)) - set(done))

    to_do.sort()

    to_do = map(str, to_do)

    print ' '.join(to_do[::2])
    print ' '.join(to_do[1::2])

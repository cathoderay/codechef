"""
  Url: https://www.codechef.com/problems/MANYCHEF
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


chef = ['C', 'H', 'E', 'F']
for _ in range(int(input())):
    s = list(input())
    p = len(s) - 1
    while p >= 0:
        if ((p - 3) >= 0 and
            (s[p-3] == '?' or s[p-3] == 'C') and
            (s[p-2] == '?' or s[p-2] == 'H') and
            (s[p-1] == '?' or s[p-1] == 'E') and
            (s[p]   == '?' or s[p]   == 'F')):
            s[p-3:p+1] = chef
            p -= 4
        else:
            p -= 1
    print(''.join(s).replace('?', 'A'))

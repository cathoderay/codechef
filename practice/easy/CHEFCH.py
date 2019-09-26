"""
  Url: https://www.codechef.com/problems/CHEFCH
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    S = input()
    a = b = c = d = 0
    e, o = S[0:len(S):2], S[1:len(S):2]

    a += e.count('+')
    b += len(e) - a
    c += o.count('+')
    d += len(o) - c
    print(min(a + d, b + c))

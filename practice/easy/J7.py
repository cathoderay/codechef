"""
  Url: https://www.codechef.com/problems/J7
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    P, S = list(map(int, input().split()))
    x2 = (-P/2 + (P**2/4 - 6*S)**0.5)/-6
    z = P/4 - 2*x2
    print("%.2f" % (x2*x2*z))

"""
  Url: https://www.codechef.com/problems/LCPESY
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from collections import Counter


for _ in range(int(input())):
    A, B = input(), input()
    print(len(A) - sum((Counter(A) - Counter(B)).values()))



"""
  Url: https://www.codechef.com/problems/CIELAB
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


A, B = map(int, raw_input().split())

if str(A - B)[-1] != '9':
    print(A - B + 1)
else:
    print(A - B - 1)

"""
  Url: https://www.codechef.com/problems/OJUMPS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


a = int(input())

if a % 6 == 0 or \
   a % 6 == 1 or \
   a % 6 == 3:
    print("yes")
else:
    print("no")

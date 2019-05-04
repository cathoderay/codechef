"""
  Url: https://www.codechef.com/problems/NOLOGIC
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

from collections import Counter
from string import ascii_lowercase


for _ in range(int(input())):
    x = Counter(ascii_lowercase)
    x.subtract(Counter(input().lower()))
    x = list(filter(lambda x: x[1] > 0, x.items()))
    print(x[0][0] if len(x) > 0 else '~')


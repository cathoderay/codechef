"""
  Url: https://www.codechef.com/problems/NAME1
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from collections import Counter


for _ in range(int(input())):    
    a, b = input().split()
    c = ''.join([input() for _ in range(int(input()))])
    x, y = Counter(c), Counter(a + b)
    y.subtract(x)
    print("NO" if [x for x in list(y.values()) if x < 0] else "YES")

"""
  Url: https://www.codechef.com/problems/TOTR
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


T, M = input().split()
english = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?_" 
bytelandian = M + ''.join(map(str.upper, M)) + ".,!? "

d = {english[i]: b 
     for i, b in enumerate(bytelandian)}

for _ in range(int(T)):
    m = input() 
    print(''.join(map(lambda x: d[x], m)))

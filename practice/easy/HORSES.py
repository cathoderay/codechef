"""
  Url: https://www.codechef.com/problems/HORSES
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    _ = input()
    S = list(map(int, raw_input().split()))
                
    S.sort()
                     
    print(min(map(lambda (a, b): b - a, zip(S, S[1:]))))

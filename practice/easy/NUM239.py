"""
  Url: https://www.codechef.com/problems/NUM239
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"



for _ in range(int(input())):
    L, R = list(map(int, input().split()))
    i = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
    c = lambda x: 3*(x//10) + sum(i[0:(x%10)+1])
    print(c(R) - c(L) + i[L%10])
    

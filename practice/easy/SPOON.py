"""
  Url: https://www.codechef.com/problems/SPOON
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


spoon = lambda x: 'spoon' in x

for _ in range(int(input())):
    R, C = list(map(int, input().split()))
    m = [input().strip().lower() for i in range(R)]    
    a = [x for x in m if spoon(x)]
    b = [x for x in [''.join([m[i][j] for j in range(C) for i in range(R)])] if spoon(x)]
    print("There is indeed no spoon!" if len(a) + len(b) == 0 else "There is a spoon!")


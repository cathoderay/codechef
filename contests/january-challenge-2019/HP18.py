"""
  Url: https://www.codechef.com/problems/HP18
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, a, b = list(map(int, input().split()))
    A = list(map(int, input().split()))[:N]
    if a == b:
        print("BOB")
        continue

    ma, mb, mab = [], [], []
    for i in A:
        if i % a == 0 and i % b == 0:
            mab.append(i)
        elif i % a == 0:
            mb.append(i)
        elif i % b == 0:
            ma.append(i)
    k = 1 if len(mab) > 0 else 0 
    ma = len(ma)
    mb = len(mb)
    print("ALICE" if ma >= (mb + k) else "BOB")
    

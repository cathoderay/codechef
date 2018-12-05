"""
  Url: https://www.codechef.com/problems/CHEFZOT
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


N = int(input())
A = list(map(int, input().split()))


count = 0
maxi = 0
for i in A:
    if i != 0:
        count += 1
        if count >= maxi:
            maxi = count
    else:
        count = 0
print(maxi)

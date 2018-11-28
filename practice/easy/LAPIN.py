"""
  Url: https://www.codechef.com/problems/LAPIN
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import ceil

for _ in range(int(input())):
    s = input()
    a = ''.join(sorted(s[:len(s)//2]))
    b = ''.join(sorted(s[ceil(len(s)/2):]))

    if a == b:
        print("YES")
    else:
        print("NO")

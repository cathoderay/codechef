"""
  Url: https://www.codechef.com/problems/ANUDTC
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

for _ in range(int(input())):
    N = int(input())

    if N <= 360 and 360 % N == 0:
        print("y", end = " ")
    else:
        print("n", end = " ")

    if N > 360:
        print("n", end = " ")
    else:
        print("y", end = " ")

    if N <= 26:
        print("y")
    else:
        print("n")

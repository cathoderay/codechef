"""
  Url: https://www.codechef.com/problems/KNIGHTMV
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


in_range = lambda x: 1 <= x <= 8
list_in_range = lambda l: len(list(filter(in_range, l))) == len(l)


for _ in range(int(input())):
    s = input()
    if len(s) != 5: 
        print("Error")
        continue
    sc, sr, dc, dr = ord(s[0])-96, ord(s[1])-48, ord(s[3])-96, ord(s[4])-48
    if not (s[2] == '-' and list_in_range([sc, sr, dc, dr])):
        print("Error")
        continue
    print("Yes" if abs((sc-dc)*(sr-dr)) == 2 else "No")

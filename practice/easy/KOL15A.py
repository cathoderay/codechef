"""
  Url: https://www.codechef.com/problems/KOL15A
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

for _ in range(int(input())):
    print(sum([int(i) for i in input() 
               if i in '0123456789']))

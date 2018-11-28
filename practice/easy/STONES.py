"""
  Url: https://www.codechef.com/problems/STONES
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    J = input()
    S = input()
             
    print(len(list(filter(lambda x: x in J, S)))) 

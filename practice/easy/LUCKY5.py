"""
  Url: https://www.codechef.com/problems/LUCKY5
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

for _ in range(int(input())):
    N = input().strip()
    print(len(N) - N.count('4') - N.count('7'))

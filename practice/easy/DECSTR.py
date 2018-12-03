"""
  Url: https://www.codechef.com/problems/DECSTR
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

from string import ascii_lowercase

for _ in range(int(input())):
    n = int(input())

    alpha = ascii_lowercase

    count = 0
    i = 0
    s = ''
    while count is not n: 
        if i == 26: i = 0
        s += alpha[i]
        if i is not 0:
            count += 1
        i += 1
    print(''.join(reversed(s)))


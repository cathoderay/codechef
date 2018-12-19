"""
  Url: https://www.codechef.com/problems/COMPILER
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    s = input()
    
    n = 0
    count = 0
    t = 0
    for c in s:
        if c == '<':
            n += 1
        elif c == '>':
            if n > 0:
                n -= 1
                count += 2
                if n == 0:
                    t = count
            else:
                break
    print(t)

"""
  Url: https://www.codechef.com/problems/ATTIC
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

import sys

for _ in range(int(sys.stdin.readline())):
    S = sys.stdin.readline()

    step_count = 0
    maxi = 0
    count = 0
    for s in S:
        if s == '.':
            step_count += 1
        else:
            if step_count > maxi:
                maxi = step_count
                count += 1
            step_count = 0
    print(count)

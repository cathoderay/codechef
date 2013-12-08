"""
 Problem: Count of Maximum 
 URL: http://www.codechef.com/problems/MAXCOUNT
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from functools import reduce

for ti in range(int(input())):
    print(reduce(lambda x, y: (x[0] % y, x[1] + int(x[0] / y)), 
                 [2**i for i in range(11, -1, -1)], 
                 (int(input()), 0))
          [1])

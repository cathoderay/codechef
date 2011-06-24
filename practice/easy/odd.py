"""
 Problem: Odd
 URL: http://www.codechef.com/problems/DCE05

"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import log, floor
   
n = int(raw_input())
for i in range(n):
    print 1 << int(floor(log(int(raw_input()), 2)))

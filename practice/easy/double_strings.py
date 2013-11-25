
"""
 Problem: Double strings
 URL: http://www.codechef.com/problems/DOUBLE
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


max = lambda x: x if x % 2 == 0 else x - 1

for i in range(int(input())):
    print(max(int(input())))

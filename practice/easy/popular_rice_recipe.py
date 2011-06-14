"""
 Problem: Popular Rice Recipe
 URL: http://www.codechef.com/problems/TIDRICE
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    scores = {}
    for j in range(n):
       line = raw_input()
       (key, value) = line.split(' ')
       if value == '+':
           scores[key] = 1
       else:
           scores[key] = -1
    sum = 0
    for k in scores:
        sum += scores[k]
    print sum

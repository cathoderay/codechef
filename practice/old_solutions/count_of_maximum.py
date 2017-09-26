"""
 Problem: Count of Maximum 
 URL: http://www.codechef.com/problems/MAXCOUNT
 Note: Yes, I know it can be done faster, but this solution is
       straightforward to understand. 
       'Premature optimization is the root of all evil'
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


t = int(input())
for i in range(t):
    input()
    numbers = list(map(int, input().split()))
    count = [0]*10001
    for n in numbers:
        count[n] += 1
    c = max(count)
    v = count.index(c)
    print(v, c)

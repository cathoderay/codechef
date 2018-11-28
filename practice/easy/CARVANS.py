"""
    Url: https://www.codechef.com/problems/CARVANS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    _ = int(input())

    mspeeds = list(map(int, input().split()))
    
    s = 1
    mini = mspeeds[0]
    for i in range(1, len(mspeeds)):
        if mspeeds[i] <= mini: 
            mini = mspeeds[i]
            s += 1
    print(s)


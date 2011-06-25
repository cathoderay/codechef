"""
 Problem: Cleaning Up
 URL: http://www.codechef.com/problems/CLEANUP
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


t = int(raw_input())

for i in range(t):
    n, m = [int(i) for i in raw_input().split()]
    done = set([int(i) for i in raw_input().split()])
    all = set(range(1, n + 1))
    to_do = list(all.difference(done))
    to_do.sort()
    chef = []
    assistant = []
    for i in range(0, len(to_do)):
       if i % 2 == 0:
           chef.append(to_do[i]) 
       else:
           assistant.append(to_do[i])

    for i in range(len(chef)):
        print chef[i],
    print ""
    for i in range(len(assistant)):
        print assistant[i],
    print ""

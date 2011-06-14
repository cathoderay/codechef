"""
 Problem: Discrepancies in the Voters List
 URL: http://www.codechef.com/problems/VOTERS
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


line = raw_input()
(n1, n2, n3) = line.split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

l = []
def read(n):
    for i in range(n):
        l.append(int(raw_input()))
    return l

l = read(n1 + n2 + n3)
l.sort()

solution = {}
for i in range(len(l)):
    if not solution.has_key(l[i]):
        solution[l[i]] = 1
    else:
        solution[l[i]] += 1

s = []
for k in solution:
    if solution[k] >= 2:
        s.append(k)

s.sort()

print len(s)
for i in s:
    print i



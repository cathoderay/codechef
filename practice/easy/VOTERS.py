"""
  Url: https://www.codechef.com/problems/VOTERS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import inf

N1, N2, N3 = list(map(int, input().split()))

def read(n):
    x = []
    for i in range(n):
        x.append(int(input()))
    x.append(inf)
    return x
    
n1 = read(N1)
n2 = read(N2)
n3 = read(N3)

i1 = i2 = i3 = 0
cur_min = min(n1[0], n2[0], n3[0])
s = []
while cur_min is not inf:
    if [n1[i1], n2[i2], n3[i3]].count(cur_min) >= 2:
        s.append(cur_min)
    if n1[i1] == cur_min:
        i1 += 1
    if n2[i2] == cur_min:
        i2 += 1
    if n3[i3] == cur_min:
        i3 += 1
    cur_min = min(n1[i1], n2[i2], n3[i3])

print(len(s))
for i in s:
    print(i)




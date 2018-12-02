"""
  Url: https://www.codechef.com/problems/PCYCLE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


N = int(input())
ns = [-1] + list(map(int, input().split()))

start = i = 1
cycles = []
cur_cycle = []
m = [-1] + [0]*(N)
count = N

while True:
    if i == start and m[i] == 1:
        cur_cycle.append(i)
        cycles.append(cur_cycle)
        cur_cycle = []
        if count is not 0:
            start = i = m.index(0)
            continue
        break
    else:
        cur_cycle.append(i)
        i = ns[i]
        m[i] = 1
        count -= 1

print(len(cycles))
for c in cycles:
    print(' '.join(map(str, c)))

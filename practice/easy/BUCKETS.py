"""
  Url: https://www.codechef.com/problems/BUCKETS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


N, K = map(int, input().split())
a = list(map(int, input().split())) 
s = sum(a)
p = list(map(lambda v: v/s, a)) 
for _ in range(N-1):
    a = list(map(int, input().split()))
    sa = sum(a) + 1
    p = [(p[i] + a[i])/sa for i in range(K)]
print(*p)

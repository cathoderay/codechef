"""
  Url: https://www.codechef.com/problems/RIGHTRI/
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


distance = lambda x1, y1, x2, y2: (x1 - x2)**2 + (y1 - y2)**2

count = 0
for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1) 
    h = max(a, b, c)
    c = [a, b, c]; c.remove(h)
    if h == sum(c):
        count += 1
    
print(count)



"""
  Url: https://www.codechef.com/problems/DAILY
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import factorial as f


X, N = map(int, input().split())
cars = [input() for _ in range(N)]

gp = lambda x: list(range(4*x-3, 4*x+1))+[56-2*x, 55-2*x]
cab = lambda a, b: f(a) // (f(b) * f(a-b)) if a >= b else 0
zeros = lambda car, i: [car[p - 1] for p in gp(i)].count('0')
print(sum([cab(zeros(car, i), X) for car in cars for i in range(1, 10)]))

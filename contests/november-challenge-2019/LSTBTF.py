"""
  Url: https://www.codechef.com/problems/LSTBTF
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from sys import stdout


squares = [i*i for i in range(9001)]
ssquares = set(squares)
next_square = {4:9, 9:16, 16:25, 25:36, 36:49, 49:64, 64:81}


def any_candidate(mi, ma):
    return next((True for i in squares if i >= mi and i <= ma), False)


def nexti(m):
    for i in range(len(m) - 1, -1, -1):
        if m[i] < 81:
            m[i:len(m)] = [next_square[m[i]]]*(len(m) - i)
            return m
    else:
        return None


def search(n, m):
    while True:
        if (n + sum(m)) in ssquares:
            return ''.join(map(str, [1]*n + list(map(lambda x: int(x**.5), m))))

        if not nexti(m):
            return None


def solve(N):
    d1 = N
    while d1 >= 0:
        k = N - d1
        if any_candidate(d1 + k*4, d1 + k*81):
            r = search(d1, [4]*k)
            if r: return r
        d1 -= 1
 

s = ''
for _ in range(int(input())):
    N = int(input())
    s += solve(N) + "\n"
stdout.write(s)

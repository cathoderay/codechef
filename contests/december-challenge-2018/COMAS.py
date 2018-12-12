"""
  Url: https://www.codechef.com/problems/COMAS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def reduce(l):
    while len(l) > 6:
        print("? " + ' '.join(map(str, l[:5])))
        a, b = list(map(int, input().split()))
        l.remove(a)
        if len(l) == 6:
            break
        l.remove(b)


def solve(l):
    reduce(l)
    a, b, c, d, e, f = l
    queries = [(a, b, c, d, e),
               (a, b, c, d, f),
               (a, b, c, e, f),
               (a, b, d, e, f),
               (a, c, d, e, f),
               (b, c, d, e, f)]
    pairs = []
    for q in queries:
        print("? %d %d %d %d %d" % q)
        pairs.append((q, list(map(int, input().split()))))
    
    exc = []
    for q1, v1 in pairs:
        for q2, v2 in pairs:
            if v1 != v2:
                diff = list(set(q1).difference(set(q2)))
                if v1[1] == v2[0] and len(diff) == 1:
                    exc.append(diff[0])
        exc.append(v1[0]) 
        exc.append(v1[1]) 
    return set([a, b, c, d, e, f]).difference(set(exc)).pop()


for _ in range(int(input())):
    N = int(input())
    print("! " + str(solve(list(range(1, N + 1)))))

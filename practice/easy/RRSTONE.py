"""
  Url: https://www.codechef.com/problems/RRSTONE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def f(A):
    maxi = max(A)
    return [maxi - A[i] for i in range(len(A))]


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

if K == 0:
    print(' '.join(map(str, A)))
else:
    if K % 2 == 1:
        print(' '.join(map(str, f(A))))
    elif min(A) < 0:
        print(' '.join(map(str, f(f(A)))))
    else:
        print(' '.join(map(str, A)))

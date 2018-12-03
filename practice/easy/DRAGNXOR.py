"""
  Url: https://www.codechef.com/problems/DRAGNXOR
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, A, B = list(map(int, input().split()))
    bA = format(A, 'b')
    A = '0'*(N-len(bA)) + bA
    A1 = A.count('1')
    A0 = A.count('0')
   
    bB = format(B, 'b')
    B = '0'*(N-len(bB)) + bB
    B1 = B.count('1')
    B0 = B.count('0')

    ones = min(A1, B0) + min(A0, B1)
    s = '1'*ones + '0'*(N-(ones))

    print(int(s, 2))
    

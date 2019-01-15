"""
  Url: https://www.codechef.com/problems/DIFNEIGH
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    m = [[0 for j in range(M)] for i in range(N)]
    
    if N == 1 or M == 1:
        k = [1, 1, 2, 2]*13
        if N >= 3 or M >= 3:
            print(2)
        else:
            print(1)
        if N == 1:
            m[0] = k[:M] 
        elif M == 1:
            t = k[:N]
            for i in range(N):
                m[i][0] = t[i]

    elif N <= 2 or M <= 2:
        k = [1, 2, 3]*17
        if N >= 3 or M >= 3:
            print(3)
        else:
            print(2)
        
        if N == 2:
            m[0] = k[:M]
            m[1] = k[:M]
        elif M == 2:
            t = [1, 2]
            t[0] = k[:N]
            t[1] = k[:N]
            for i in range(N):
                m[i][0] = t[0][i]
                m[i][1] = t[1][i]
    
    elif N >=3 and M >= 3:
        k = [[2, 2, 4, 4]*13,
             [1, 3, 3, 1]*13,
             [4, 4, 2, 2]*13,
             [3, 1, 1, 3]*13]   
        print(4)
        for i in range(N):
            m[i] = k[(i % 4)][:M]
    
    for i in range(N):
        print(' '.join(map(str, m[i])))

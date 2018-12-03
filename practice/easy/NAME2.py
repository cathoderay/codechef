"""
  Url: https://www.codechef.com/problems/NAME2
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

for _ in range(int(input())):
    M, N = input().split()
    
    if len(N) < len(M):
        M, N = N, M
    
    i = 0
    for n in N:
        if n == M[i]:
            i += 1
            if i == len(M):
                print("YES")
                break
    else:
        print("NO")
            

"""
  Url: https://www.codechef.com/problems/ANUBTG
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    C = list(map(int, input().split()))
    
    C = sorted(C, reverse=True)
    cost = 0    
    i = 0
    while i < len(C):
        if i + 1 < len(C):
            cost += C[i] + C[i+1]
        else:
            cost += C[i]
            break
        i += 4
    print(cost)




        


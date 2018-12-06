"""
  Url: https://www.codechef.com/problems/PLAYFIT
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    G = list(map(int, input().split()))
    
    if len(G) < 2: 
        print("UNFIT")
        continue

    sol = 0
    mini = G[0]
    for i in range(1, len(G)):
        dif = G[i] - mini
        if (dif > sol): sol = dif
        if G[i] < mini: mini = G[i]
    print('UNFIT' if sol <= 0 else sol)
         

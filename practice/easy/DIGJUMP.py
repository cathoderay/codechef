""" Url: https://www.codechef.com/problems/DIGJUMP """


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

from math import inf

S = list(map(int, input().strip()))

a = [[] for _ in range(10)]
[a[v].append(i) for i, v in enumerate(S)]
d = [False] * 10
ml = [(False, inf)] * len(S); ml[0] = (True, 0)
q = [0]

while len(q):
    cur = q.pop(0)

    if cur == len(S) - 1:
        print(ml[cur][1])
        break

    for adj in [cur - 1, cur + 1]: 
        if ((not (0 <= adj < len(S))) 
             or ml[adj][0]): 
            continue
        ml[adj] = (True, ml[cur][1] + 1)
        q.append(adj) 

    if d[S[cur]] == False:
        d[S[cur]] = True
        for p in a[S[cur]]:
            if ml[p][0] == True: continue
            ml[p] = (True, ml[cur][1] + 1)
            q.append(p)

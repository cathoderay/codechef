"""
  Url: https://www.codechef.com/problems/GRID
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    m = [input().strip() for j in range(N)]
    
    mc = [[0 for i in range(N)] for j in range(N)]
    for r in range(N):
        mc[r][N-1] = 1 if m[r][N-1] == '#' else 0
        for c in range(N-2, -1, -1):
            if m[r][c] == '#' or mc[r][c+1] == 1:
                mc[r][c] = 1
    s = 0
    for c in range(N):
        for r in range(N-1, -1, -1):
            if m[r][c] == '.':
                if mc[r][c] == 0: s += 1
            else: break
    print(s)



"""
  Url: https://www.codechef.com/problems/ADAKNG
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def adjacents(r, c):
    m = [(r - 1, c - 1),(r - 1, c), (r - 1, c + 1),
         (r, c - 1), (r, c + 1),
         (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
    return list(filter(lambda x: 0 <= x[0] <= 7 and 0 <= x[1] <= 7, m))

def get_marked(m):
    return [(i, j) for i in range(8) 
                   for j in range(8) 
                   if m[i][j] == 1]

for _ in range(int(input())):
    R, C, K = list(map(int, input().split()))    
    m = [[0 for i in range(8)] for i in range(8)]

    m[R-1][C-1] = 1

    for i in range(K):
        for (r, c) in get_marked(m):
            for (rl, cl) in adjacents(r, c):
                m[rl][cl] = 1

    print(sum(m[i][j] for i in range(8) 
                      for j in range(8)))

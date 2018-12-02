"""
  Url: https://www.codechef.com/problems/LEBOMBS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    S = input()

    count = 0 
    for i in range(N):
        if S[i] == '1' or (i > 0 and S[i-1] == '1') or \
           (i < N - 1 and S[i + 1] == '1'):
           continue
        count += 1
    print(count)

    #alternative solution?
    #S = '0' + input() + '0'
    #count = 0
    #for i in range(1, N+1):
    #    if S[i-1] == '0' and S[i+1] == '0' and S[i] == '0':
    #        count += 1
    #print(count)

    

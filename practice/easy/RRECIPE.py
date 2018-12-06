"""
  Url: https://www.codechef.com/problems/RRECIPE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    S = input()
    lim = len(S) - 1

    sol = 1
    for i in range(len(S)//2):    
        if S[i] == '?':
            if S[lim - i] == '?':
                sol = (sol * 26) % 10000009
        else:
            if S[i] != S[lim - i] and S[lim - i] != '?':
                print(0)
                break
    else:
        if len(S) % 2 == 1:
            if S[len(S)//2] == '?':
                sol = (sol * 26) % 10000009
        print(sol)



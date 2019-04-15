"""
  Url: https://www.codechef.com/problems/KLPM
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

S = input()

def is_palindrome(s):
    for i in range(len(s)//2):
        if not s[i] == s[len(s) - 1 - i]:
            return False
    return True

def subs(s, f):
    r = []
    for i in range(s, f):
        for j in range(i+1, f+1):
            r.append((i, j))
    return r

substrings = subs(0, len(S))
r = 0
for ai, bj in substrings:
    for xi, yj in substrings:
        if xi >= bj:
            word = S[ai:bj] + S[xi:yj]
            if is_palindrome(word):
                r += 1
print(r)


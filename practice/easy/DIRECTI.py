"""
  Url: https://www.codechef.com/problems/DIRECTI
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    s, d = [], []
    for i in range(N):
        m = input().split() 
        s.append(' '.join(m[2:]))
        if not m[0] == 'Begin':
            d.append("Right" if m[0] == "Left" else "Left")

    print("Begin on %s" % (s.pop()))
    for i in range(N-1):
        print("%s on %s" % (d.pop(), s.pop()))
    print()

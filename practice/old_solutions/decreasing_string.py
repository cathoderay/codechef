import string

t = int(raw_input())
for i in range(t):
    k = int(raw_input())
    l = list(string.lowercase*4)

    p = k + 1
    if k > 25 and k < 51:
        p += 1
    if k > 50 and k < 76:
        p += 2
    if k > 75:
        p += 3

    s = l[:p]
    s.reverse()
    print(''.join(s))

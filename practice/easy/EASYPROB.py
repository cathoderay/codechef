"""
  Url: https://www.codechef.com/problems/EASYPROB
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def repr(n):
    b = list(bin(n)[2:])
    b.reverse()
    s = []
    for i, v in enumerate(b):
        if v == '1':
            if i == 0 or i == 2:
                s.append('2(%d)' % i)
            elif i == 1:
                s.append("2")
            else:
                s.append("2(%s)" % repr(i))
    s.reverse()
    return '+'.join(s)


ns = [137, 1315, 73, 136, 255, 1384, 16385]
for n in ns:
    print("%d=%s" % (n, repr(n)))


"""
solution:
137=2(2(2)+2+2(0))+2(2+2(0))+2(0)
1315=2(2(2+2(0))+2)+2(2(2+2(0)))+2(2(2)+2(0))+2+2(0)
73=2(2(2)+2)+2(2+2(0))+2(0)
136=2(2(2)+2+2(0))+2(2+2(0))
255=2(2(2)+2+2(0))+2(2(2)+2)+2(2(2)+2(0))+2(2(2))+2(2+2(0))+2(2)+2+2(0)
1384=2(2(2+2(0))+2)+2(2(2+2(0)))+2(2(2)+2)+2(2(2)+2(0))+2(2+2(0))
16385=2(2(2+2(0))+2(2)+2)+2(0)
"""

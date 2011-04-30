"""
 Problem: A very easy problem
 URL: http://www.codechef.com/problems/EASYPROB
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def solve(n):
    b = list(bin(n)[2:])
    b.reverse()
    s = []
    for i, v in enumerate(b):
        if v == '1':
            if i == 0 or i == 2:
                s.append("2(%d)" % i)
            elif i == 1:
                s.append("2")
            else:
                s.append("2(%s)" % solve(i))
    s.reverse()
    return '+'.join(s)

print "137=%s" % solve(137)
print "1315=%s" % solve(1315)
print "73=%s" % solve(73)
print "136=%s" % solve(136)
print "255=%s" % solve(255)
print "1384=%s" % solve(1384)
print "16385=%s" % solve(16385)


"""
Output:
137=2(2(2)+2+2(0))+2(2+2(0))+2(0)
1315=2(2(2+2(0))+2)+2(2(2+2(0)))+2(2(2)+2(0))+2+2(0)
73=2(2(2)+2)+2(2+2(0))+2(0)
136=2(2(2)+2+2(0))+2(2+2(0))
255=2(2(2)+2+2(0))+2(2(2)+2)+2(2(2)+2(0))+2(2(2))+2(2+2(0))+2(2)+2+2(0)
1384=2(2(2+2(0))+2)+2(2(2+2(0)))+2(2(2)+2)+2(2(2)+2(0))+2(2+2(0))
16385=2(2(2+2(0))+2(2)+2)+2(0)
"""

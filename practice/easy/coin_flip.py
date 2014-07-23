import sys

for t in xrange(int(sys.stdin.readline())):
    for l in xrange(int(sys.stdin.readline())):
        i, n, q = sys.stdin.readline().split()
        n = int(n)

        s = n//2
        if i == q:
            print(s)
        else:
            print(n - s)

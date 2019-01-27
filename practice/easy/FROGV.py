"""
  Url: https://www.codechef.com/problems/FROGV
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

distance = lambda x, y: abs(x - y)

N, K, P = list(map(int, input().split()))
A = list(map(int, input().split()))
S = [(i, j) for i, j in enumerate(A)]
S = sorted(S, key=lambda x: x[1])


class QUW:
    def __init__(self, n):
        self.pi = list(range(0, n + 1))
        self.size = [1]*(n + 1)

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb: return

        if self.size[ra] < self.size[rb]:
           self.pi[ra] = rb;
           self.size[rb] += self.size[ra]
        else:
            self.pi[rb] = ra
            self.size[ra] += self.size[rb]

    def find(self, a):
        while not self.pi[a] == a:
            a = self.pi[a]
        return a

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def add(self, a, b):
        if not self.connected(a, b):
            self.union(a, b)


QUW = QUW(N)
for i in range(N - 2, -1, -1):
    if distance(S[i + 1][1], S[i][1]) <= K:
        QUW.add(S[i + 1][0], S[i][0])


for _ in range(P):
    a, b = list(map(int, input().split()))
    a, b = a-1, b-1

    print("Yes" if QUW.connected(a, b) else "No")

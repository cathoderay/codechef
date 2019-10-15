"""
  Url: https://www.codechef.com/problems/BACREP
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from sys import stdin
from collections import namedtuple, defaultdict


Node = namedtuple('Node', ['i', 'parent', 'children'])


def travel_up(node, t, a):
    c, ac = 0, 0
    if len(node.children) == 0:
        while ac <= t and node:
            c += a[node.i]
            k = t - ac
            for x in p[node.i]:
                if x[0] <= k:
                    c += x[1]
                elif x[0] > k:
                    break
            node = node.parent
            ac += 1
        return c
    while ac <= t and node:
        k = t - ac
        for x in p[node.i]:
            if x[0] == k:
                c += x[1]
            elif x[0] > k:
                break
        if ac == t:
            c += a[node.i]
        node = node.parent
        ac += 1
    return c

def bfs(adj, N):
    nodes = [0 for _ in range(N)]
    nodes[0] = Node(0, None, [])
    v = set([0])
    q = [nodes[0]]
    while len(v) < N:
        cur = q.pop(0)
        for i in adj[cur.i]:
            if i not in v:
                v.add(i)
                new_node = Node(i, cur, [])
                nodes[i] = new_node
                q.append(new_node)
                cur.children.append(new_node)
    return nodes

N, Q = map(int, input().split())
adj = [set() for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, stdin.readline().split())
    x -= 1
    y -= 1
    adj[x].add(y)
    adj[y].add(x)
a = [int(i) for i in stdin.readline().split()]
p = defaultdict(list)

nodes = bfs(adj, N)

for i in range(1, Q+1):
    q = stdin.readline().split()
    if len(q) == 3:
        _, v, k = q
        v = int(v)
        k = int(k)
        p[v-1].append((i, k))
        p[v-1].sort(key=lambda x: x[0])
    else:
        _, v = q
        v = int(v)
        print(travel_up(nodes[v-1], i, a))

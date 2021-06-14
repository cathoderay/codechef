"""
  Url: https://www.codechef.com/problems/SUBTRCOV
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

from sys import stdin, stdout


WHITE = 0
GRAY = 1
BLACK = 2

read_numbers = lambda: list(map(int, stdin.readline().strip().split()))
output_line = lambda x: stdout.write(x)


def find_farthest_leaf(N, E, root=0):
    color = [WHITE] * N
    farthest_leaf = root
    level = 0
    max_level = 0

    color[root] = GRAY
    stack = [root]

    while stack:
        cur = stack[-1]

        if color[cur] == BLACK:
            stack.pop()
            level -= 1
            continue

        level += 1
        if level >= max_level:
            max_level = level
            farthest_leaf = cur

        for child in E[cur]:
            if color[child] == BLACK:
                continue

            if color[child] == WHITE:
                color[child] = GRAY
                stack.append(child)

        color[cur] = BLACK
    return farthest_leaf


def search_strips(N, E, root):
    color = [WHITE] * N
    strips = [[] for _ in range(N)]
    children = [[] for _ in range(N)]
    leafs = [False] * N

    color[root] = GRAY
    stack = [root]

    while stack:
        cur = stack[-1]

        if color[cur] == BLACK:
            """
            When all children of "cur" node are processed
            and it is ready to get out of the stack we can
            calculate the strips it contributes to the 
            tree until this point, so it can be collected by its 
            parent later, like a DFS in a recursive approach 
            saving its returning value to be used by the caller.
            """
            stack.pop()

            new_strips = []
            for child in children[cur]:
                if leafs[child]:
                    new_strips += [1]
                else:
                    if len(strips[child]):
                        strips[child][0] += 1
                    new_strips += strips[child]
            new_strips.sort(reverse=True)
            strips[cur] = new_strips
            continue

        for child in E[cur]:
            if color[child] == BLACK:
                continue

            if color[child] == WHITE:
                color[child] = GRAY
                stack.append(child)

            children[cur].append(child)
        leafs[cur] = False if children[cur] else True
        color[cur] = BLACK
    return strips[root]


def solve(N, E, k):
    if k == 1: return 1
    if k == 2: return 2

    farthest_leaf = find_farthest_leaf(N, E)
    strips = search_strips(N, E, root=farthest_leaf)

    max_k = 1
    solution = 1
    for strip in strips:
        max_k += strip
        solution += 1
        if k <= max_k:
            return solution


def main():
    solutions = []
    for _ in range(int(input())):
        n, k = read_numbers()
        E = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v = read_numbers()
            u -= 1
            v -= 1
            E[u].append(v)
            E[v].append(u)
        solution = solve(n, E, k)
        solutions.append(str(solution))
    solutions = '\n'.join(solutions)
    output_line(solutions)


main()

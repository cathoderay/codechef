"""
  Url: https://www.codechef.com/problems/SHROUTE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from bisect import bisect_left
from sys import stdin, stdout
from math import inf


read_line = lambda: stdin.readline().strip()
output_line = lambda x: stdout.write(x)
read_numbers = lambda: list(map(int, read_line().split()))


def find_min_dist(A, ones, twos, ones_set, twos_set, v):
    if v == 0 or v in ones_set or v in twos_set: return 0

    left = bisect_left(ones, v - 1)
    if left == len(ones) or ones[left] >= v: left -= 1
    if left == -1 or A[ones[left]] != 1 or ones[left] >= v: left = inf
    else: left = ones[left]

    right = bisect_left(twos, v + 1)
    if right == len(twos): right = -1
    if right == -1 or A[twos[right]] != 2 or twos[right] <= v: right = inf
    else: right = twos[right]

    if left == right == inf: return -1
    return min(abs(v - left), abs(right - v))


def solve(A, B):
    ones = [i for i, v in enumerate(A) if v == 1]
    twos = [i for i, v in enumerate(A) if v == 2]
    ones_set = set(ones)
    twos_set = set(twos)
    params = [A, ones, twos, ones_set, twos_set]
    solution = [str(find_min_dist(*params, b - 1)) for b in B]
    return ' '.join(solution) + '\n'


def main():
    for _ in range(int(input())):
        N, M = read_numbers()
        A = read_numbers()[:N]
        B = read_numbers()[:M]
        answer = solve(A, B)
        output_line(answer)


main()

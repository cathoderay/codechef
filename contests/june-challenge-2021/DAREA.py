"""
  Url: https://www.codechef.com/problems/DAREA
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import inf
from sys import stdin


read_line = lambda: stdin.readline().strip()
read_point = lambda: tuple(map(int, read_line().split()))
box_area = lambda left, right: (right[1] - left[1]) * (right[0] - left[0])


def solve(p):
    sort_by_x = sorted(p, key=lambda x: (x[0], -x[1]))

    box_left = []
    min_x, min_y = sort_by_x[0]
    max_x, max_y = sort_by_x[0]
    for x, y in sort_by_x:
        if x < min_x: min_x = x
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if y > max_y: max_y = y
        box_left.append([(min_x, min_y), (max_x, max_y)])

    box_right = []
    min_x, min_y = sort_by_x[-1]
    max_x, max_y = sort_by_x[-1]
    for x, y in sort_by_x[::-1]:
        if x < min_x: min_x = x
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if y > max_y: max_y = y
        box_right.append([(min_x, min_y), (max_x, max_y)])

    area = inf
    for i in range(len(sort_by_x)):
        area_left = box_area(*box_left[i])
        area_right = box_area(*box_right[len(sort_by_x)-2-i])
        new_area = area_left + area_right
        if new_area < area: area = new_area
    return area


def main():
    for _ in range(int(input())): 
        N = int(input())
        p = [read_point() for _ in range(N)]
        x = solve(p)
        y = solve([(y, x) for x, y in p])
        solution = min(x, y)
        print(solution)


main()
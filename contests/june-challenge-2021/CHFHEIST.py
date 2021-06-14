"""
  Url: https://www.codechef.com/problems/CHFHEIST
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

def solve(D, d, P, Q):
    streaks = D // d
    sum = 0
    if streaks >= 1:
        first = P
        last = P + Q * (streaks - 1)
        sum += d * (first + last) * streaks // 2
    remains = D % d
    if remains > 0:
        last = P + Q * streaks
        sum += remains * last
    return sum


def main():
    for _ in range(int(input())):
        D, d, P, Q = list(map(int, input().split()))
        print(solve(D, d, P, Q))


main()

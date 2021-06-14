"""
  Url: https://www.codechef.com/problems/BITTUP
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from sys import stdin, stdout


MOD = 10 ** 9 + 7
MAX_N = 10 ** 6

read_line = lambda: stdin.readline().strip()


def exp(b, e):
    if b == 0: return 0
    if e == 0: return 1

    if e % 2 == 0: return (exp(b, e // 2) ** 2) % MOD
    else: return (b % MOD) * (exp(b, e - 1) % MOD) % MOD


def solve(N, M, dp):
    return exp((((dp[N - 1]) - 1) % MOD), M)


def pre_calculate():
    dp = [1 for _ in range(MAX_N)]
    for i in range(MAX_N):
        dp[i] = (dp[i - 1] * 2) % MOD
    return dp


def main():
    solutions = []
    dp = pre_calculate()
    for _ in range(int(input())):
        N, M = list(map(int, read_line().split()))
        solution = solve(N, M, dp)
        solutions.append(solution)
    stdout.write('\n'.join(map(str, solutions)))


main()

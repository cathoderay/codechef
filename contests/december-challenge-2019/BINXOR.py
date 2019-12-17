"""
  Url: https://www.codechef.com/problems/BINXOR
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from sys import stdin, stdout


MAXN = 10000 + 1
MOD = 1000000007


rline = lambda: stdin.readline().strip()
inverse_mul = lambda x: pow(x, MOD - 2, MOD)


def comb(n, r):
    return (fact[n] * inverse_mul(fact[r] * fact[n-r])) % MOD


def solve():
    global n, a, b

    a = a.count('1')
    b = b.count('1')

    froma = abs(a - b)
    toa = min(n - a, b) + min(n - b, a)

    s = 0
    for i in range(froma, toa + 1, 2):
        s += comb(n, i)

    return s % MOD


def read_input():
    global n, a, b
    n, a, b = int(rline()), rline(), rline()


def write_output(s):
    stdout.write('\n'.join(map(str, s)))


def pre_compute():
    global fact

    fact = [1] * MAXN
    for i in range(1, MAXN):
        fact[i] = (fact[i-1] * i) % MOD


def main():
    pre_compute()
    s = []
    for _ in range(int(input())):
        read_input()
        answer = solve()
        s.append(answer)
    write_output(s)


main()

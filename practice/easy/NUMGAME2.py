"""
  Url: https://www.codechef.com/problems/NUMGAME2
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


"""
    Brute force attempt to come up 
    with an hypothesis to the actual
    solution.

MAXN = 1000 
primes = [1]*(MAXN+1)
for i in range(2, MAXN):
    if primes[i] == 1:
        for j in range(2*i, MAXN, i):
            primes[j] -= 1


def pi(n):
    return list(map(lambda x: x[0], 
                list(filter(lambda x: x[0] is not 0 and x[1] == 1, 
                     list(enumerate(primes[0:n]))))))


switch = lambda p: 'alice' \
         if p == 'bob' else 'bob'


def solve(n, player='bob'):
    if n == 1:
        return switch(player)

    new_player = switch(player)
    moves = [solve(n - p, new_player) for p in pi(n)]
    for m in moves:
        if m == player:
            return player
    return new_player


for i in range(1, 50):
    print(i, solve(i, 'bob'))

It turns out that the solution is an 
arithmetic progression:
1,5,9,...
Any prime can be written in the form 4n - 1 or 4n + 1...

TODO: prove it by mathematical induction...
"""


for _ in range(int(input())):
    N = int(input())
    s = 'BOB' if N % 4 != 1 else 'ALICE'
    print(s)

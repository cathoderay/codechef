"""
  Url: https://www.codechef.com/problems/EQUATION
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


"""
    Problem:
        number of solutions of a + b + c <= N
        with 0 <= a <= A; 0 <= b <= B; 0 <= c <= C
    Key ideas:
        0. ignore the constraints of a, b, c
        1. calculate the number of solutions of
           a + b + c = N:
            for that, translate the combinatorial
            problem into a simpler one, which is:
            organize o's (N) and |'s (2), e.g.:
            if N = 10, one possible solution is:
              o o | o o o | o o o o o 
              where a = 2, b = 3, c = 5
            this allows us to have zero's as solutions,
            e.g.:
              | | o o o o o o o o o o
              where a = 0, b = 0, c = 10
            So, the number of possible solutions of
            a + b + c = N is equal to: 
            C(n + 2, 2) = (n + 2)! / (2! n!)
                        = (n + 2)*(n + 1) / 2
        2. now, sum up all the possible solutions for
            a + b + c <= N. In order to calculate that,
            you need the expression for the sum of squares.
            Hint: start with (n - 1)^3 
            The sum is equal to: 

                         (i + 2)*(i + 1)   (n + 1)*(n + 2)*(n + 3)
            sum(i=0->n)  --------------- = -----------------------
                                   2                    6 

        3. Use the pidgeon hole + inclusion-exclusion
            principle to deal with the A, B, C constraints.

"""
 

for _ in range(int(input())):
    N, A, B, C = list(map(int, input().split()))

    f = lambda N: (N+1)*(N+2)*(N+3)//6
    is_positive = lambda x: x >= 0
    to_sum = [N, N-A-B-2, N-B-C-2, N-A-C-2]
    to_subtract = [N-A-1, N-B-1, N-C-1, N-A-B-C-3]
    do = lambda x: sum(map(f, filter(is_positive, x)))
    print(do(to_sum) - do(to_subtract))

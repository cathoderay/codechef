/*
 Problem: Summing subsets
 URL: http://www.codechef.com/problems/RESN05

 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com

 Observation: It's easy to see that:

 F(n) =  2^(n - 1)n + 2F(n - 1)

 Resolving for n - 1:
 F(n) = 2^(n - 1)((n - 1) + n) + 4F(n - 2)
 F(n) = 2^(n - 1)((n - 2) + (n - 1) + n) + 8F(n - 3)

 Generalization:
 F(n) = 2^(n - 1)(1 + 2 + 3 + ... + n)
 F(n) = 2^(n - 1)((1 + n)n/2)
 F(n) = 2^(n - 2)(1  + n)n, n >= 2
 F(n) = 2^(n - 2)(n^2 + n), for all n >= 2, since the base is F(1) = 1.

 There's a "jump from the cat" to see that for n > 24 the solution is 8388608 - 1.
 Trying to convince myself yet...
*/


#include<stdio.h>

long long int solve(int n) {
    int i;
    long long int  s = 1;
    for(i = 2; i <= n; i++ ) {
        s = (s + ((1 << (i - 2)) % 8388608)*((i*i + i) % 8388608 )) % 8388608;
    }
    return s;
}

int main() {
    int i, t;
    long long int  n;
    scanf("%d", &t);
    for(i = 0; i < t; i++) {
        scanf("%lld", &n);
        if (n <= 23) 
            printf("%lld\n", solve(n));
        else
            printf("8388607\n");
    }
    return 0;
}

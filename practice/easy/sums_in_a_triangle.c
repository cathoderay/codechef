/*
 Problem: Sums in a triangle
 URL: http://www.codechef.com/problems/SUMTRIAN
 
 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com

 Observation: Used memoization technique. It can be a
 little bit faster. Actually, it's not necessary to allocate
 all the matrix, just the larger line of it -- last one.
 But it solves the problem in codechef within the given 
 Time Limit.
 Brute force, without memoization gives a O(2^n).
 With memoization: O(n^2).
*/


#include<stdio.h>

int m[101][101];

int main() {
    int n, t, i, j, k, lines;
    
    scanf("%d\n", &n);
    for(t = 0; t < n; t++) {
        scanf("%d\n", &lines);
    
        for(i = 0; i < lines; i++) 
            for(k = 0; k <= i; k++) 
               scanf("%d", &m[i][k]);

        for(i = lines - 2; i >= 0; i--)
            for(j = 0; j <= i; j++)
                m[i][j] += m[i+1][j] > m[i+1][j+1] ? m[i+1][j] : m[i+1][j+1];

         printf("%d\n", m[0][0]);
    }
    return 0;
}

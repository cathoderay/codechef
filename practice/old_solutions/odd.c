/*
 Problem: Odd
 URL: http://www.codechef.com/problems/DCE05
 
 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com
*/


#include<stdio.h>
#include<math.h>

int main() {
    int t, n, i, sol;
 
    scanf("%d", &t);
    for(i = 0; i < t; i++) {
        scanf("%d", &n);
        printf("%d\n", 1 << (int)floor(log(n)/log(2)));
    }

    return 0;
}

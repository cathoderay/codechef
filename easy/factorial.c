/*
 Problem: Factorial
 URL: http://www.codechef.com/problems/FCTRL

 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com
*/


#include<stdio.h>

int main() {
    int n, step, sum, t, i;

    scanf("%d", &t);
    for(i = 0; i < t; i++) {
        sum = 0;
        step = 5;
        scanf("%d", &n);
    
        while(n >= step) {
            sum += n/step;
            step *= 5;
        }
        printf("%d\n", sum);
    }
    return 0;
}

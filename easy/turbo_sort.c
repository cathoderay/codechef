/*
 Problem: Turbo Sort
 URL: http://www.codechef.com/problems/TSORT
 
 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com
*/


#include<stdio.h>
#define MAX 1000001

unsigned int v[MAX];

int main() {
    unsigned int i, j, n;

    for(i = 0; i < MAX; i++) {
        v[i] = 0;
    }

    scanf("%d", &n);
    for(i = 0; i < n; i++) {
        scanf("%d", &j);
        v[j] += 1;
    }

    for(i = 0; i < MAX; i++) {
        if (v[i] != 0) {
            for(j = 0; j < v[i]; j++) {
                printf("%d\n", i);
                n--;
            }
        }
        if (n == 0)
           break;
    }
    return 0;
}

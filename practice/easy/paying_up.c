/*
 Problem: Paying up
 URL: http://www.codechef.com/problems/MARCHA1
 
 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com

 Observation: this approach is ingenuous, but solved the
 problem in the time limit stipulated by codechef. 
 Run in 1.61s.
*/


#include<stdio.h>

int v[20];

int sum(int q) {
    int r;
    int i = 0;
    int s = 0;
    
    while(q > 0) {
        r = q % 2;
        q = q >> 1;
        if (r == 1) 
            s += v[i];
        i++;
    }
    return s;
}

int main() {

    int t, n, m, f, i, max;
    scanf("%d", &t);

    while(t--) {
        scanf("%d %d", &n, &m);

        for(i = 0; i < n; i++) 
            scanf("%d", &v[i]);

        f = 0;
        max = 1 << n;
        for(i = 0; i < max; i++) {
            if (sum(i) == m) {
                printf("Yes\n");
                f = 1;
                break;
            }
        }
        if (f == 0) printf("No\n");
    }

    return 0;
} 

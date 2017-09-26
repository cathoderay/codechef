/*
 Problem: Rescue
 URL: http://www.codechef.com/problems/DCE04

 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com

 Observation: This is the most ingenuous approach that
 solves the problem in the time limit described.
*/

#include<stdio.h>

int main() {
    int i, t, ca, m, w, ch; 
    
    scanf("%d", &t);
    for(i = 0; i < t; i++) {
        int s = 0; int sm = 0; int sw = 0; int sch = 0;
        scanf("%d %d %d %d", &ca, &m, &w, &ch);
        while(s < ca) {
            if (ch > 0 && (sm + sw) >= (sch + 1)/4.0) {
                ch--;
                sch++;
                s++;
            } else if (w > 0 && sm >= (sw + 1)/2.0) {
                w--;
                sw++;
                s++;
            } else if (m > 0) {
                m--;
                sm++;
                s++;
            } else break;
        }
        printf("%d %d %d\n", sm, sw, sch);
    }
    return 0;
}

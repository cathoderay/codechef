/*
 Problem: Yet Another Number Game
 URL: http://www.codechef.com/problems/NUMGAME
 
 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com
*/


#include<stdio.h>

int main() {
    int i, n, t;

    scanf("%d", &t);
    for(i = 0; i < t; i++){
        scanf("%d", &n);
        if (n % 2 == 0)
            printf("ALICE\n");
        else
            printf("BOB\n");
    }
    return 0;    
}

/*
 Problem: ATM
 URL: http://www.codechef.com/problems/HS08TEST

 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com
*/


#include<stdio.h>

int main() {
    float balance;
    int withdraw;

    scanf("%d %f", &withdraw,  &balance);
    if(withdraw % 5 == 0 && withdraw <= (balance - 0.50) ) {
        balance = balance - withdraw - 0.50;
    }
    printf("%.2f", balance);
    
    return 0;
}

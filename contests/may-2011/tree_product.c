/*
 Problem: Tree product
 URL: http://codechef.com/MAY11/problems/TPRODUCT

 Author: Ronald Kaiser

 Observation: this is a first approach. It was giving Wrong Answer
 because I had to deal with bignums.
 As I didn't want to implement such functions, I reimplemented the
 same idea in Python -- because bignums are builtins.
*/

#include<stdio.h>

#define MAX 65536
#define MODULO 1000000007

long long int v[MAX];
int current_max;
int current_height;
long long int p[MAX];

long long int dfs(int pos) {
    long long int l, r;

    if (pos >= (1 << (current_height - 1))) {
        return v[pos];
    } 

    if (p[2*pos] != -1) 
        l = p[2*pos];
    else 
        l = dfs(2*pos);

    if(p[2*pos + 1] != -1) 
        r = p[2*pos + 1];
    else
        r = dfs(2*pos + 1);

    l = v[pos]*l;
    r = v[pos]*r;
    return l > r ? l : r;
}



int main() {
    int h, max, i;

    scanf("%d", &h);
    while(h) {
        current_height = h;
        current_max = (1 << h) - 1;
        for(i = 1; i <= current_max; i++) {
            scanf("%lld", &v[i]);
        }
        for(i = 1; i <= MAX; i++)
            p[i] = -1;
        printf("%lld\n", dfs(1));
    
        scanf("%d", &h);
    }

    return 0;
}

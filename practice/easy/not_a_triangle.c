/*
 Problem: Not a Triangle
 URL: http://www.codechef.com/problems/NOTATRI

 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com

 Observation: implemented a binary search for first element greater than X
 Complexity: O(n^2*log(n))
 
*/

#include<stdio.h>

#define MAX 2001

int v[MAX];

int compare (const void * a, const void * b) {
      return (*(int*)a - *(int*)b);
}

int find_first_greater(int x, int start, int end) {
    int m;
    if (start > end)
        return -1;
    m = start + (end - start)/2;
    if (v[m] > x) {        
        if (m == 0)
            return 0;
        if (v[m - 1] > x)
            return find_first_greater(x, start, m - 1);
        else
            return m;
    }
    else 
        return find_first_greater(x, m + 1, end);
}

int main() {
    int i, j, n, sum, start, end, x, pos;

    scanf("%d", &n);
    while(n != 0){
        for(i = 0; i < n; i++) {
            scanf("%d", &v[i]);
        }
        sum = 0;
        qsort(v, n, sizeof(int), compare);

        for(i = 0; i <= n -2; i++) {
            for(j = i + 1; j <= n - 1; j++) {
                start = j;
                end = n - 1;
                x = v[i] + v[j];
                pos = find_first_greater(x, start, end);
                if (pos != -1)
                    sum += n - pos;
            }
        }
        printf("%d\n", sum);
        scanf("%d", &n);
    }
}

/*
 Problem: Distribute idlis Equally
 URL: http://www.codechef.com/problems/EQIDLIS

 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com
*/


#include<stdio.h>
#include<math.h>

#define MAX 3002
#define INFINITUM 1000000000

int main() {
    int n, t, i, j, e, sum, max, max_pos, min, min_pos, steps, r;
    int list[MAX];

    scanf("%d", &t);

    for(i = 0; i < t; i++) {
        scanf("%d", &n);
        sum = 0;
        for(j = 0; j < n; j++) {
            scanf("%d", &list[j]);
            sum += list[j];
        }
        if (sum % n != 0) {
            printf("-1\n");
        } else {
            steps = 0;
            min = -1;
            max = 1;
            while (1) {
                min = INFINITUM;
                min_pos = -1;
                max = -INFINITUM;
                max_pos = -1;
                for(j = 0; j < n; j++) {
                    if (list[j] < min) {
                        min = list[j]; 
                        min_pos = j;
                    }
                    if (list[j] > max) {
                        max = list[j];
                        max_pos = j;
                    }
                }
                if (min == max)
                    break;
                r = ceil((list[max_pos] - list[min_pos])/2.0);
                list[max_pos] -= r;
                list[min_pos] += r;
                steps++;
            }
            printf("%d\n", steps);
        }
    }

    return 0;
}

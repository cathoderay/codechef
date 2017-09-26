/*
 Problem: Count palindromes
 URL: http://www.codechef.com/problems/COUNTPAL
 
 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com
*/


#include<stdio.h>
#include<string.h>

#define MAX 1002

int p[MAX][MAX] = {{0}};
long int m[MAX] = {0};

int main() {
    char word[MAX];
    int start, end, len, i, j;
    gets(word);
    len = strlen(word);

    for(start = len-1; start >= 0; start--) {
        for(end = start; end < len; end++) {
            if (start == end || (word[start] == word[end] && end - start == 1))
                p[start][end] = 1;
            else if (word[start] == word[end] && end - 1 >= 0 && start + 1 <=end) 
		p[start][end] = p[start+1][end-1];
        }
    }
    m[0] = 1;
    for(end = 1; end < len; end++) {
        for(start = 0; start <= end; start++) {
	   if (p[start][end] == 1) {
               if (start == 0 || start == 1)
	          m[end] = (m[end] + 1) % 1000000007;
               else
                  m[end] = (m[end] + m[start-1]) % 1000000007;
	   }
        }
    }
    printf("%ld\n", m[len-1]);
    return 0;
}


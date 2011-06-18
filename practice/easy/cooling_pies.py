"""
 Problem: Cooling Pies
 URL: http://www.codechef.com/problems/COOLING

 Observation: Greedy approach.
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    pw = [int(i) for i in raw_input().split()]
    rw = [int(i) for i in raw_input().split()]

    pw.sort()
    rw.sort()

    ptr_pw = len(pw) - 1
    ptr_rw = len(rw) - 1
    sol = 0  
    while(ptr_pw >=0 and ptr_rw >= 0):
        if pw[ptr_pw] <= rw[ptr_rw]:
	    sol += 1
            ptr_rw -= 1
        ptr_pw -= 1
    print sol 

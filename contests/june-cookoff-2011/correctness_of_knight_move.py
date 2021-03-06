"""
 Problem: Correctness of Knight Move
 URL: http://www.codechef.com/problems/KNIGHTMV
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


n = int(raw_input())
cells = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
cells_keys = cells.keys()
for i in range(n):
    move = raw_input()
    try:
        int(move[1])
	int(move[4])
    except:
        print "Error"
	continue
    if (len(move) == 5 and move[0] in cells_keys and 
       int(move[1]) in range(1, 9) and move[2] == '-' and 
       move[3] in cells.keys() and int(move[4]) in range(1,9)):
	move = list(move)
        move[0] = cells[move[0]]
        move[3] = cells[move[3]]
        source = [int(i) for i in move[:2]]
        destiny = [int(i) for i in move[3:5]]
        if ((abs(destiny[0] - source[0]) == 2 and abs(destiny[1] - source[1]) == 1) or
            (abs(destiny[0] - source[0]) == 1 and abs(destiny[1] - source[1]) == 2)):
	   print "Yes"
        else:
           print "No"
    else: 
        print "Error"


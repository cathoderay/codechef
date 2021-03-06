"""
 Problem: Correctness of Knight Move
 URL: http://www.codechef.com/problems/KNIGHTMV
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


n = int(raw_input())
cells = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
cells_keys = cells.keys()
str_num = [str(i) for i in range(1, 9)]
for i in range(n):
    move = raw_input()
    if (len(move) == 5):
        if (not move[1] in str_num) or (not move[4] in str_num):
            print "Error"
            continue
        if (move[0] in cells_keys and move[2] == '-' and move[3] in cells_keys):
            move = list(move)
            move[0] = cells[move[0]]
            move[1] = int(move[1])
            move[3] = cells[move[3]]
            move[4] = int(move[4])
            if ((abs(move[3] - move[0]) == 2 and abs(move[4] - move[1]) == 1) or
                (abs(move[3] - move[0]) == 1 and abs(move[4] - move[1]) == 2)):
	        print "Yes"
            else:
                print "No"
        else:
            print  "Error"
    else: 
        print "Error"


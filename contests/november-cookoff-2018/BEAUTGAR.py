"""
  Url: https://www.codechef.com/COOK100B/problems/BEAUTGAR/
  Beautiful Garland Problem Code: BEAUTGAR

  All submissions for this problem are available.###Read problems statements in Hindi, Mandarin Chinese, Russian, Vietnamese and Bengali as well.

  There is a garland — a cyclic rope with red and green flowers on it in some order. The sequence of flower colours is described by a string s

  ; since the rope is cyclic, each two consecutive flowers are adjacent and the first and last flower are also adjacent.

  The garland is beautiful if there is no pair of adjacent flowers with identical colours.

  You want the garland to be beautiful. To achieve that, you may perform the following operation at most once:

    Make two cuts on the rope (not intersecting the flowers), splitting the garland into two parts.
    Reverse one of these two parts.
    Tie together corresponding endpoints of the two parts, creating one whole garland again.

  Can you find out whether it is possible to make the garland beautiful?
  Input

    The first line of the input contains a single integer T 
  denoting the number of test cases. The description of T
  test cases follows.
  The first and only line of each test case contains a single string s
  describing the garland. Each character of s is either 'R' or 'G', denoting a red or green flower respectively.

  Output

  For each test case, print a single line containing the string "yes" if the garland can be made beautiful or "no" otherwise.
  Constraints

    1≤T≤105

  2≤|s|≤105
  the sum of |s|
  over all test cases does not exceed 106

  Example Input

  3
  RG
  RRGG
  RR

  Example Output

  yes
  yes
  no

  Explanation

  Example case 1: The garland is already beautiful.

  Example case 2: We can cut the garland between flowers 1 and 2 and between flowers 3 and 4. After reversing the part containing flowers 2 and 3 and rejoining, we obtain "RGRG".
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    s = input()
   
    if len(s) % 2 != 0:
        print('no')
    elif s.count('R') != len(s)/2:
        print('no')
    else:
        rr = 0 
        gg = 0
        s = s + s[0]
        last = 0
        for cur in s:
            if rr > 1 or gg > 1:
                print('no')
                break
            if cur == last:
                if cur == 'R':
                    rr += 1
                if cur == 'G':
                    gg += 1
            last = cur
        if rr == gg and (rr == 1 or rr == 0):
            print('yes')

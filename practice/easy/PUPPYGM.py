"""
  Url: https://www.codechef.com/problems/PUPPYGM
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

"""
Key idea:
    - use a recursive approach like the following,
      so you can have an intuition of the solution;
    - print the solution and see the pattern;
    - you can try to prove it by induction.

def play(a, b):
    if a <= 1 and b <= 1:
        return False

    if (a == 1 and b == 2) or \
       (b == 1 and a == 2):
        return True

    for i in range(1, b//2+1):
        if not play(b-i, i):
            return True

    for i in range(1, a//2+1):
        if not play(a-i, i):
            return True
    return False

for i in range(1, 30):
    for j in range(1, 30):
        print(1 if play(i, j) else 0, end="")
    print('\n')
"""


for _ in range(int(input())):
    A, B = list(map(int, input().split()))
    print("Tuzik" if A % 2 == 0 or B % 2 == 0 else "Vanka")

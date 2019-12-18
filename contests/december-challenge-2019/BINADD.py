"""
  Url: https://www.codechef.com/problems/BINADD
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from sys import stdin, stdout


rline = lambda: stdin.readline().strip()


def solve():
    global A, B

    if not '1' in B: return 0

    diff = len(A) - len(B)

    if diff > 0: 
        B = '0' * diff + B
    else: 
        A = '0' * (-diff) + A

    s = 1
    for i in range(len(A) - 1, -1, -1):
        if A[i] == B[i] == '1':
            j = i - 1
            while (j >= 0 and A[j] != B[j]):
                j -= 1
            s = max(s, (i - j + 1))
    return s


def read_input():
    global A, B
    A, B = '0' + rline(), '0' + rline()


def write_output(s):
    stdout.write('\n'.join(map(str, s)))
    

def main():
    s = []
    for _ in range(int(input())):
        read_input()
        answer = solve()
        s.append(answer)
    write_output(s)
    

main()

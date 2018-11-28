"""

"""


for _ in range(int(input())):
    N, X = list(map(int, input().split()))

    ns = list(map(int, input().split()))

    SUM = sum(ns) 
    if SUM % X >= min(ns):
        print(-1)
    else:
        print(SUM//X)



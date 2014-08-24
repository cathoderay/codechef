for t in range(int(raw_input())):
    n, x = map(int, raw_input().split())
    v = map(int, raw_input().split())
    s = sum(v)
    if s % x >= min(v):
        print -1
    else:
        print s // x

t = int(raw_input())
for i in range(t):
    n = int(raw_input()) #wont use, consuming input
    h = map(int, raw_input().split())

    h.sort()

    last = 0
    diff = 1000000000
    for j in h:
        if last == 0:
            last = j 
        elif diff > (j - last):
            diff = j - last
        last = j
    print(diff)
            

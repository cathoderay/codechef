t = int(raw_input())
for i in range(t):
    n = int(raw_input()) #wont use, just consuming input
    c = map(int, raw_input().split())

    acc = 0
    speed = 0
    for j in c:
        if speed == 0:
            speed = j
            acc += 1    
        elif speed >= j:
            speed = j
            acc += 1
    print(acc)

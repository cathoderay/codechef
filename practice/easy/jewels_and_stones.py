
for t in range(int(raw_input())):
    j = raw_input() 
    s = raw_input() 
    inter = set(s).intersection(set(j))
    c = 0
    for i in s:
        if i in inter:
            c += 1
    print c

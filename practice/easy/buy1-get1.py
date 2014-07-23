import math

n = int(raw_input())
for i in range(n):
    s = filter(str.isalpha, raw_input())
    d = {}
    for l in s:
        if l not in d:
            d.update({l: 1})
        else:
            d[l] += 1
    acc = 0
    for l in d:
       acc += int(math.ceil(d[l]/2.0))
    print(acc)


def distance(a, b):
    return (a[0] - b[0])**2 + (b[1] - a[1])**2

def read_point():
    return map(int, raw_input().split())

n = int(raw_input())
for i in range(n):
    r = int(raw_input())
    p1 = read_point() 
    p2 = read_point() 
    p3 = read_point()

    r2 = r*r
    outs = filter(lambda p: p > r2, 
                 [distance(p1, p2), 
                  distance(p1, p3), 
                  distance(p2, p3)])

    if len(outs) > 1:
        print("no")
    else:
        print("yes")
    

t = int(raw_input())
for i in range(t):
    n, c = map(int, raw_input().split())
    if sum(map(int, raw_input().split())) <= c:
        print("Yes")
        continue
    print("No")

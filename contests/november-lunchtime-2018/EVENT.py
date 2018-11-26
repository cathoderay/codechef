"""
    Url: https://www.codechef.com/LTIME66B/problems/EVENT
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    start, end, l, r = input().split()
    l = int(l)
    r = int(r)

    count = 1
    cur_day = start
    next_day = {"sunday": "monday", 
                "monday": "tuesday",
                "tuesday": "wednesday",
                "wednesday": "thursday",
                "thursday": "friday",
                "friday": "saturday",
                "saturday": "sunday"}

    while cur_day != end:
        count += 1
        cur_day = next_day[cur_day]

    potential_days = set(range(count, 101, 7))
    possible_days = set(range(l, r + 1, 1))
    s = potential_days.intersection(possible_days)

    if len(s) == 1:
        print(s.pop())
    elif len(s) > 1:
        print("many")
    else:
        print("impossible")

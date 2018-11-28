"""
  Url: https://www.codechef.com/problems/ERROR/
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    s = input()
    if ("101" in s) or ("010" in s):
        print("Good")
    else:
        print("Bad") 

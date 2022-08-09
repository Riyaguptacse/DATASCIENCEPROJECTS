import re

N= int(input())
con = False
for i in range(N):
    s = input()
    if '{' in s:
        con = True
    elif '}' in s:
        con = False
    elif con:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)
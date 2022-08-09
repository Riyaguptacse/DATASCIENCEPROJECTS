import re

Str, k = input(), input()
matches = re.finditer(r'(?=(' + k + '))', Str)

firstmatch = False
for match in matches:
    firstmatch = True
    print((match.start(1), match.end(1) - 1))

if firstmatch == False:
    print((-1, -1))
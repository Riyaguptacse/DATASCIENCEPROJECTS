import re

exp=r"([a-zA-Z0-9])\1+"

m = re.search(exp,input())

if m:
    print(m.group(1))
else:
    print(-1)
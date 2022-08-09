import re

for i in range(int(input())):
    pattern = r"[456]\d{3}(-?\d{4}){3}$"
    n = input()
    if bool(re.match(pattern, n)) is True:
        if bool(re.search(r"([\d])\1\1\1", n.replace("-", ""))) is False:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
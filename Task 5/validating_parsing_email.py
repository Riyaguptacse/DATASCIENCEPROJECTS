
import re

string = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'
for i  in range(int(input())):
    name, email = input().split(' ')
    if re.match(string, email):
        print(name, email)
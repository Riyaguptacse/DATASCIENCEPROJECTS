from re import compile

number = compile('^[-+]?[0-9]*\.[0-9]+$')
for i in range(int(input())):
    print(bool(number.match(input())))
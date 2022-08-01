def swap_case(s):
    num = ""
    for char in s:
        if char.isupper() == True:
            num+=(char.lower())
        else:
            num+=(char.upper())
    return num

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
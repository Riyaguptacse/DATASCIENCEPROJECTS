if __name__ == '__main__':
    str1= input()
    print(any(c.isalnum() for c in str1))
    print(any(c.isalpha() for c in str1))
    print(any(c.isdigit() for c in str1))
    print(any(c.islower() for c in str1))
    print(any(c.isupper() for c in str1))
def print_formatted(number):
    l = len(bin(number)[2:])
   
    for i in range(1,number+1):
        print(str(i).rjust(l,' '),end=" ")
        print(oct(i)[2:].rjust(l,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l,' '),end=" ")
        print(bin(i)[2:].rjust(l,' '),end=" ")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
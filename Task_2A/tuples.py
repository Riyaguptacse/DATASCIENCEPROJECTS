if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tup = ()
    for x in integer_list:
        tup+=(x,)
    
    print(hash(tup))

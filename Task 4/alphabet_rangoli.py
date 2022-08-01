def print_rangoli(size):
    w  = size*4-3
    s = ''

    for i in range(1,size+1):
        for j in range(0,i):
            s+= chr(96+size-j)
            if len(s) < w :
                s += '-'
        for k in range(i-1,0,-1):    
            s += chr(97+size-k)
            if len(s) < w :
                s += '-'
        print(s.center(w,'-'))
        s= ''

    for i in range(size-1,0,-1):
        s = ''
        for j in range(0,i):
            s += chr(96+size-j)
            if len(s) < w :
                s += '-'
        for k in range(i-1,0,-1):
            s += chr(97+size-k)
            if len(s) < w :
                s += '-'
        print(s.center(w,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
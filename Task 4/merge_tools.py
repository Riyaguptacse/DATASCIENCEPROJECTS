def merge_the_tools(string, k):
    temp = []
    l_temp = 0
    for items in string:
        l_temp += 1
        if items not in temp:
            temp.append(items)
        if l_temp == k:
            print (''.join(temp))
            temp = []
            l_temp = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
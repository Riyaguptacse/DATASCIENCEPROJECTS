if __name__ == '__main__':
    N = int(input())
    Output = [];
    for i in range(0,N):
        arr= input().split();
        if arr[0] == "print":
            print(Output)
        elif arr[0] == "insert":
            Output.insert(int(arr[1]),int(arr[2]))
        elif arr[0] == "remove":
            Output.remove(int(arr[1]))
        elif arr[0] == "pop":
            Output.pop();
        elif arr[0] == "append":
            Output.append(int(arr[1]))
        elif arr[0] == "sort":
            Output.sort();
        else:
            Output.reverse();

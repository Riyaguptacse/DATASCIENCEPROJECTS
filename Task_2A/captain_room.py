N = int(input())
arr = map(int, input().split())
array= sorted(array)

for i in range(len(array)):
    if(i != len(array)-1):
        if(array[i]!=array[i-1] and array[i]!=array[i+1]):
            print(array[i])
            break;
    else:
        print(arrar[i])
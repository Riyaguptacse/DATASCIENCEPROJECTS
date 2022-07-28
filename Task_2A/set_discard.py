n = int(input())
s = set(map(int, input().split()))
num = int(input())
for i in range(num):
    arr = input().split()
    if arr[0]=="remove":
        s.remove(int(arr[1]))
    elif arr[0]=="discard":
        s.discard(int(arr[1]))
    else :
        s.pop()
print(sum(list(s)))
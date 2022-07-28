A = int(input())
a = set(map(int,input().split()))
N = int(input())
for i in range(N):
    arr = input().split()
    output = arr[0]
    s = set(map(int,input().split()))
    if (output == 'update'):
        a |= s
    elif (output == 'intersection_update'):
        a &= s
    elif (output == 'difference_update'):
        a -= s
    elif (output == 'symmetric_difference_update'):
        a ^= s
print(sum(a))

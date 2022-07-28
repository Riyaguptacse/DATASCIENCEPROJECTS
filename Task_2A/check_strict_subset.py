arr = set(input().split())
N = int(input())
output = True

for i in range(N):
    arr2 = set(input().split())
    if not arr2.issubset(arr):
        output = False
    if len(arr2) >= len(arr):
        output = False

print(output)
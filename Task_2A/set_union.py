M= int(input())
m = list(input().split())
N= int(input())
n = list(input().split())

s1 = set(m)
s2 = set(n)

print(len(s1.union(s2)))
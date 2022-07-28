n,m = input().split() 
happiness = 0 
array = input().split() 
set_a = set(input().split())
set_b =set(input().split())
for i in array:
    if i in set_a and i not in set_b:
         happiness += 1 
    if i in set_b and i not in set_a: 
        happiness -= 1
print(happiness)
import math
s = 0.12
a = 0
for i in range(0, 3):
    a+= math.factorial(10)/math.factorial(i)/math.factorial(10-i) * s**i * (1-s)**(10-i)
    if i == 1:
        b = 1 - a

print(round(a, 3))
print(round(b, 3))
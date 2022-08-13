mean = 500
std = 80
n = 100
z = 1.96

mean = mean
std = std / n**(1/2)

print(round(mean - std * z, 2))
print(round(mean + std * z, 2))
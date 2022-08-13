import math
mean, std = 70, 10
dev= lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(round((1-dev(80))*100,2))
print(round((1-dev(60))*100,2))
print(round((dev(60))*100,2))

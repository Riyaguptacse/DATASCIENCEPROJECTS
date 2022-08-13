import math
def dev(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))
mean = 20
std = 2
print(round(dev(19.5, mean, std), 3))
print(round(dev(22, mean, std) - dev(20, mean, std), 3))
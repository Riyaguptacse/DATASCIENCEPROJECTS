import math
def clt(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))
mean = 205
std = 15
n = 49
target = 9800
mean_sum = n * mean
std_sum = std * n**(1/2)
print(round(clt(target, mean_sum, std_sum), 4))
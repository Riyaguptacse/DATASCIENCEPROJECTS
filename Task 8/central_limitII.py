import math
def clt(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))

mean = 2.4
std = 2
n = 100
target = 250

mean_sum = n * mean
std_sum = std * n**(1/2)

# Find the probability that sum <= 250
print(round(clt(target, mean_sum, std_sum), 4))
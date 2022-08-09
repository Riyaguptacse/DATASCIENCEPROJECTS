import numpy as np
N,M = map(int,input(). split())
array = []
for i in range(N):
    row = list(map(int,input(). split()))
    array. append(row)
    np_ar = np. array(array)
print(np. transpose(np_ar))
print(np_ar.flatten())
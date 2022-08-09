import numpy as np
N= int(input())
A = np.array([input().split() for i in range(N)], int)
B = np.array([input().split() for i in range(N)], int)
print(np.dot(a, b))
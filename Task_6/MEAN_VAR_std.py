
import numpy as np
N, M = list(map(int, input().split()))
a = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.mean(a, axis=1))
print(np.var(a, axis=0))
print(round(np.std(a, axis=None), 11))



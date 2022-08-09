import numpy

l = [float(x) for x in input().split()]
x = float(input())

print(numpy.polyval(l,x))
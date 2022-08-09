import numpy
numpy.set_printoptions(legacy='1.13')

array = numpy.array(input().split(),float)

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))

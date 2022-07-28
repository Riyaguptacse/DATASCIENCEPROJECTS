from __future__ import division

def average(array):
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array/len_array
    return output

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result

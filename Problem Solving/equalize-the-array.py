#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    deletions = 0
    counters = []
    filtered_data = list(set(arr))
    arr.sort()

    for num in filtered_data:
        counters.append(arr.count(num))

    max_value = max(counters)
    max_index = counters.index(max_value)
    max_num = filtered_data[max_index]

    for num in arr:
        if num != max_num:
            deletions += 1
            
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

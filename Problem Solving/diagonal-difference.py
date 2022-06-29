#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    diag_left_right = 0
    diag_right_left = 0
    
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if i == j: diag_left_right += arr[i][j]
            if i+j==len(arr)-1: diag_right_left += arr[i][j]
            
    return abs(diag_left_right - diag_right_left)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

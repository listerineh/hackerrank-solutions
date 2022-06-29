#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    first_0 = c.index(0)
    last_0  = first_0

    current_0 = first_0
    steps = 0

    for i in range(first_0+1, len(c)):
        if c[i] == 0: last_0 = i

    while current_0 < len(c) - 2:
        if c[current_0 + 2] == 0:
            current_0 += 2
            steps += 1
        elif c[current_0 + 1] == 0:
            current_0 += 1
            steps += 1

    if current_0 != last_0:
        val = last_0 - current_0
        
        if c[current_0 + val] == 0:
            current_0 += val
            steps += 1
            
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    total = len(arr)
    
    positives = 0
    negatives = 0
    zeros = 0
    
    for num in arr:
        if num > 0: positives += 1
        elif num < 0: negatives += 1
        else: zeros += 1
        
    print("{:.6f}".format(positives/total))
    print("{:.6f}".format(negatives/total))
    print("{:.6f}".format(zeros/total))
    

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)

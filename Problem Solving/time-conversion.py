#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s[:-2]
    val = s[-2:]
    
    hours, minutes, seconds = time.split(':')
    
    if val == 'PM': 
        if hours != '12': hours = int(hours) + 12
    else:
        if hours == '12': hours = '00'
        
    return f"{hours}:{minutes}:{seconds}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()

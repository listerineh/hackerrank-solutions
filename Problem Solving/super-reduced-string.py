#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def validate(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]: return False

    return True

def superReducedString(s):
    while True:
        to_delete = []

        for i in range(len(s)-1):
            if s[i] == s[i+1] and not i in to_delete: 
                to_delete.append(i)
                to_delete.append(i+1)

        to_delete.sort(reverse=True)
        for k in to_delete: s = s[:k] + s[k+1:]

        if validate(s): break
    
    return s if s != '' else 'Empty String'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = superReducedString(s)
    fptr.write(result + '\n')
    fptr.close()

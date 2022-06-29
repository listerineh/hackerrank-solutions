#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(n-1, -1, -1):
        for k in range(n):
            if k >= i: print('#',end='')
            else: print(' ',end='')
        print()

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)

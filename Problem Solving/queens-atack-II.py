#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#
def queensAttack(n, k, r_q, c_q, obstacles):
    attacked_squares = 0

    directions = [[1,1],[1,0],[0,1],[-1,-1],[-1,0],[0,-1],[-1,1],[1,-1]]
    obs_set = {}

    if(obstacles): 
        for obstacle in obstacles:
            obs_set[obstacle[0],obstacle[1]] = 1

    for move in directions:
        i, j = r_q, c_q
        i += move[0]
        j += move[1]
        while(i<=n and j<=n and i>0 and j>0):
            if (i,j) in obs_set: break
            else:
                attacked_squares += 1
            i += move[0]
            j += move[1]

    return attacked_squares

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')
    fptr.close()

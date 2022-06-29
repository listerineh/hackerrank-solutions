#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grades = []

    for grade in grades:
        if grade < 40:
            if grade >= 38: final_grades.append(40)
            else: final_grades.append(grade)
        else:
            val = True
            for aux in range(grade, grade+3):
                if aux % 5 == 0: 
                    final_grades.append(aux)
                    val = False
                    break
            if val: final_grades.append(grade)
            
    return final_grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

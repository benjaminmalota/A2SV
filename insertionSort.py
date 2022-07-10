#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    ar = [2,4,6,8,3]
    current = ar[-1]
    n = len(ar) - 1
    for i in (range(4,0,-1)):
    
        if current < ar[i - 1]:
            ar[i] = ar[i -1]
            print(*ar)
        else:
            ar[i] = current
            print(*ar)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

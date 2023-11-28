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
    j=n-2
    hold=arr[-1]
    while j>=0:
        if hold<arr[j]:
            arr[j+1]=arr[j]
        else:
            arr[j+1]=hold
            break
        print(*arr)
        j-=1
    if hold<arr[0]:
        arr[0]=hold
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

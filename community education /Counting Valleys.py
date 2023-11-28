import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    # Write your code here
    valleys=0
    lst=[]
    n=0
    for i in range (steps):
        if path[i]=="D":
            n-=1
        elif path[i]=="U":
            n+=1
        lst.append(n)
    for j in range(steps):
        if lst[j]==0 and lst[j-1]<0:
            valleys+=1     
    return valleys 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

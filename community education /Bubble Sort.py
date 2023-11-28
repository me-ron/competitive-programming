import math
import os
import random
import re
import sys


def countSwaps(a):
    # Write your code here
    numSwaps=0
    for i in range (len(a)):
        for j in range (i+1,len(a)):
            if a[j]<a[i]:
                numSwaps+=1
                a[i],a[j]=a[j],a[i]
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

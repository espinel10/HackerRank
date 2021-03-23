#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the andProduct function below.
def msbPos(n):
    msb_p=-1
    while(n):
        n=n>>1
        msb_p=msb_p+1
    return msb_p




def andProduct(a, b):
    x=a
    y=b
    acum=0
    while(x&y):
        i=msbPos(x)
        j=msbPos(y)
        if i==j:
            acum=acum+2**j
            x=x-2**j
            y=y-2**j
        else:
            break
    return acum
   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()


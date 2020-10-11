
import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    stick=sticks
    stick.sort()
    stick.reverse()
    salida=None
    per=-999999
    N=len(stick)
    band=0
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            for z in range(j+1,N):
                if ((stick[j]+stick[z])>stick[i]):
                    salida=[stick[z],stick[j],stick[i]]
                    band=1
                    break
            if band==1:
                break
        if band==1:
                break

    if salida==None:
        return [-1]
    else:
        return salida


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

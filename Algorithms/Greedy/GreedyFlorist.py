#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c ,n):
    pass
    acum=0
    f=[0 for i in range(k)]
    orden=c[:]
    orden.sort(reverse=True)
  
    while n!=0 and len(orden)>0:
        for i in range(0,len(f)):
            if n==0 or len(orden)==0:
                break
            else:
                acum=acum+(f[i] + 1)*orden[0]
                f[i]=f[i]+1
                n=n-1
                orden.remove(orden[0]) 

    return acum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c,n)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()

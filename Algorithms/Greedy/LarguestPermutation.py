#!/bin/python3

#URL:  https://www.hackerrank.com/challenges/largest-permutation/problem

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    n=len(arr)
    entrada=arr[:]
    N=n
    indices=range(0,n)
    datos=dict(zip(arr,indices))
    j=k
    if k>n:
      j=n
    i=0
    while k!=0 and i<n:
      if entrada[i]==N:
        i=i+1
        N=N-1
      else:
        tmp=entrada[i]
        entrada[i]=N
        entrada[datos[N]]=tmp
        datos[tmp]=datos[N]
        datos[N]=i
        i=i+1
        N=N-1
        k=k-1      
    return entrada    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

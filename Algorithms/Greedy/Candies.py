
import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    if n==1:
        return 1
    if n==2:
        return 3
    entrada=arr
    N=n
    if entrada[-1]==min(entrada):
        entrada.reverse()

    aux=[1 for i in range(N)]
    for i in range(0,N-1):
        if entrada[i]>entrada[i+1]:
            if i==0:
                aux[i]=aux[i+1]+1
                continue

            if entrada[i-1]>entrada[i]:
                aux[i]=aux[i+1]+1
                if aux[i-1]<=aux[i]:
                    j=i
                    while j>=1 and (aux[j-1]<=aux[j]) and (entrada[j-1]>entrada[j]):
                        aux[j-1]=aux[j]+1
                        j=j-1
            else:
                if aux[i-1]>=aux[i]:
                    aux[i]=min(aux[i-1],aux[i+1])+1
        else:
            if entrada[i]!=entrada[i+1]:
                aux[i+1]=aux[i]+1

    return sum(aux)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

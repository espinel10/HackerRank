###URL https://www.hackerrank.com/challenges/new-year-chaos/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    cont=0
    entrada=q
    N=len(entrada)
    band=0
    colocts=[i+1 for i in range(0,N)]
    while len(colocts)>0:
        indice=entrada.index(colocts[-1])
        dif=colocts[-1]-(indice+1)
        if dif<=2:
            if dif==2:
                cont=cont+2
                temp=entrada[indice+1]
                entrada[indice+1]=entrada[indice]
                entrada[indice]=temp
                temp=entrada[indice+2]
                entrada[indice+2]=entrada[indice+1]
                entrada[indice+1]=temp
            if dif==1:
                cont=cont+1
                temp=entrada[indice+1]
                entrada[indice+1]=entrada[indice]
                entrada[indice]=temp
            colocts.pop()      
        else:
            band=1
            break


    if band==1:
        return "Too chaotic"      
    else:
        return cont


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        result=minimumBribes(q)
        fptr.write(str(result) + '\n')

    fptr.close()

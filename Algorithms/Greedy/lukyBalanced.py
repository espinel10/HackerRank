#URL https://www.hackerrank.com/challenges/luck-balance/problem
import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    pass
    max=contests[0]
    for i in range(0,n):
        for j in range(i+1,n):
            if contests[i][0]<contests[j][0]:
                aux=contests[i]
                contests[i]=contests[j]
                contests[j]=aux
    acum=0      
    for i in contests:
        if i[1]==0:
            acum=acum+i[0]
        else:
            if k>0:
                acum=acum+i[0]
                k=k-1
            else:
                acum=acum-i[0]
                
    return acum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
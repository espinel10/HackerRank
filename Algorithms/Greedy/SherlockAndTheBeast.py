
import math
import os
import random
import re
import sys
def values(i,j):
    if i==0:
        return []
    res=[]
    for k in range(0,i):
        res.append(j)
    return res

# Complete the decentNumber function below.
def decentNumber(n):
    resp=[]
    if n%3==0:
        return int("".join(list(map(str,values(n,5)))))
    #if n%5==0:
    #    return int("".join(list(map(str,values(n,3)))))
    a=0
    b=0
    a=0
    b=0
    a=n//3
    N=n
    band=0
    while band==0:
        if(N-a*3)>0:
            a=a-1
            n=n-3*a
        if n%5==0:
            b=n//5
            band=1
        if a<0:
            return -1
        n=N

    resp+=values(a*3,5)
    resp+=values(b*5,3)
    return int("".join(list(map(str,resp))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = decentNumber(n)
        fptr.write(str(result) + '\n')

    fptr.close()

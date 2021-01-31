#URL: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    j=0
    abc="abcdefghijklmnopqrstuvwxyz"
    d=list(abc)
    i=range(0,len(d))
    dic1=dict(zip(d,i))
    j=j+k
    while j>len(d)-1:
        j=j-len(d)
    aux=[]
    entrada=list(s)
    while len(aux)<len(d):
        if j>len(d)-1:
            j=0
        aux.append(d[j])
        j=j+1
    salida=[]
    for z in entrada:
        if z in d:
            salida.append(aux[dic1[z]])
        else:
            if z.lower() in d:
                salida.append(aux[dic1[z.lower()]].upper())
            else:
                salida.append(z)
    return "".join(salida)            
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
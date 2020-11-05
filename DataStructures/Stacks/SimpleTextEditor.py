#URL https://www.hackerrank.com/challenges/simple-text-editor/problem

import math
import os
import random
import re
import sys
from collections import deque

def simpleText(S):
    salida=[]
    ult=""
    pri=""
    k=0
    pote=deque([])
    for i in S:
        aux=i.split()
        if aux[0]=="1":
            ult+=aux[1]
            pote.append(ult)
        if aux[0]=="2":
            auxi=list(ult)
            dif=len(auxi)-int(aux[1])
            if dif>-1:
                auxi=[auxi[j] for j in range(dif)]
                ult="".join(auxi)
            pote.append(ult)
        if aux[0]=="3":
            auxi=list(ult)
            salida.append(auxi[int(aux[1])-1])
        if aux[0]=="4":
            j=pote.pop()
            if len(pote)==0:
                j=pri
                ult=""
                pote.append(ult)
            else:
                ult=pote.pop()
                pote.append(ult)


        if k==0:
            pri+=ult
            k=1


    return salida





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    S=[]
    for t_itr in range(t):
        s = input()
        S.append(s)

    salida=simpleText(S)

    for i in salida:
        fptr.write(i + '\n')

    fptr.close()

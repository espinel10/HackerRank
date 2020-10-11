import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    E=w
    E.sort()
    salida=[]
    i=0
    j=0
    while len(E)>0:
        aux=[]
        cont=0
        j=E[0]+4
        for i in E:
            if i>j:
                break
            aux.append(i)
            cont=cont+1
        salida.append(aux)
        E=E[cont:]
    return len(salida)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()

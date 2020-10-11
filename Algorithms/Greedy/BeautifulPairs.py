import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    C=A
    N=len(B)
    respuesta=[]

    for i in range(0,N):
        if B[i] in A:
            j=A.index(B[i])
            respuesta.append((i,j))
            A[j]=-1

    if A.count(-1)==N:
        return len(respuesta)-1
    else:
        return len(respuesta)+1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()

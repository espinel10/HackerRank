###URL https://www.hackerrank.com/challenges/flipping-the-matrix/problem
import math
import os
import random
import re
import sys

# Complete the flippingMatrix function below.
def flippingMatrix(matrix,n):
    entrada=matrix
    N=2*n
    i=0
    j=N-1
    aux=[]
    while j>i:
        m=0
        n=N-1
        while m<n:
            aux.append(max(entrada[i][m],entrada[i][n],entrada[j][m],entrada[j][n]))
            m=m+1
            n=n-1
        i=i+1
        j=j-1
    return sum(aux)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix,n)

        fptr.write(str(result) + '\n')

    fptr.close()

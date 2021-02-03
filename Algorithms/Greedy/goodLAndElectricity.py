
# https://www.hackerrank.com/challenges/pylons/problem
import math
import os
import random
import re
import sys

# Complete the pylons function below.
def verificar(n,arr2,k):
    N=n
    prueba=[-1,-1]
    band=0
    for i in arr2:    
        L=k
        R=k
        if i-L+1<0:
            L=i+1
        if i+R>n:
            R=n-i
        if band==0:
            prueba=[i-L+1,i+R]
            band=1
            if (i-L+1)!=0:
              break
        else:
            if prueba[1]<i+R and (prueba[0]<=(i-L+1) and prueba[1]>=(i-L+1)):
                prueba[1]=i+R
            else:
                break
    if prueba[1]==N and prueba[0]==0:
        return 1 
    else:
        return 0
    
        
def pylons(k,arr):
  from collections import deque
  N=len(arr)
  indices=[]
  for i in range(0,N):
    if arr[i]==1:
      indices.append(i)
  band=verificar(N,indices,k)
  if band==1:
    intervalos=[]
    for i in indices:
      n=N
      L=k
      R=k
      if i-L+1<0:
        L=i+1
      if i+R>n:
        R=n-i
      if band==0:
        prueba=[i-L+1,i+R-1]
        band=1

      aux=[i-L+1,i+R-1]
      intervalos.append(aux)
    i=0
    salida=deque([])
    while intervalos[i][0]==0:
      i=i+1
    i=i-1
    salida.append(intervalos[i])
    may=intervalos[i][1]  
    while i<len(intervalos):
      saco=salida.pop()
      if saco[0]==0:
        salida.append(saco)
        i=i+1
        salida.append(intervalos[i])
        continue
      
      if intervalos[i][0]<=may+1:
        salida.append(intervalos[i])
      else:
        may=saco[1]
        salida.append(saco)
        salida.append(intervalos[i])
      if intervalos[i][1]==N:
        break
      i=i+1
    return len(salida)
  else:
    return -1  
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
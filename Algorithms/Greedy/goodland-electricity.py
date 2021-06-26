#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def verificar(intervals,nums):
    ab=[intervals[0][0],intervals[0][1]]
    band=True
    if ab[0]!=0:
        return False
    if ab[1]==nums:
        return True
    for i in range(1,len(intervals)):
        if intervals[i][0] <= ab[1]+1:
            ab[1]=intervals[i][1]
        else:
            band=False
            break
    if ab[1]!=nums:
        band=False
    return band

def devuelvo(ab,i,vals):
    ref=None
    while vals[i][0] <= ab+1:
        ref=vals[i][:]
        i=i+1
        if i==len(vals):
            break
    return i,ref

def inicio(intervals):
    ref=None
    i=0
    while intervals[i][0]==0:
        ref=intervals[i][:]
        i=i+1
        if i==len(intervals):
            break
    return i,ref



def pylons(k,arr):
    intervals=[]
    for i in range(0,len(arr)):
        if arr[i]==1:
            intervals.append([max(0,i-k+1),min(len(arr)-1,i+k-1)])

    band=verificar(intervals,len(arr)-1)
    if band:
        salida=[]
        i,ini=inicio(intervals)
        salida.append(ini)
        while i<len(intervals):
            i,ref=devuelvo(salida[-1][1],i,intervals)
            salida.append(ref)
        print(salida)
        return len(salida)
    else:
        return -1

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pylons(k, arr)
    print(result)

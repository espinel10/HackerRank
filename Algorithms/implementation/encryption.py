#!/bin/python3

import math
import os
import random
import re
import sys

# url: https://www.hackerrank.com/challenges/encryption/problem
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    L=len(s)
    s=list(s)
    w=math.sqrt(L)
    b=math.ceil(w)
    a=math.floor(w)
    if a*a>=L:
        a=a
        b=a
    elif a*b>=L:
        a=a
        b=b
    elif b*b>=L:
        a=b
        b=b
    men=["" for i in range(b)]
    for i in range(len(s)):
        men[i%b]=men[i%b]+s[i]

    return " ".join(men)
   
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

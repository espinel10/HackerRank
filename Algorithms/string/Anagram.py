#URL: https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    entrada=list(s)
    if len(entrada)%2!=0:
        return -1
    mit=int(len(entrada)/2)  
    a=entrada[:mit]
    b=entrada[mit:]
    cont=0
 
    for j in a:
        if j in b :
            cont=cont+1
            b.remove(j) 
    salida=len(a)-cont
    return salida

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
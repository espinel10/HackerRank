###URL https://www.hackerrank.com/challenges/tower-breakers-1/problem

import math
import os
import random
import re
import sys


# Complete the towerBreakers function below.
def towerBreakers(n, m):
    band=0
    if m==1 or n%2==0 :
        band=2
    else:
        band=1
    #m == 1 || n % 2 == 0 ? 2 : 1

    return band



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

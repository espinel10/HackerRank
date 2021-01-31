
#URL https://www.hackerrank.com/challenges/pangrams/problem

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    d=list("abcdefghijklmnopqrstuvwxyz")
    entrada=list(s)
    for i in entrada:
        if i.lower() in d:
            d.remove(i.lower())
    if len(d)>0:
        return "not pangram"
    else:
        return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
###############my function#########################
def equalStacks(h1, h2, h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    indices=[sum(h1),sum(h2),sum(h3)]
    entrada=[deque(h1),deque(h2),deque(h3)]
    band=0
    if indices[0]==indices[1] and indices[2]==indices[0]:
        band=1
    while band==0:
        pass
        i=indices.index(max(indices))
        value=entrada[i].pop()
        indices[i]=indices[i]-value
        if indices[0]==indices[1] and indices[2]==indices[0]:
            band=1

    return indices[0]
#######################################
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

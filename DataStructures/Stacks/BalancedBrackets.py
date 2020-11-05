import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def match(a,b):
  if a=="{" and b=="}":
    return 1
  elif a=="(" and b==")":
    return 1
  elif a=="[" and b=="]":
    return 1
  else:
    return 0


def isBalanced(s):
    entrada=list(s)
    a=deque(entrada)
    b=deque()
    while a:
      value=a.pop()
      if b:
        value2=b.pop()
        if match(value,value2)==0:
          b.append(value2)
          b.append(value)
      else:
        b.append(value)
    if b:
      return "NO"
    else:
      return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

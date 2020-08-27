import sys
import random
#######URL
#######https://www.hackerrank.com/challenges/pmix/problem

def prote():
    aleatorio=['A','B','C','D']
    var=random.randint(0,3)
    return aleatorio[var]

cont=0
S=[]
for i in range(10**6):
    S.append(prote())

print(len(S))

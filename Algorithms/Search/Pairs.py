import sys
import random
####URL https://www.hackerrank.com/challenges/pairs/problem

def run(k,entrada,dic):
    cont=0

    for i in range(len(entrada)-1,-1,-1):
        try:
            if dic[entrada[i]-k]>0:
                cont=cont+1
        except KeyError:
            continue

    print(cont)


entrada=[1,3,5,8,6,4,2]
entrada.sort()
k=2
dic = dict(zip(entrada,entrada))
run(k,entrada,dic)

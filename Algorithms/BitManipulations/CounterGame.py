import sys
import math
import time
########URL problems
#######https://www.hackerrank.com/challenges/counter-game/problem

def run(n):
    band=0
    win=0
    cont=0
    while n>1:
        A=bin(n)
        if cont%2!=0:
            print("Richard")
        else:
            print("Louise")
        if A.count('1')==1:
            n=n//2
            print("--{}--".format(n))
            time.sleep(2)
        else:
            i=1
            while n>pow(2,i):
                i=i+1
            i=i-1
            B=bin(pow(2,i))
            n=int(A,2)-int(B,2)

            print("**{}** ".format(n))
            time.sleep(1)

        cont=cont+1

    print("###################")
    if cont%2==0:
        print("Richard")
    else:
        print("Louise")


n=int(input())
run(n)

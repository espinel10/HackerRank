import sys
import random
###URL https://www.hackerrank.com/challenges/fibonacci-modified/problem

def fibonacci_dinamico(n,memo={}):
    if n==1:
        return memo[n]
    elif n==2:
        return memo[n]

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1,memo)**2 + fibonacci_dinamico(n-2,memo)
        memo[n]=resultado
        return resultado

def run(t1,t2,n):
    dic={}
    dic[1]=t1
    dic[2]=t2
    print("---")
    print(fibonacci_dinamico(n,dic))
    print("---")

###0 <= t1,t2 <=  2
##2< n < 20

print("ingrese t1")
t1=int(input())
print("ingrese t2")
t2=int(input())
print("ingrese n")
n=int(input())
run(t1,t2,n)

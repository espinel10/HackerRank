###URL https://www.hackerrank.com/challenges/recursive-digit-sum/problem
import numpy as np
import pandas as pd

def super_digit(n):
  resultado=None
  if int(n)<10:
    resultado=int(n)
  else:
    num=np.array(list(map(int,list(str(n)))))
    print(np.sum(num))
    resultado=super_digit(np.sum(num))

  return resultado

def run(n,k):
    numero=str(n)
    aux=[]
    for i in range(k):
        aux.append(numero)
    return super_digit("".join(aux))

def corregir():
  prueba=[[148,3,3],[9875,4,8],[123,3,9],[9875,1,2]]
  bandera=1
  for i in prueba:
    n=i[0]
    k=i[1]
    result=i[2]
    resp=run(n,k)
    print("{}  {}".format(result,resp))
    if result!=resp:
      bandera=0
  return bandera


if corregir()==1:
  print("CORRECTO")
else:
  print("INCORRECTO")

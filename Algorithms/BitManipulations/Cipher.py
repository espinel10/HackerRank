import sys
import math
import random
############URL
############https://www.hackerrank.com/challenges/cipher/problem


######################una opcion mas eficiente ##################################
def run(N,K,S):
    a=bin(S)[2:]
    entrada=list(map(int,a))
    accum=0
    salida=[]
    iter=len(entrada)-K+1
    for i in range(iter):
        salida.append(accum^entrada[i])
        accum = accum ^ salida[-1]
        if i>=K-1:
            accum =accum ^ salida[i-K+1]

    respuesta="".join(map(str,salida))
    print(int(respuesta,2))
    return "".join(map(str,salida))

#####################segunda opcion poco eficiente y da error de memoria cuando N es 10^6 y K es  10 ^ 6##############################################
def run2(N,K,S):
    entrada=list(bin(S)[2:])
    salida=[]
    ind=len(entrada)-1

    while len(salida)<N:
        aux=None
        if len(salida)<K:
            aux=salida
        else:
            y=len(salida)-(K-1)
            aux=salida[y:]
        salida.append(bitsXor(aux,entrada[ind]))
        ind=ind-1
    salida.reverse()
    respuesta=bin(int("".join(salida),2))[2:]


    print("bits {} --------> mensaje descifrado {} ".format(respuesta,int(respuesta,2)))
    return respuesta



def bitsXor(lista,value):
    if len(lista)==0:
        return value
    else:
        res=lista[0]
        for i in range(len(lista)-1):
            res=xor(res,lista[i+1])
        res=xor(res,value)
        return res

def xor(a,b):
    if a==b:
        return '0'
    else:
        return '1'


#############genero el mensaje a cifrar aleatoriamente
#############y ka es mi variable a que me va a yudar a cifrar
ene=random.randint(1,100000)
ka=random.randint(1,100000)

auxi=[]
for i in range(ka):
    auxi.append(ene<<i)

resp=auxi[0]
for i in range(len(auxi)-1):
    resp=resp^auxi[i+1]
#############S es mi mensaje cifrado
S=resp
#N=10
#K=3
#S='1110011011'
K=ka
N=len(list(bin(ene)[2:]))
print("N {} K {} ".format(N,K))

print(" {} (sindescifrar)---->(mensaje cifrado)".format(ene),end=" ")
print(S)
print("####################")
respuesta=run(N,K,S)
print(respuesta)
if respuesta==bin(ene)[2:]:
    print("CORRECTO")
else:
    print("INCORRECTO")

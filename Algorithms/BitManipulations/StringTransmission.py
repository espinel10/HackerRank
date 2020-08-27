import sys
import math
import random
########URL
#######https://www.hackerrank.com/challenges/string-transmission/problem
cont=0



def trans_dinamic(S,memo,K):
    ##diccionario memo['cadena+K']=valor donde K es el numero de errores maximo permitido
    chain=S[:]
    #print(chain)
    print(memo)
    #print(K)
    #print("**************")
    if len(chain)==2 or len(chain)==3:

        if len(chain)==2:
            sum=0
            auxi=[]
            auxi.append([chain[0],chain[1]])
            if K>0:
                auxi.append([f(chain[0]),chain[1]])
                auxi.append([chain[0],f(chain[1])])
                if K>1:
                    auxi.append([f(chain[0]),f(chain[1])])

            for i in auxi:
                if i.count(0)==2 or i.count(1)==2:
                    continue

                sum=sum+1
            return sum
        else:
            sum=0
            auxi=[]
            auxi.append([chain[0],chain[1],chain[2]])
            if K>0:
                auxi.append([f(chain[0]),chain[1],chain[2]])
                auxi.append([chain[0],f(chain[1]),chain[2]])
                auxi.append([chain[0],chain[1],f(chain[2])])
                if K>1:
                    auxi.append([f(chain[0]),f(chain[1]),chain[2]])
                    auxi.append([chain[0],f(chain[1]),f(chain[0])])
                    auxi.append([f(chain[0]),chain[1],f(chain[2])])
                    if K>2:
                        auxi.append([f(chain[0]),f(chain[1]),f(chain[2])])

            for i in auxi:
                if i.count(0)==3 or i.count(1)==3:
                    continue
                sum=sum+1
            return sum

    try:
        return memo["".join(map(str,chain))+"+"+str(K)]
    except KeyError:
        mitad=len(chain)//2
        resultado=0
        if K!=len(chain):
            if K%2==0:

                resultado=trans_dinamic(chain[mitad:],memo,K//2)+trans_dinamic(chain[:mitad],memo,K//2)
            else:

                resultado=trans_dinamic(chain[mitad:],memo,(K//2)+1)+trans_dinamic(chain[:mitad],memo,K//2)
                resultado=resultado+trans_dinamic(chain[mitad:],memo,K//2)+trans_dinamic(chain[:mitad],memo,(K//2)+1)

        else:
            resultado=trans_dinamic(chain[mitad:],memo,len(chain[mitad:]))+trans_dinamic(chain[:mitad],memo,len(chain[:mitad]))

        memo["".join(map(str,chain))+"+"+str(K)]=resultado
        return resultado




def f(bit):
    if bit==0:
        return 1
    else:
        return 0



k=999
dic={}
s=random.randint(10,1000000)
s=s-1
Si=list(map(int,list(bin(s)[2:])))
opc=trans_dinamic(Si,{},k)
print(opc)

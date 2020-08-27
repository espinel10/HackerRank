import sys

##ULR https://www.hackerrank.com/challenges/icecream-parlor/problem



def run(m,entrada):
    salida=[]
    dic={}
    for i in range(len(entrada)):
        dic[entrada[i]]=i+1

    print(dic)
    for i in range(0,len(entrada)-1):
        try:
            if i+1==dic[m-entrada[i]]:
                continue
            salida.append(dic[m-entrada[i]])
            salida.append(i+1)
            salida.sort()
            break
        except KeyError:
            continue


    print(salida)




m=4
entrada=[1,4,5,3,2]
run(m,entrada)


###URL----> https://www.hackerrank.com/challenges/password-cracker/problem

import sys
import re

class Craker:
    def __init__(self,entrada,output):
        self.entrada=[]
        self.bandera=0
        self.salida=[]
        self.out=output
        for i in entrada:
            Regex_Pattern = r'{}'.format(i)
            test_String=output
            match=re.findall(Regex_Pattern,test_String)
            if len(match)>0:
                self.entrada.append(i)
        Regex_Pattern = r'^[{}]+$'.format("|".join(self.entrada))
        test_String=output
        match=re.findall(Regex_Pattern,test_String)
        if len(match)==1:
            self.craker_password(output,[])

    def verificar_regex(self,j):
        result=[]
        for i in self.entrada:
            if i == j:
                continue
            a=len(list(j))
            b=len(list(i))
            Regex_Pattern = r'^{}.*$'.format(j)
            test_String=i
            if a > b :
                Regex_Pattern = r'^{}.*$'.format(i)
                test_String=j
            match=re.findall(Regex_Pattern,test_String)
            if len(match)>0:
                result.append(i)
        return result

    def craker_password(self,out2,salida):
        sali=salida[:]
        out=out2
        cont=0
        band=0
        while band==0:
            cont2=0
            for i in self.entrada:
                Regex_Pattern = r'^{}.*$'.format(i)
                test_String=out
                match=re.findall(Regex_Pattern,test_String)
                if len(match)==1:
                    opc=self.verificar_regex(i)
                    if len(opc)>0:
                        for j in opc:
                            Regex_Pattern = r'^{}.*$'.format(j)
                            t_S=test_String
                            match=re.findall(Regex_Pattern,t_S)
                            if len(match)>0:
                                k=len(list(j))
                                aux=list(test_String)
                                aux=aux[k:]
                                b=len(list(test_String))
                                sali2=sali[:]
                                sali2.append(j)
                                self.craker_password("".join(aux),sali2)
                                sali2=sali2[:b]
                    k=len(list(i))
                    aux=list(test_String)
                    aux=aux[k:]
                    out="".join(aux)
                    sali.append(i)
                    if out=='':
                        self.bandera=1
                        self.salida=sali

                    if self.bandera==1:
                        band=1
                        break
                else:
                    cont2=cont2+1
            if cont2==len(self.entrada):
                band=1
            if "".join(sali)==self.out:
                self.bandera==1
                band=1
            if cont > 2000:
                band=1
            cont=cont+1

    def getSalida(self):
        if "".join(self.salida)==self.out:
            return " ".join(self.salida)
        else:
            return 'WRONG PASSWORD'



def run(entrada,output):
    cr=Craker(entrada,output)
    print(cr.getSalida())

pw='we web adaman barcod wi weed webada wedding adamantio adamantiotiotia man men mania'
entrada=list(pw.split(" "))
entrada.reverse()
output='webadaman'

run(entrada,output)

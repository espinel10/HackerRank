import sys
import time
import re
import os
###URL https://www.hackerrank.com/challenges/crossword-puzzle/problem

class Edge:
    def __init__(self):
        self.s=None
        self.d=None
        self.Label=None
        self.xy=None

class Puzzle:
    def __init__(self,mapa,words):

        self.words=words
        self.inicio=None
        self.mapa=mapa
        self.resultado=None
        self.opciones=[]
        self.palabras=[]
        self.bandera=0
        self.H=[]
        self.V=[]
        self.camino=[]
        opc=[]
        min=9999999
        xy=None
        for i in range(0,10):
            for j in range(0,10):
                if mapa[i][j]=='-':
                    opc.append([i,j])
                    if i+j<min:
                        min=i+j
                        xy=[i,j]
        inicio=None
        for i in range(0,len(opc)):
            obj=Edge()
            obj.xy=opc[i]
            for j in range(0,len(opc)):
                if opc[i][0]==opc[j][0] and opc[j][1]==opc[i][1]+1:
                    obj.d=j
                if opc[i][1]==opc[j][1] and opc[j][0]==opc[i][0]+1:
                    obj.s=j
                if obj.s!=None and obj.d!=None:
                    break
            if xy==opc[i]:
                inicio=i
            self.opciones.append(obj)
        for j in range(0,len(self.opciones)):
            h=1
            v=1
            if self.V.count(j)==1:
                v=0
            if self.H.count(j)==1:
                h=0
            if h==1:
                self.crosswordH(j)
            if v==1:
                self.crosswordV(j)
        map=self.mapa[:][:]
        cont=0
        pal=self.words
        self.func_recur(map,cont,pal)

    def func_recur(self,map,cont,pal):
        m=map[:][:]
        print("**********************")
        mostrar_mapa(m)
        p=pal[:]
        i=cont
        aux=[]
        if self.bandera==1:
            return

        if len(pal)==0:
            self.bandera=1
            self.mapa=map
            return

        for h in self.camino[i]:
            if m[h[0]][h[1]]=='-':
                aux.append('.')
            else:
                aux.append(m[h[0]][h[1]])
        Regex_Pattern = r'^{}$'.format("".join(aux))
        for j in p:
            if self.bandera==1:
                break
            test_String=j
            match=re.findall(Regex_Pattern,test_String)
            if len(match)>0:
                pr=p[:]
                m2=m[:][:]
                auxi=list(j)
                con=0
                for h in self.camino[i]:
                    m2[h[0]][h[1]]=auxi[con]
                    con=con+1
                pr.remove(test_String)
                self.func_recur(m2,cont+1,pr)


    def crosswordH(self,i):
        camino=[]
        band=0
        while band==0:
            camino.append(self.opciones[i].xy)
            if self.opciones[i].d !=None:
                self.H.append(i)
                i=self.opciones[i].d
            else:
                self.H.append(i)
                band=1
        if len(camino)>1:
            self.camino.append(camino)

    def crosswordV(self,i):
        camino=[]
        band=0
        while band==0:
            camino.append(self.opciones[i].xy)
            if self.opciones[i].s !=None:
                self.V.append(i)
                i=self.opciones[i].s
            else:
                self.V.append(i)
                band=1
        if len(camino)>1:
            self.camino.append(camino)


def mostrar_mapa(mapa):
    for i in range(0,10):
        for j in range(0,10):
            print(mapa[i][j],end=" ")
        print()


def run(entrada,mapa):
    mostrar_mapa(mapa)
    obj=Puzzle(mapa,entrada)
    print()
    mostrar_mapa(obj.mapa)



entrada=['AGRA','NORWAY','ENGLAND','GWALIOR']

entrada.reverse()
mapa=[['+','-','+','+','+','+','+','+','+','+'],
     ['+','-','+','+','+','+','+','+','+','+'],
     ['+','-','-','-','-','-','-','-','+','+'],
     ['+','-','+','+','+','+','+','+','+','+'],
     ['+','-','+','+','+','+','+','+','+','+'],
     ['+','-','-','-','-','-','-','+','+','+'],
     ['+','-','+','+','+','-','+','+','+','+'],
     ['+','+','+','+','+','-','+','+','+','+'],
     ['+','+','+','+','+','-','+','+','+','+'],
     ['+','+','+','+','+','+','+','+','+','+']]


run(entrada,mapa)

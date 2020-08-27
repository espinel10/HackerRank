##URL https://www.hackerrank.com/challenges/count-luck/problem
import sys
import os
import time


class Count:
    def __init__(self,map):
        self.mapa=map
        self.Iposition=[]
        self.Fposition=[]

        self.road=[]
        self.mov=[]
        dic={}
        x=0
        y=0
        for i in map:
            x=0
            for j in i:
                if j=='*':
                    self.Fposition.append(y)
                    self.Fposition.append(x)
                if j=='M':
                    self.Iposition.append(y)
                    self.Iposition.append(x)
                if j=='.':
                    self.mov.append([y,x])
                x=x+1
            y=y+1

        self.mov.append(self.Iposition)
        self.mov.append(self.Fposition)
        self.getRoad([self.Iposition])


    def getCamino(self):
        aux=[]
        for i in range(0,len(self.road)-1):
            if self.road[i][0]!=self.road[i+1][0] and self.road[i][1]!=self.road[i+1][1]:
                continue
            else:
                aux.append(self.road[i])
        aux.append(self.road[-1])
        self.road=aux
        return self.road


    def getUlt(self):
        return self.Fposition

    def getMov(self):
        return self.mov

    def getRoad(self,steps):
        pasos=steps[:]
        movimientos=[]
        ult=pasos[-1]



        if ult==self.Fposition:
            if len(pasos)<len(self.road) or len(self.road)==0:
                self.road=pasos
                return
        a=ult[0]
        b=ult[1]
        if self.mov.count([a,b+1])==1 and pasos.count([a,b+1])==0:
            pasos.append([a,b+1])
            self.getRoad(pasos)


        if self.mov.count([a,b-1])==1 and pasos.count([a,b-1])==0:
            pasos.append([a,b-1])
            self.getRoad(pasos)

        if self.mov.count([a+1,b])==1 and pasos.count([a+1,b])==0:
            pasos.append([a+1,b])
            self.getRoad(pasos)

        if self.mov.count([a-1,b])==1 and pasos.count([a-1,b])==0:
            pasos.append([a-1,b])
            self.getRoad(pasos)




def run(map,k):

    obj=Count(map)
    pasos=obj.getCamino()
    cont=0
    ruta=obj.getMov()
    for p in pasos:
        conta=0
        if p==obj.getUlt():
            break
        if ruta.count([p[0],p[1]+1])==1 and pasos.count([p[0],p[1]+1])==0:
            conta=conta+1
        if ruta.count([p[0],p[1]-1])==1 and pasos.count([p[0],p[1]-1])==0:
            conta=conta+1
        if ruta.count([p[0]+1,p[1]])==1 and pasos.count([p[0]+1,p[1]])==0:
            conta=conta+1
        if ruta.count([p[0]-1,p[1]])==1 and pasos.count([p[0]-1,p[1]])==0:
            conta=conta+1



        if conta>0:
            cont=cont+1






    print("{} {}".format(k,cont))

    if cont==k:
        print("Impressed")
    else:
        print("Oops!")


def mostrar(map):
    os.system ("clear")
    for i in map:
        for x in i:
            print(x,end=" ")
        print()





map=[list('.X.X......X'),
     list('.X*.X.XXX.X'),
     list('.XX.X.XM...'),
     list('......XXXX.')]
k=3

#map=[list("*.M"),
#    list(".X.")]
#k=1

run(map,k)

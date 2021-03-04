
class Node:
    def __init__(self, label, parent):
        self.label = label
        self.bandera=0
        self.clave_valor=[]
        self.hijos = []
        self.parent = parent
        # Métdos para asignar nodos

    def getClave_valor(self):
        return self.clave_valor
    def getLabel(self):
        return self.label
    def setLabel(self, label):
        self.label = label
    def setBandera(self, bandera):
         self.bandera=bandera
    def getBandera(self):
        return self.bandera
    def getHijo(self,clave):
        return self.hijos[clave]
    def setHijo(self, hijo):
        self.hijos.append(hijo)
    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent = parent



class BackHanoi:
  def __init__(self,torre,hist):
    self.N=len(torre)
    self.indices=[1,2,3,4]
    self.torr=torre[:]
    self.ganador=0
    self.vetados=[]
    self.vetados_rama=[]
    self.historial=hist[:]
    self.historial_memo=[]
    self.unos=[1 for i in range(len(torre))]
    self.menor=None
    self.bandera=0
    self.ways=[]
    self.before=[]
    self.caminos=[]
    self.metrica=50
    self.pasos=0
    ###########################
    self.root=Node(torre[:],None)
    self.historial_memo.append(self.root)
    cont=0
    while self.bandera==0 and cont<100:
      print("mejor nro",cont)
      print(torre)
      self.gen_arbol(self.root)
      
      if self.bandera==0:
        mejor=self.best_rama().getLabel()
        torre=mejor[:]
        new_node=Node(torre[:],None)
        self.root=new_node
        self.pasos=0
        self.torr=torre[:]
      else:
        self.before=self.ways[0]+self.before
      cont=cont+1

  def best_path(self):
    return 1
    
  def best_rama(self):
    no_vetados=[]
    for i in self.historial_memo:
      camino=self.recorre(i)
      hijos=self.search(i.getLabel())
      if i not in self.vetados_rama and len(hijos)!=0:
        self.historial=self.historial[:-len(hijos)]
        no_vetados.append(i)
    if len(no_vetados)==0:
      no_vetados=self.historial_memo

    mejor=no_vetados[0]
    for i in no_vetados:
      a=i.getLabel()
      b=mejor.getLabel()
      ai=self.get_j(a)
      bi=self.get_j(b)
      if ai<bi:
        mejor=i
      elif ai==bi:
        if a.count(a[ai-1])<b.count(b[bi-1]) or a[:ai].count(1)<b[:bi].count(1):
          mejor=i
        
    camino=self.recorre(mejor)
    self.before=camino[1:]+self.before
    print(self.before)
    return mejor



  def agregar_movimiento(self,rama):
    aux=[rama.getLabel()]
    pivo=rama
    while pivo.getParent()!=None:
      pivo=pivo.getParent()
      aux.append(pivo.getLabel())

    if aux[0]==self.unos:
      self.bandera=1
      self.ways.append(aux[:])
    
    if aux[0]==self.unos and len(aux)<self.metrica:
      self.menor=aux[:]
      self.metrica=len(self.menor)
    self.caminos.append(aux[:])
    print("recorrido",aux)
    return

  def get_history(self,rama):
    aux=[]
    pivo=rama
    while pivo.getParent()!=None:
      pivo=pivo.getParent()
      for i,j in pivo.getClave_valor():
        aux=aux+[j]
    
    #print("history",aux)
    return aux[:]

  def recorre(self,rama):
    aux=[rama.getLabel()]
    pivo=rama
    while pivo.getParent()!=None:
      pivo=pivo.getParent()
      aux.append(pivo.getLabel())
    return aux[:]

  def progreso(self,rama):
    if rama==self.root:
      return 1
    a=rama.getLabel()
    b=rama.getParent().getLabel()
    i=self.get_j(a)
    j=self.get_j(b)
    if i<j:
      return 1
    else:
      if i==j:
        if a.count(a[i-1])==b.count(b[i-1]):
          return 1
      return 0
      


########################################
  def gen_arbol(self,memo):
    self.pasos=self.pasos+1
    #print(self.pasos)
    if self.bandera==1 or self.pasos>50 :
      return
    #print("--------------------")
    #print("label:",memo.getLabel())
    #print("bandera:",memo.getBandera())
    #hist=self.get_history(memo)
    etiqueta=memo.getLabel()
    if len(memo.getClave_valor())==0:
      rutas=self.search(etiqueta[:])
      #print("---------------------------")
      #print("historial",self.historial)
      #print("entrada",rutas)
      #if len(rutas)>0:
      #  rutas=self.get_pivote(rutas[:],etiqueta[:])
      #print("pivote",rutas)
      if len(rutas)>0 and etiqueta.count(1)<len(etiqueta) and len(self.recorre(memo))<self.metrica:
        rutas=self.get_pivote(rutas,etiqueta)
        #print("pivotes",rutas)
        j=0
        for i in rutas:
          new_node=Node(i[:],memo)
          self.historial_memo.append(new_node)
          memo.setHijo(new_node)
          memo.clave_valor.append((j,i[:]))
          #hist.append(i[:])
          j=j+1
      else:
        #print("no puede seguir mala tuya")
        padre=memo.getParent()
        memo.setBandera(1)
        self.vetados.append(etiqueta)
        self.vetados_rama.append(memo)
        self.agregar_movimiento(memo)
        self.gen_arbol(padre)
        return
    
    
    #print("hijos:",memo.getClave_valor())
    cont=0
    for i in range(0,len(memo.getClave_valor())):
      if memo.getHijo(i).getBandera()==0:
        new_node=memo.getHijo(i)
        #print("voy al hijo",new_node.getLabel())
        self.gen_arbol(new_node)
        break
      cont=cont+1
      

    if cont==len(memo.getClave_valor()) and memo.getLabel()!=self.torr:
      #print("no puede seguir mala tuya")
      self.agregar_movimiento(memo)
      memo.setBandera(1)
      self.vetados.append(etiqueta)
      self.vetados_rama.append(memo)
      padre=memo.getParent()
      self.gen_arbol(padre)

      


  #PIVOTE########################################
  def get_pivote(self,arr,ante):
    pivote=None
    bolsa=[]
    bolsa2=[]
    menor=99999999999999999
    cont=0
    if self.unos in arr:
      return [self.unos]
    for i in arr:
      a=self.get_j(i)
      b=self.get_j(ante)
      if a<b:
        bolsa.append(i[:])
        pivote=i[:]
      else:
        if a==b:
          if i.count(i[a-1])<menor:
            menor=i.count(i[a-1])
    if pivote:
      return bolsa[:]
    else:
      if ante!=self.torr:
        for i in arr:
          a=self.get_j(i[:])
          if i.count(i[a-1])==menor:
            bolsa.append(i[:])
            
        return bolsa[:]
      else:
        
        return arr[:]
  ########################################

  def get_j(self,arr):
    piv=arr[:]
    i=1
    while piv[i:].count(1)!=len(piv[i:]) and len(piv[i:])!=0:
      i=i+1
    return i
     
  def posibles(self,arr,j):
    aux=arr[:j]
    aux.append(arr[j])
    posibles=[]
    for i in self.indices:
      if i not in aux:
        posibles.append(i)
    return posibles

  def search(self,torre):
    torr=torre[:]
    swap=[]
    for i in range(0,len(torr)):
      indie=torre.index(torre[i])
      if i!=indie:
        continue
      opc=self.posibles(torr,i)
      for m in opc:
        swap.append((i,m))
    llenar=[]
    for i in swap:
      aux=torr[:]
      aux[i[0]]=i[1]
      if aux not in self.historial:
        self.historial.append(aux[:])
        llenar.append(aux[:])
    return llenar[:]
        
 


      


def run():
    S=[1,4,1]
    obj=BackHanoi(S)
    

if __name__ == '__main__':
    run()


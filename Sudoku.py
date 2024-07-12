def trovaeluguali(l):
    cop={}
    for j in range(0,len(l)):
        eluguali=1
        for p in range(0,len(l)):
            if j==p:
                pass
            else:
                if l[j]==l[p]:
                    eluguali+=1
        if eluguali!=1:
            cop[eluguali]=l[j]
    return cop

import math
from copy import deepcopy
class cella:
    def __init__(self,v=0,pv=[]):
        self.v=v
        self.pv=pv
    def addpv(self,x):
        if x in self.pv:
            pass
        else:
            if self.pv==[]:
               self.pv.append(x)
            else:
                for i in range(0,len(self.pv)):
                    if self.pv[i]<x:
                        if i==len(self.pv)-1:
                            self.pv.append(x)
                        else:
                            pass
                    else:
                        self.pv.insert(i,x)
                        break
    def delpv(self,x):
        if not(x in self.pv):
            pass
        else:
            self.pv.remove(x)
    def give_v(self,x):
        self.v=x
class sudoku:
    def __init__(self,list):
        self.list=list
    def testprogressi(self):
        pv=0
        for i in range(0,len(self.list[0])):
            for j in range(0,len(self.list[0])):
                pv+=len(self.list[i][j].pv)
        return pv       
    def contavalorir(self,i):
        valori=0
        for j in range(0,len(self.list[0])):
                if self.list[i][j].v!=0:
                    valori+=1
                else:
                    pass
        return valori
    def contavaloric(self,j):
        valori=0
        for i in range(0,len(self.list[0])):
                if self.list[i][j].v!=0:
                    valori+=1
                else:
                    pass
        return valori
    def contavaloria(self,i):
        t=int(math.sqrt(len(self.list[i])))
        valori=0
        for k in range(0,len(self.list[i])):
            if self.list[k/t+(i/t)*t][k%t+(i%t)*t].v!=0:
                valori+=1
            else:
                pass
        return valori
    def contavalori(self):
        val=0
        for i in range(0,len(self.list[0])):
            val+=self.contavalorir(i)
        return val
    def inriga(self,i,x):
        for k in range(0,len(self.list[i])):
            if self.list[i][k].v!=x:
                if k==len(self.list[i])-1:
                    return False
                else:
                    pass
            else:
                return True
    def incolonna(self,i,x):
        for k in range(0,len(self.list[i])):
            if self.list[k][i].v!=x:
                if k==len(self.list[i])-1:
                    return False
                else:
                    pass
            else:
                return True
    def inarea(self,i,x):
        t=int(math.sqrt(len(self.list[i])))
        for k in range(0,len(self.list[i])):
            if self.list[k/t+(i/t)*t][k%t+(i%t)*t].v!=x:
                if k==len(self.list[i])-1:
                    return False
                else:
                    pass
            else:
                return True
    def cinriga(self,i,l):
        if l[0]==i:
            return True
        else:
            return False
    def cincolonna(self,j,l):
        if l[1]==j:
            return True
        else:
            return False
    def cinarea(self,i,l):
        t=int(math.sqrt(len(self.list[0])))
        if t*(l[0]/t)+l[1]/t==i:
            return True
        else:
            return False
    def delriga(self,i,x):
        for k in range(0,len(self.list[i])):
            if x in self.list[i][k].pv:
                self.list[i][k].delpv(x)
            else:
                pass
    def delcolonna(self,i,x):
        for k in range(0,len(self.list[i])):
            if x in self.list[k][i].pv:
                self.list[k][i].delpv(x)
            else:
                pass
    def delarea(self,i,x):
        t=int(math.sqrt(len(self.list[i])))
        for k in range(0,len(self.list[i])):
            if x in self.list[k/t+(i/t)*t][k%t+(i%t)*t].pv:
                self.list[k/t+(i/t)*t][k%t+(i%t)*t].delpv(x)
            else:
                pass
    def insval(self,i,j,x):
        t=int(math.sqrt(len(self.list[i])))
        self.list[i][j].give_v(x)
        self.delriga(i,x)
        self.delcolonna(j,x)
        self.delarea((i/t)*t+j/t,x)
        self.list[i][j].pv=[]
    def inspval(self,i,j):  
        t=int(math.sqrt(len(self.list[0])))
        for p in range(1,len(self.list[0])+1):
            if not(self.incolonna(j,p) or self.inriga(i,p) or self.inarea((i/t)*t+j/t,p)) and\
               self.list[i][j].v==0:
                self.list[i][j].addpv(p)
    def singlepv(self,i,j):
        if len(self.list[i][j].pv)==1:
            self.insval(i,j,self.list[i][j].pv[0])   
    def simplepvr(self,i):
        t=int(math.sqrt(len(self.list[0])))
        for p in range(1,len(self.list[0])+1):
            u=0
            coppie=[]
            for k in range(0,len(self.list[0])):
                if p in self.list[i][k].pv:
                    u+=1
                    coppie += [[i,k]]
            if u==1:
                self.insval(i,coppie[0][1],p)
            else:
                z=set([l[1]/t for l in coppie])
                if len(z)==1:
                    self.delarea((i/t)*t+coppie[0][1]/t,p)
                    for h in coppie:
                        self.list[i][h[1]].addpv(p)
    def simplepvc(self,i):
        t=int(math.sqrt(len(self.list[0])))
        for p in range(1,len(self.list[0])+1):
            u=0
            coppie=[]
            for k in range(0,len(self.list[0])):
                if p in self.list[k][i].pv:
                    u+=1
                    coppie += [[k,i]]
            if u==1:
                self.insval(coppie[0][0],i,p)
            else:
                z=set([l[0]/t for l in coppie])
                if len(z)==1:
                    self.delarea((coppie[0][0]/t)*t+i/t,p)
                    for h in coppie:
                        self.list[h[0]][i].addpv(p)
            
    def simplepva(self,i):
        t=int(math.sqrt(len(self.list[0])))
        for p in range(1,len(self.list[0])+1):
            u=0
            coppie=[]
            for k in range(0,len(self.list[0])):
                if p in self.list[k/t+(i/t)*t][k%t+(i%t)*t].pv:
                    u+=1
                    coppie += [[k/t+(i/t)*t,k%t+(i%t)*t]]
            if u==1:
                self.insval(coppie[0][0],coppie[0][1],p)
            else:
                z=set([h[1] for h in coppie])
                w=set([y[0] for y in coppie])
                if len(z)==1:
                    self.delcolonna(coppie[0][1],p)
                    for h in coppie:
                        self.list[h[0]][h[1]].addpv(p)
                elif len(w)==1:
                    self.delriga(coppie[0][0],p)
                    for y in coppie:
                        self.list[y[0]][y[1]].addpv(p)
    def simple2pvr(self,i):
        duplette=[[x,y] for x in range(1,len(self.list[0])+1) for\
                  y in range(1,len(self.list[0])+1) if x<y]
        for d in duplette:
            u=0
            coppie=[]
            for j in range(0,len(self.list[0])):
                if self.list[i][j].pv==d:
                    u+=1
                    coppie+=[[i,j]]
            if u==2:
                self.delriga(i,d[0])
                self.delriga(i,d[1])
                for h in coppie:
                        self.list[i][h[1]].addpv(d[0])
                        self.list[i][h[1]].addpv(d[1])
    def simple3pvr(self,i):
        if self.contavalorir(i)<6:
            ctripl=[[[i,x],[i,y],[i,z]]for x in range(0,len(self.list[0])) \
         for y in range(0,len(self.list[0])) \
         for z in range(0,len(self.list[0])) \
                if x<y and y<z and \
                (self.list[i][x].v==self.list[i][y].v==self.list[i][z].v==0)]
            for m in ctripl:
                test=list(set(self.list[i][m[0][1]].pv+\
                         self.list[i][m[1][1]].pv+\
                         self.list[i][m[2][1]].pv))
                if len(test)==3:
                    for g in range(0,len(self.list[0])):
                        if [i,g] in m:
                            pass
                        else:
                            self.list[i][g].delpv(test[0])
                            self.list[i][g].delpv(test[1])
                            self.list[i][g].delpv(test[2])
                            
                    
            
    def simple2pvc(self,j):
        duplette=[[x,y] for x in range(1,len(self.list[0])+1) for\
                  y in range(1,len(self.list[0])+1) if x<y]
        for d in duplette:
            u=0
            coppie=[]
            for i in range(0,len(self.list[0])):
                if self.list[i][j].pv==d:
                    u+=1
                    coppie+=[[i,j]]
            if u==2:
                self.delcolonna(j,d[0])
                self.delcolonna(j,d[1])
                for h in coppie:
                        self.list[h[0]][j].addpv(d[0])
                        self.list[h[0]][j].addpv(d[1])
    def simple3pvc(self,j):
        if self.contavaloric(j)<6:
            ctripl=[[[x,j],[y,j],[z,j]]for x in range(0,len(self.list[0])) \
             for y in range(0,len(self.list[0])) \
             for z in range(0,len(self.list[0])) \
                if x<y and y<z and \
                (self.list[x][j].v==self.list[y][j].v==self.list[z][j].v==0)]
            for m in ctripl:
                test=list(set(self.list[m[0][0]][j].pv+\
                    self.list[m[1][0]][j].pv+\
                    self.list[m[2][0]][j].pv))
                if len(test)==3:
                    for g in range(0,len(self.list[0])):
                        if [g,j] in m:
                            pass
                        else:
                            self.list[g][j].delpv(test[0])
                            self.list[g][j].delpv(test[1])
                            self.list[g][j].delpv(test[2])
                
    def simple2pva(self,i):
        t=int(math.sqrt(len(self.list[i])))
        duplette=[[x,y] for x in range(1,len(self.list[0])+1) for\
                  y in range(1,len(self.list[0])+1) if x<y]
        for d in duplette:
            u=0
            coppie=[]
            for k in range(0,len(self.list[0])):
                if self.list[k/t+(i/t)*t][k%t+(i%t)*t].pv==d:
                    u+=1
                    coppie += [[k/t+(i/t)*t,k%t+(i%t)*t]]
            if u==2:
                self.delarea((coppie[0][0]/t)*t+coppie[0][1]/t,d[0])
                self.delarea((coppie[0][0]/t)*t+coppie[0][1]/t,d[1])
                for h in coppie:
                        self.list[h[0]][h[1]].addpv(d[0])
                        self.list[h[0]][h[1]].addpv(d[1])
    def simple3pva(self,i):
        t=int(math.sqrt(len(self.list[i])))
        if self.contavaloria(i)<6:
            ctripl=[[[x/t+(i/t)*t,x%t+(i%t)*t],\
                  [y/t+(i/t)*t,y%t+(i%t)*t],\
                  [z/t+(i/t)*t,z%t+(i%t)*t]]\
                 for x in range(0,len(self.list[0])) \
                 for y in range(0,len(self.list[0])) \
                 for z in range(0,len(self.list[0])) \
                 if x<y and y<z and\
                        self.list[x/t+(i/t)*t][x%t+(i%t)*t].v==\
                        self.list[y/t+(i/t)*t][y%t+(i%t)*t].v==\
                        self.list[z/t+(i/t)*t][z%t+(i%t)*t].v==0]
            for m in ctripl:
                test=list(set(self.list[m[0][0]][m[0][1]].pv+\
                         self.list[m[1][0]][m[1][1]].pv+\
                         self.list[m[2][0]][m[2][1]].pv))
                if len(test)==3:
                    for g in range(0,len(self.list[0])):
                        if [g/t+(i/t)*t,g%t+(i%t)*t] in m:
                            pass
                        else:
                            self.list[g/t+(i/t)*t][g%t+(i%t)*t].delpv(test[0])
                            self.list[g/t+(i/t)*t][g%t+(i%t)*t].delpv(test[1])
                            self.list[g/t+(i/t)*t][g%t+(i%t)*t].delpv(test[2])
    def celleconpvr(self,i,x):
        if self.inriga(i,x):
            pass
        else:
            return [[i,j] for j in range(0,len(self.list[0])) \
                if x in self.list[i][j].pv]
    def celleconpvc(self,j,x):
        if self.incolonna(j,x):
            pass
        else:
            return [[i,j] for i in range(0,len(self.list[0])) \
                if x in self.list[i][j].pv]
    def celleconpva(self,i,x):
        t=int(math.sqrt(len(self.list[i])))
        if self.inarea(i,x):
            pass
        else:
            return [[k/t+(i/t)*t,k%t+(i%t)*t] \
                for k in range(0,len(self.list[0])) \
                if x in self.list[k/t+(i/t)*t][k%t+(i%t)*t].pv]
                
    def simple4pvr(self,i):
        combinazioni=[self.celleconpvr(i,p) \
                      for p in range(1,len(self.list[0])+1)]
        for u in range(0,len(self.list[0])):
                if None in combinazioni:
                    combinazioni.remove(None)
                else:
                    break
        if combinazioni==[]:
            pass
        else:
            d=trovaeluguali(combinazioni)
            for e in d:
                if e==len(d[e]) and\
                           (len(d[e])<len(self.list[0])-self.contavalorir(i)):
                    listaunione=[]
                    intersez=set(self.list[i][d[e][0][1]].pv)
                    for q in d[e]:
                        intersez&=set(self.list[q[0]][q[1]].pv)
                    for j in range(0,len(self.list[0])):
                        if not([i,j] in d[e]):
                            listaunione+=self.list[i][j].pv
                    valoridacanc=set(range(1,len(self.list[0])+1))-(intersez-set(listaunione))
                    for q in d[e]:
                        for p in valoridacanc:
                            self.list[q[0]][q[1]].delpv(p)
            
    def simple4pvc(self,j):
        combinazioni=[self.celleconpvc(j,p) \
                      for p in range(1,len(self.list[0])+1)]
        for u in range(0,len(self.list[0])):
                if None in combinazioni:
                    combinazioni.remove(None)
                else:
                    break
        if combinazioni==[]:
            pass
        else:
            d=trovaeluguali(combinazioni)
            for e in d:
                if e==len(d[e]) and\
                           (len(d[e])<len(self.list[0])-self.contavaloric(j)):
                    listaunione=[]
                    intersez=set(self.list[d[e][0][0]][j].pv)
                    for q in d[e]:
                        intersez&=set(self.list[q[0]][q[1]].pv)
                    for i in range(0,len(self.list[0])):
                        if not([i,j] in d[e]):
                            listaunione+=self.list[i][j].pv
                    valoridacanc=set(range(1,len(self.list[0])+1))-(intersez-set(listaunione))
                    for q in d[e]:
                        for p in valoridacanc:
                            self.list[q[0]][q[1]].delpv(p)

                        
                                        
    def simple4pva(self,i):
        t=int(math.sqrt(len(self.list[i])))
        combinazioni=[self.celleconpva(i,p) \
                      for p in range(1,len(self.list[0])+1)]
        for u in range(0,len(self.list[0])):
                if None in combinazioni:
                    combinazioni.remove(None)
                else:
                    break
        if combinazioni==[]:
            pass
        else:
            d=trovaeluguali(combinazioni)
            for e in d:
                if e==len(d[e]) and\
                           (len(d[e])<len(self.list[0])-self.contavaloria(i)):
                    listaunione=[]
                    intersez=set(self.list[d[e][0][0]][d[e][0][1]].pv)
                    for q in d[e]:
                        intersez&=set(self.list[q[0]][q[1]].pv)
                    for k in range(0,len(self.list[0])):
                        if not([k/t+(i/t)*t,k%t+(i%t)*t] in d[e]):
                            listaunione+=self.list[k/t+(i/t)*t][k%t+(i%t)*t].pv
                    valoridacanc=set(range(1,len(self.list[0])+1))-(intersez-set(listaunione))
                    for q in d[e]:
                        for p in valoridacanc:
                            self.list[q[0]][q[1]].delpv(p)
    
    def semplpvr(self,i):
        self.simple2pvr(i)
        self.simple3pvr(i)
        self.simple4pvr(i)
    def semplpvc(self,j):
        self.simple2pvc(j)
        self.simple3pvc(j)
        self.simple4pvc(j)
    def semplpva(self,i):
        self.simple2pva(i)
        self.simple3pva(i)
        self.simple4pva(i)
    
    def loop(self):
        newt=0
        t=1
        while self.contavalori()<(len(self.list[0]))**2 and (newt<t):
            t=self.testprogressi()
            for q in range(0,len(self.list[0])):
                self.simplepvr(q)
                self.simplepvc(q)
                self.simplepva(q)
                self.semplpvr(q)
                self.semplpvc(q)
                self.semplpva(q)
                for i in range(0,len(self.list[0])):
                    for j in range(0,len(self.list[0])):
                        self.singlepv(i,j)
            newt=self.testprogressi()   
    def solve(self):
        t=int(math.sqrt(len(self.list[0])))
        for i in range(0,len(self.list[0])):
            for j in range(0,len(self.list[0])):
                self.list[i][j]=cella(self.list[i][j],[])
        for i in range(0,len(self.list[0])):
            for j in range(0,len(self.list[0])):
                self.inspval(i,j)
                self.singlepv(i,j)
        for i in range(0,len(self.list[0])):
            for j in range(0,len(self.list[0])):
                self.singlepv(i,j)
        self.loop()
        if self.contavalori()==(len(self.list[0]))**2:
            f=[[self.list[i][j].v for j in range(0,len(self.list[0]))]for i in range(0,len(self.list[0]))]
            for i in range(0,len(self.list[0])):
                print f[i]
        else:
            r=True
            other=sudoku(deepcopy(self.list))
            for i in range(0,len(self.list[0])):
                if r:
                    for j in range(0,len(self.list[0])):
                        if len(self.list[i][j].pv)==2:
                            other.insval(i,j,self.list[i][j].pv[0])
                            other.loop()
                            if other.contavalori()==(len(self.list[0]))**2:
                                r=False
                                break
                            else:
                                other=sudoku(deepcopy(self.list))
                                other.insval(i,j,self.list[i][j].pv[1])
                                other.loop()
                                if other.contavalori()==(len(self.list[0]))**2:
                                    r=False
                                    break
                                    
            f=[[other.list[i][j].v for j in range(0,len(self.list[0]))]for i in range(0,len(self.list[0]))]
            for i in range(0,len(self.list[0])):
                print f[i]
    def p(self):
        for i in range(0,len(self.list[0])):
            for j in range(0,len(self.list[0])):
                self.list[i][j]=cella(self.list[i][j],[])
    def p1(self):
        for i in range(0,len(self.list[0])):
            for j in range(0,len(self.list[0])):
                self.inspval(i,j)
    def p2(self):
        f=[[self.list[i][j].v for j in range(0,len(self.list[0]))]for i in range(0,len(self.list[0]))]
        for i in range(0,len(self.list[0])):
            print f[i]
    def p2v(self):
        f=[[self.list[i][j].pv for j in range(0,len(self.list[0]))]for i in range(0,len(self.list[0]))]
        for i in range(0,len(self.list[0])):
            print f[i]

        

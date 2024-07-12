import math
import string
def inizio(s,c,n):
    def ini(s,c,n): 
        if not s:
            return 0
        elif s[0]!=c:
            return 0
        elif s[0]==c:
             t=1+ini(s[1:len(s)],c,n)
        return t
    return ini(s,c,n)==n
def lun(l):
    d={}
    d[len(l[0])]=[l[0]]
    for i in range(1,len(l)):
        trovato=False
        for k in range(0,i):
            if len(l[i])==len(l[k]):
                d[len(l[k])] = [l[k]]+[l[i]]
                trovato=True
        if not t:
            d[len(l[i])] = [l[i]]
    if 0 in d:
        del d[0]
    for h in d:
        print h, ", ".join(d[h])

def Trovain(l,n):
    trovato=False
    indice=0
    while (not trovato) and indice<=len(l)-1:
        if l[indice]==n:
            trovato= True
            print indice+1
        indice += 1
    if not trovato:
        print None
def spirale(n):
    def frontiera(n,k,m):
        j=(len(m)-n)/2
        for i in range(n):
            m[j][j+i]=k+i
        for i in range(n-1):
            m[j+1+i][j+n-1]=k+n+i
        for i in range(n-1):
            m[j+n-1][j+n-2-i]=k+2*n-1+i
        for i in range(n-2):
            m[j+n-2-i][j]=k+3*n-2+i
        
    spir=[[0 for i in range(n)]for i in range(n)]
    if n==0:
        return None
    elif n==1:
        return 1
    else:
        for i in range(n/2+n%2):
            frontiera(n-2*i,4*i*(n-i)+1,spir)
        spazi= int(math.log(n**2)/math.log(10))
        for i in range(n):
            for h in range(n):
                spir[i][h]= "%d" %spir[i][h]+" "*(1+ spazi-int(math.log(spir[i][h])/math.log(10)))
        for i in range(n):
            spir[i]= "".join(spir[i])
        for c in spir:
            print c
        
            
class cellulare:

    def __init__(self,marca,modello,prezzo):
        self.marca=marca
        self.modello=modello
        self.prezzo=prezzo
    def modifica_prezzo(self,n):
        self.prezzo=n
class magazzino:
    def __init__(self,inventario={},n_inv=0):
        self.inventario=inventario
        self.n_inv = n_inv
    def inserisci_nuovo_modello(self,cellulare,n):
        self.inventario[self.n_inv]=[cellulare,n]
        self.n_inv +=1
    def acquisisci_nuovo(self,n,k):
        self.inventario[n][1] += k
    def vendita(self,n,k):
        if self.inventario[n][1]==0:
            print "Esaurito"
        elif self.inventario[n][1]>0 and k>self.inventario[n][1]:
            print "Non disponibile in quantità richiesta; ve ne sono %d \
         in magazzino" %self.inventario[n][1]
        else: 
            self.inventario[n][1] -= k

def stamp(N):
    for i in range(0,N):
        for k in range(0,i+1):
            print N-k,
        print
def read():
    s=raw_input("Inserisci Frase: ")
    print s
    for c in string.letters:
        if s.count(c)!=0:
            print "%s compare %d" %(c, s.count(c))
def p():
    n=[]
    a=int(raw_input("Inserire numero intero: "))
    n.append(a)
    while a!=0:
        a=int(raw_input("Inserire numero intero: "))
        n.append(a)
    n.remove(0)
    print "Somma: %d" %(sum(n))
    print "Media: %f" %(float(sum(n))/len(n))
    print "Minimo: %d" %(min(n))
    print "Massimo: %d" %(max(n))
def leggi():
    s=raw_input("Inserisci stringa: ")
    cv=0
    cc=0
    d={}
    for c in string.letters:
        if c not in "aeiou" and s.count(c)!=0:
            cc+=s.count(c)
            d[c]=s.count(c)
        elif c in "aeiou" and s.count(c)!=0:
            cv+=s.count(c)
            d[c]=s.count(c)
    print (cv,cc,d)
    
        
        

    

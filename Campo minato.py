import random
import copy
class campo_minato:
    def __init__(self,m,n,b):
        self.m=m
        self.n=n
        self.b=b
        self.l=[["" for j in range(self.n)] for i in range(self.m) ]
        for p in range(self.b):
            self.l[random.randrange(0,self.m)][random.randrange(0,self.n)]="*"
    def contabombe(self,i,j):
        p=0
        for c in [-1,0,1]:
            for a in [-1,0,1]:
                if i+c in range(self.m) and j+a in range(self.n) and not(c==0 and a==0):
                    if self.l[i+c][j+a]=="*":
                        p+=1
        return p
    
                        

    def gioca(self):
        print "Quando verrà richiesto l'inserimento della mossa da effettuare, inserire 0 se si \
vuole cliccare la casella, 1 se si vuole contrassegnarla con una bandera e 2 se si vuole \
togliere il contrassegno; digitare Exit se si vuole terminare il gioco."
        risultato=True
        vinto=True
        campo=[["" for j in range(self.n)] for i in range(self.m) ]
        def clicca_ricorsivo(self,i,j):
            if self.contabombe(i,j)!=0:
                campo[i][j]=self.contabombe(i,j)
            else:
                campo[i][j]=0
                for c in [-1,0,1]:
                    for a in [-1,0,1]:
                        if i+c in range(self.m) and j+a in range(self.n) and campo[i+c][j+a]=="":
                            clicca_ricorsivo(self,i+c,j+a)
        def clicca0(self,i,j):
            if self.l[i][j]=="*":
                pass
            else:
                clicca_ricorsivo(self,i,j)
        while risultato and vinto:
            i=int(raw_input("indice riga:"))
            j=int(raw_input("indice colonna:"))
            d=int(raw_input("Mossa: "))
            c_valida= i in range(self.m) and j in range(self.n)
            if d==0 and c_valida:    
                clicca0(self,i,j)
                if self.l[i][j]=="*":
                    risultato=False
            if d==1 and c_valida:
                campo[i][j]="T"
            if d==2 and c_valida:
                campo[i][j]=""
            if d=="Exit":
                break
            if risultato:
                for v in campo:
                    print v
            conta=0
            for v in range(self.m):
                for g in range(self.n):
                    if self.l[v][g]=="*" and campo[v][g]=="T":
                        conta+=1
            if conta==self.b:
                vinto=False
        if not vinto:
            print "Complimenti hai vinto"
        else:
            for v in self.l:
                print v
            print "Hai Perso"
                
                

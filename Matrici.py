import math
class Ratio():
    def __init__(self,num,den=1):
        if den==1:
            self.num,self.den=num,1
            return
        if den<0:
            self.num,self.den=-num,-den
        else:
            self.num,self.den= num,den
        mcd =self.__mcd(abs(num),abs(den))
        self.num /= mcd
        self.den /= mcd
    def __repr__(self):
        return "Ratio(%d,%d)"%(self.num,self.den)
    def __str__(self):
        if self.den!=1:
            return "%d/%d"%(self.num,self.den)
        return "%d"%self.num
    def __eq__(self,other):
        return float(self.num)/self.den==float(other.num)/other.den
    def __lt__(self,other):
        return float(self.num)/self.den<float(other.num)/other.den
    def __le__(self,other):
        return float(self.num)/self.den<=float(other.num)/other.den
    def __gt__(self,other):
        return float(self.num)/self.den>float(other.num)/other.den
    def __ge__(self,other):
        return float(self.num)/self.den>=float(other.num)/other.den
    def __nonzero__(self):
        return self.num
    def __neg__(self):
        return Ratio(-self.num,self.den)
    def __add__(self,other):
        if type(other)==type(1):
            other=Ratio(other)
        return Ratio(self.num*other.den+other.num*self.den,self.den*other.den)
    def __sub__(self,other):
        if type(other)==type(1):
            other=Ratio(other)
        return Ratio(self.num*other.den-other.num*self.den,self.den*other.den)
    def __mul__(self,other):
        if type(other)==type(1):
            other=Ratio(other)
        return Ratio(self.num*other.num,self.den*other.den)
    def __div__(self,other):
        if type(other)==type(1):
            other=Ratio(other)
        return Ratio(self.num*other.den,self.den*other.num)
    def __mcd(self,x,y):
        if x==y:
            return x
        elif x>y:
            return self.__mcd(x-y,x)
        else:
            return self.__mcd(x,y-x)
class pol:
    def __init__(self,l):
        self.l=l
    def deg(self):
        return len(self.l)-1
    def __repr__(self):
        p=""
        g=self.deg()+1
        for i in self.l[:(len(self.l)-1)]:
            g+=-1
            if i==1:
                p += "x^%d+"%g if g!=1 else "x+"
            elif i==0:
                pass
            elif i==-1:
                p += "-x^%d+"%g if g!=1 else "-x+"
            else:
                p += str(i)
                p+="x^%d+"%g if g!=1 else "x+"
        if self.l[self.deg()]!=0:
            p += str(self.l[self.deg()])
        if p[-1]=="+":
            p=p[:-1]
        p=p.replace("+-","-")
        return p
    def __add__(self,other):
        if self.deg()<other.deg():
            self,other=other,self
        k=[]
        for j in range(len(self.l)-len(other.l)):
            k.append(self.l[j])
        for i in range(len(self.l)-len(other.l),len(self.l)):
            k.append(self.l[i]+other.l[i-(len(self.l)-len(other.l))])
        return pol(k)
    def __radd__(self,n):
        self.l[len(self.l)-1]+=n
        return self
    def __mul__(self,other):
        k=[0 for i in range(self.deg()+other.deg()+1)]
        for j in range(len(self.l)):
            for i in range(len(other.l)):
                k[j+i]+=self.l[j]*other.l[i]
        return pol(k)
    def __rmul__(self,n):
        k=[n*t for t in self.l]
        return pol(k)
    def __sub__(self,other):
        return self+(-1)*other
class matrix():
    def __init__(self,list):
        self.list=list

    def righe(self):
        return len(self.list)
    def colonne(self):
        return len(self.list[0])
    def test(self):
        return self.colonne()==self.righe()
    def rc(self,other,n,m):
        x=0
        for i in range(0,self.colonne()):
            z= x + other.list[i][m]*self.list[n][i]
            x=z
        return x
    def __mul__(self,other):
        if not self.colonne()==other.righe():
            print 'Il prodotto non può essere eseguito!'
        else:
            p=[[i for i in range(0,other.colonne())] for i in range(0,self.righe())]
            for c in range(0,other.colonne()):
                for r in range(0,self.righe()):
                    p[r][c]= self.rc(other,r,c)
        return matrix(p)
    def scal(self,n):
        for j in range(0,self.colonne()):
            for i in range(0,self.righe()):
                self.list[i][j]= self.list[i][j]*n
        return self
    def __add__(self,other):
        if self.righe()==other.righe() and \
           self.colonne()==other.colonne():
            s=[[i for i in range(0,other.colonne())] for i in range(0,self.righe())]
            for c in range(0,self.colonne()):
                for r in range(0,self.righe()):
                    s[r][c]= self.list[r][c]+other.list[r][c]
            return s
        else:
            print 'La somma non può essere eseguita!'

    def __repr__(self):
        return self.__str__()            
    
    def __str__(self):
        s=""
        for i in range(0,self.righe()):
            s = s+ str(self.list[i])+"\n"
        return s
    def power(self,n):
        if n<0:
            return "impossibile"
        if n==0:
            return [[0 if i!=k else 1 for i in range(0,self.colonne())]for k in range(0,self.colonne())]
        else:
            return self*matrix(self.power2(n-1))
        

    def transp(self):
        tr=[[self.list[c][i] for c in range(self.righe())] for i in range(self.colonne())]
        return matrix(tr)
    def sottmatrix(self,i,j):
        k= [[self.list[r][c] for c in range(0,self.colonne())] for r in range(0,self.righe())]
        for d in range(0,len(k)):
            del k[d][j]
        del k[i]
        return matrix(k)
    
    def det(self):
        if not (self.test()):
            print 'Non è una matrice quadrata, idiota!'
        else:
            if self.colonne()==4:
                return self.list[0][0]*(self.list[1][1]*self.list[2][2]*self.list[3][3] + \
                   self.list[1][2]*self.list[2][3]*self.list[3][1] +\
                   self.list[1][3]*self.list[2][1]*self.list[3][2] -\
                   self.list[1][2]*self.list[2][1]*self.list[3][3] -\
                   self.list[1][3]*self.list[2][2]*self.list[3][1] -\
                   self.list[1][1]*self.list[2][3]*self.list[3][2])-\
                   self.list[1][0]*(self.list[0][1]*self.list[2][2]*self.list[3][3] + \
                   self.list[0][2]*self.list[2][3]*self.list[3][1] +\
                   self.list[0][3]*self.list[2][1]*self.list[3][2] -\
                   self.list[3][1]*self.list[2][2]*self.list[0][3] -\
                   self.list[3][2]*self.list[2][3]*self.list[0][1] -\
                   self.list[3][3]*self.list[2][1]*self.list[0][2])+\
                   self.list[2][0]*(self.list[0][1]*self.list[1][2]*self.list[3][3] + \
                   self.list[0][2]*self.list[1][3]*self.list[3][1] +\
                   self.list[0][3]*self.list[1][1]*self.list[3][2] -\
                   self.list[3][1]*self.list[1][2]*self.list[0][3] -\
                   self.list[3][2]*self.list[1][3]*self.list[0][1] -\
                   self.list[3][3]*self.list[1][1]*self.list[0][2])-\
                   self.list[3][0]*(self.list[0][1]*self.list[1][2]*self.list[2][3] + \
                   self.list[0][2]*self.list[1][3]*self.list[2][1] +\
                   self.list[0][3]*self.list[1][1]*self.list[2][2] -\
                   self.list[0][2]*self.list[1][1]*self.list[2][3] -\
                   self.list[0][3]*self.list[1][2]*self.list[2][1] -\
                   self.list[0][1]*self.list[1][3]*self.list[2][2])
            elif self.colonne()==3:
                return self.list[0][0]*self.list[1][1]*self.list[2][2] + \
                   self.list[0][1]*self.list[1][2]*self.list[2][0] +\
                   self.list[0][2]*self.list[1][0]*self.list[2][1] -\
                   self.list[0][1]*self.list[1][0]*self.list[2][2] -\
                   self.list[0][2]*self.list[1][1]*self.list[2][0] -\
                   self.list[0][0]*self.list[1][2]*self.list[2][1]
            elif self.colonne()==2:
                return self.list[0][0]*self.list[1][1]- \
                   self.list[0][1]*self.list[1][0]
            elif self.colonne()==1:
                return self.list[0][0]
            else:
                x=0
                for k in range(0,self.colonne()):
                    z= x + ((-1)**(k+2))*self.list[k][0]*(self.sottmatrix(k,0).det())
                    x=z
                return x
    def p_caratteristico(self):
        xid=[[pol([1,0]) if i==j else 0 for i in range(self.colonne())]for j in range(self.colonne())]
        A=[[pol([-self.list[i][j]]) for j in range(self.colonne())] for i in range(self.righe())]
        X=matrix(matrix(xid)+matrix(A))
        return X.det()
    def inv(self):
        d=[self.det()]
        if (self.test() and d[0]==0):
            print "la matrice non è invertibile"
        else:
            inverse = [[float((-1)**(r+c+2)*(self.sottmatrix(c,r)).det())/d[0] for c in range(0,self.colonne())] for r in range(0,self.righe())]
            return matrix(inverse)

    def Tr(self):
        if self.test():
            x=0
            for i in range(0,self.colonne()):
                z= x + self.list[i][i]
                x=z
            return x
        else:
            return None
    def addmulc(self,a,b,n):
        for i in range(0,self.righe()):
            self.list[i][a]+= float(n)*self.list[i][b]
    def addmulr(self,a,b,n):
        for i in range(0,self.colonne()):
            self.list[a][i]+= float(n)*self.list[b][i]
    def changec(self,a,b):
        if a==b:
            pass
        for i in range(0,self.righe()):
            t=self.list[i][a]
            self.list[i][a]=self.list[i][b]
            self.list[i][b]=t
    def changer(self,a,b):
        if a==b:
            pass
        for i in range(0,self.colonne()):
            t=self.list[a][i]
            self.list[a][i]=self.list[b][i]
            self.list[b][i]=t
    def mulc(self,a,n):
        for i in range(0,self.righe()):
            self.list[i][a]=float(n)*self.list[i][a]
    def mulr(self,a,n):
        for i in range(0,self.colonne()):
            self.list[a][i]=float(n)*self.list[a][i]
    def rk(self):
        if self.colonne()==self.righe() and self.det()!=0:
            return self.colonne()
        else:
            if self.colonne()>self.righe():
                self=matrix(self.transp())
            rk=0
            ker=0
            while rk+ker!=self.colonne():
                r=0
                nonfinito=True
                while nonfinito and self.list[r][rk]==0:
                    if r==self.righe()-1:
                        nonfinito=False
                    r+=1
                if r==self.righe():
                    self.changec(rk,self.colonne()-ker-1)
                    ker+=1
                else:
                    self.changer(rk,r)
                    self.mulc(rk,float(1)/self.list[rk][rk])
                    for i in range(0,self.colonne()-rk-1):
                        self.addmulc(rk+i+1,rk,float(-1)*self.list[rk][rk+i+1])
                    for k in range(0,self.righe()-rk-1):
                        self.addmulr(rk+k+1,rk,float(-1)*self.list[rk+k+1][rk])
                    rk+=1
            return rk
    def ker(self):
        return self.colonne()-self.rk()
    
class vector():
    def __init__(self,list):
        self.list=list
    def M(self,matrix):
        i = [o for o in range(0,len(self.list))]
        if not (len(self.list)==matrix.colonne()):
            print "il vettore non appartiene al dominio dell'applicazione"
        else:
            for h in range(0,len(self.list)):
                x=0
                for k in range(0,len(self.list)):
                    z = x + self.list[k]*matrix.list[h][k]
                    x=z
                i[h]=x
        return i
    def __add__(self,other):
        if len(self.list)==len(other.list):
            return [self.list[i]+other.list[i] for i in range(0,len(self.list))]
        else:
            print "Error"
    def __mul__(self,other):
        if len(self.list)!=len(other.list):
            print "Error"
        s=0
        for i in range(len(self.list)):
            s= self.list[i].conjugate()*other.list[i]+s
        return s
    def __rmul__(self,a):
        return [self.list[i]*a for i in range(0,len(self.list))]
        
    def norma(self):
        print math.sqrt(self*self)
        
    
        
        
    

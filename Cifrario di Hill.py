
def invmod26(n):
        n %= 26
        d={1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17,25:25}
        if not(n in d):
            return None
        else:
            return d[n]
class matrix():
    def __init__(self,list):
        self.list=list

    def righe(self):
        return len(self.list)
    def colonne(self):
        return len(self.list[0])
    def test(self,other):
        return self.colonne()==self.righe()
    def rc(self,other,n,m):
        x=0
        for i in range(0,self.colonne()):
            z= x + other.list[i][m]*self.list[n][i]
            x=z
        return x


    def __mul__(self,other):
        if not self.test(other):
            print 'Il prodotto non può essere eseguito!'
        else:
            p=[[i for i in range(0,other.colonne())] for i in range(0,self.righe())]
            for c in range(0,other.colonne()):
                for r in range(0,self.righe()):
                    p[r][c]= self.rc(other,r,c)
        return p

        

    def transp(self):
        tr=[[self.list[c][i] for c in range(self.righe())] for i in range(self.colonne())]
        return tr


    def sottmatrix(self,i,j):
        k= [[o for o in range(0,self.colonne())] for o in range(0,self.righe())]
        for c in range(0,self.colonne()):
            for r in range(0,self.righe()):
                k[r][c]= self.list[r][c]
        for d in range(0,len(k)):
            del k[d][j]
        del k[i]
        return k
    def det(self):
        if not (self.colonne()==self.righe()):
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
                    z= x + ((-1)**(k+2))*self.list[k][0]*(matrix(self.sottmatrix(k,0)).det())
                    x=z
                return x
    def inv(self):
        d=[self.det()]
        if (self.colonne()==self.righe() and d[0]==0):
            print "la matrice non è invertibile"
        else:
            inverse = [[o for o in range(0,self.colonne())] for o in range(0,self.righe())]
            for r in range(0,self.righe()):
                for c in range(0,self.colonne()):
                    inverse[r][c]= float((-1)**(r+c+2)*(matrix(self.sottmatrix(c,r))).det())/d[0]
            return inverse
    
    def invZ26(self):
        d = invmod26(self.det())
        if not d :
            print "la matrice non è invertibile"
        else:
                inverse = [[o for o in range(0,self.colonne())] for o in range(0,self.righe())]
                for r in range(0,self.righe()):
                        for c in range(0,self.colonne()):
                                inverse[r][c]= d*((-1)**(r+c+2)*(matrix(self.sottmatrix(c,r))).det())
                for r in range(len(inverse)):
                        for c in range(len(inverse[0])):
                            inverse[r][c] %=26
                return inverse





def cryhill(s,key):
    key = matrix(key)
    for r in range(key.righe()):
        for c in range(key.colonne()):
            key.list[r][c] %=26
    det = key.det()%26
    if not(invmod26(det)):
        print "La matrice non è invertibile!!!"
    else:
        s = s.lower()
        s = s.replace('è','e').replace('é','e').replace('à','a').replace('ì','i').replace('ù','u').replace('ò','o')
        testocript=[c for c in s]
        t=[(ord(c)-97) for c in s if c.isalpha()]
        if len(t)%(key.colonne())!=0:
            for i in range(key.colonne()-len(t)%(key.colonne())):
                t.append(23)
                nontrovato=True
                e=0
                while nontrovato:
                        if testocript[len(testocript)-1-e].isalpha():
                                testocript.insert(len(testocript)-e,"x")
                                nontrovato=False
                        else:
                                e +=1
        m=[]
        for i in range(len(t)/(key.colonne())):
            v=[]
            for k in range(key.colonne()*i,key.colonne()*(i+1)):
                v.append(t[k])
            m.append(v)
        m = matrix(matrix(m).transp())
        tcry= matrix(matrix(key*m).transp())
        for r in range(tcry.righe()):
            for c in range(tcry.colonne()):
                tcry.list[r][c] =(tcry.list[r][c])%26
                tcry.list[r][c] = chr(tcry.list[r][c]+97)
        for i in range(len(t)):
            t[i]= tcry.list[i/key.colonne()][i%key.colonne()]
        te=0
        h=0
        nonfinito=True
        while nonfinito:
            if testocript[te].isalpha():
                testocript[te]=t[h]
                h +=1
                te +=1
            else:
                te +=1
            if h==len(t):
                nonfinito=False
        sentence = ''.join(testocript)
        print sentence


from math import *
def t_erodoto(n):
    if n<2:
        return [1]
    else:
        t_erodoto=range(1,n+1)
        for i in t_erodoto:
            for k in t_erodoto:
                if k<=i or i==1:
                    pass
                else:
                    if k%i==0:
                        t_erodoto.remove(k)
                    else:
                        pass
    return t_erodoto
def test(p):
    s=int(sqrt(p))
    k="si"
    for t in t_erodoto(s):
        if not p%t==0 or t==1:
           pass
        else:
            k="no"
    return k
        
    

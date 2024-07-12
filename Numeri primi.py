import math
def isprimo(n):
    if n==2 or n==3:
        return True
    for d in range(2,int(math.sqrt(n))+1):
        if n%d==0:
            return False
    return True
def primi(n):
    primi=[]
    for p in range(2,n+1):
        if isprimo(p):
            primi+=[p]
    return primi
def pi(n):
    return len(primi(n))

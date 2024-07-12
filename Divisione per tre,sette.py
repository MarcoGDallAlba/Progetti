import random
def Div3(n):
    if n<0:
        n=-n
    t=[0,3,6,9]
    if n<10:
        return n in t
    else:
        n=str(n)
        t=[int(c) for c in n]
        return Div3(sum(t))
def Div7(n):
    if n<0:
        n=-n
    if n<10:
        if n==0 or n==7:
            return True
        elif not(n==0 or n==7):
            return False
    else:
        return Div7(n/10-2*(n%10))
def mcd(x,y):
    if x==0:
        return y
    if y==0:
        return x
    else:
        if x<y:
            return mcd(x,y%x)
        if x>=y:
            return mcd(x%y,y)
        
def prova(b,n):
    x=0
    for u in range(n):
        r=int(random.randint(1,b))
        s=int(random.randint(1,b))
        if mcd(r,s)==1:
            x+=1
    return (float(x)/n)*100

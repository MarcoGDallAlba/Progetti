def Stri(n):
    cont=[o for o in range(0,n)]
    cont[0],cont[1],cont[2]=0,1,1
    for k in range(3,n):
        cont[k]=cont[k-1]+cont[k-2]+cont[k-3]
    i=0
    for c in range(0,n):
        t=cont[c]+i
        i=t
    print i

def Tri(n):
    cont=[o for o in range(0,n)]
    cont[0],cont[1],cont[2]=0,1,1
    for k in range(3,n):
        cont[k]=cont[k-1]+cont[k-2]+cont[k-3]
    print cont[n-1]

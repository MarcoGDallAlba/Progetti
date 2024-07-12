def Trova(d,l):
    return (l in d)

def insertbook(d,l):
    if not(l in d):
        d[l]=1
    else:
        d[l] +=1
def sellbook(d,l):
    if not(l in d):
        print "Esaurito"
    else:
        d[l] -= 1
        print "Vendita effettuata!"
        if d[l]==0:
            del d[l]
def showStore(d):
    for t in d:
        print t, "*"*d[t], d[t]

        

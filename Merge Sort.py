def fusione(q,l):
    s=[]
    i=0
    while len(q)!=0 and len(l)!=0:
        if q[0]<=l[0]:
            s.append(q[0])
            q.remove(q[0])
        else:
            s.append(l[0])
            l.remove(l[0])
    if q==[]:
        return s+l
    if l==[]:
        return s+q
def Merges(l):
    if len(l)==1:
        return l
    if len(l)==2:
        if l[0]<=l[1]:
            return l
        else:
            return l[::-1]
    else:
        return fusione(Merges(l[0:len(l)/2]), Merges(l[len(l)/2:len(l)]))


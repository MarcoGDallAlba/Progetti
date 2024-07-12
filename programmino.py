def trovaeluguali(l):
    cop=[]
    for j in range(0,len(l)):
        eluguali=1
        for p in range(0,len(l)):
            if j==p:
                pass
            else:
                if l[j]==l[p]:
                    eluguali+=1
        if eluguali!=1 and not([l[j],eluguali] in cop):
            cop+=[[l[j],eluguali]]
    return cop

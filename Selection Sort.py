def selection_sort(l):
    for i in range(0,len(l)-1):
        for k in range(i+1,len(l)):
            if l[i]>=l[k]:
                l[i],l[k]=l[k],l[i]
    return l
def insertion_sort(l):
    for i in range(1,len(l)):
        l_i=l[i]
        j=i
        while j>0 and l[j-1]> l_i:
            l[j]=l[j-1]
            j-=1
        l[j]=l_i
    return l
def bubble_sort(l):
    for p in range(0,len(l)-1):
        k,nonfinito=0,True
        while nonfinito:
            if l[k]>l[k+1]:
                l[k],l[k+1]=l[k+1],l[k]
            k+=1
            if k==(len(l)-1-p):
                nonfinito=False
    return l
        

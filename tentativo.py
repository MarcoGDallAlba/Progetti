def get_permutazioni(s,k,n):
    if k==n:
        return [s[:]]
    sols=[]
    A=[i for i in range(n) if i not in s]
    for a in A:
        s.append(a)
        sols += get_permutazioni(s,k+1,n)
        s.pop()
    return sols

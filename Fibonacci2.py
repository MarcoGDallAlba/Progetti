
def seq_fibo(n):
    x=0
    y=1
    print (1,x)
    print (2,y)
    if n>=3:
        for i in range(3,n+1):
            z=x+y
            x = y
            y = z
            print (i,z)
    else:
        a=1
def n_fibo(n):
    x=0
    y=1
    if n==1:
        print x
    if n==2:
        print y
    for i in range(3,n+1):
        z=x+y
        x = y
        y = z
    print z
    
        
    

    
    


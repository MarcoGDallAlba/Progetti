def neve():
    n = int(raw_input("Quanti metri di neve ci sono fuori?:" ))
    if n<2:
        print "bah,una cosuccia"
    elif n>=2 and n<=3:
        print "vai a giocare a palle di neve!"
    elif n>3 and n<=10:
        print "stai a casa per carit�"
    elif n>10 and n<=20:
        print "Ma che �? il finimondo?!"
    else:
        print "Armagheddon...mi dispiace inizia a pregare il tuo dio.. :("

import random
y = random.randint(1, 7)
x= int(raw_input("Facciamo un gioco...io penso a un numero da uno a sette e tu provi a indovinarlo; ti darò due possibilità:"))
if x==y :
    print "Complimenti,hai vinto tu!"
else:
    print "NO!Il tuo numero è "\
          +("maggiore" if x>y else "minore")\
          +" del mio.\n"
    x= int(raw_input("Riprova:"))
    if x==y :
        print "Ora hai indovinato!"
    else :
        print "gen gne gne!!La macchina ha battuto l'uomo!XP. Avevo pensato al numero %d" %y
    
    

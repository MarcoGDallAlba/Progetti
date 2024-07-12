class rubrica:
    def __init__(self,d):
        self.d=d
    def aggiungi(self,nome,numero,anno_nascita,luogo_nascita,via):
        if nome in self.d:
            if [numero,anno_nascita,luogo_nascita,via]==self.d[nome]:
                return "Il contatto è già presente in rubrica"
            else:
                finito=True
                while finito:
                    nome=str(raw_input("Nella rubrica è presente un contatto omonimo; inserisca un altro nome: "))
                    if not(nome in self.d):
                        self.d[nome]=[numero,anno_nascita,luogo_nascita,via]
                        finito=False
        else:
            self.d[nome]=[numero,anno_nascita,luogo_nascita,via]
    def togli(self,nome):
        if nome in self.d:
            del self.d[nome]
        else:
            print "Il contatto inserito, non è presente in rubrica"
    def print_numeri(self):
        numeri=[t for t in self.d]
        for i in range(len(numeri)):
            for j in range(i+1,len(numeri)):
                if numeri[i].lower()>numeri[j].lower():
                    numeri[i],numeri[j]=numeri[j],numeri[i]
        for r in numeri:
            print (r,self.d[r][0]),
    def print_contatti(self):
        numeri=[t for t in self.d]
        for i in range(len(numeri)):
            for j in range(i+1,len(numeri)):
                if numeri[i].lower()>numeri[j].lower():
                    numeri[i],numeri[j]=numeri[j],numeri[i]
        for r in numeri:
            print r
    def modifica_nome(self,nome,nome_nuovo):
        if nome_nuovo in self.d:
            finito=True
            while finito:
                nome_nuovo=str(raw_input("Nella rubrica è presente un contatto omonimo; inserisca un altro nome: "))
                if not(nome_nuovo in self.d):
                    finito=False
                    self.d[nome_nuovo]=self.d[nome]
                    del self.d[nome]
        else:
            self.d[nome_nuovo]=self.d[nome]
            del self.d[nome]
    def modifica_numero(self,nome,numero_nuovo):
        numeri_presenti=[self.d[k][0] for k in self.d]
        finito=True
        while finito:
            if numero_nuovo in numeri_presenti:
                risposta=str(raw_input("Il numero inserito è in possesso di un'altro contatto; procedere comunque alla modifica? "))
                if risposta.lower()=="sì" or risposta.lower()=="si":
                    self.d[nome][0]=numero_nuovo
                    finito=False
                else:
                    nuovo_numero=str(raw_input("Inserisca il nuovo numero: "))
            else:
                finito=False
        if not(self.d[nome][0]==numero_nuovo):
            self.d[nome][0]=numero_nuovo
    

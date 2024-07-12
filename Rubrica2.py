class contatto:
    def __init__(self,nome=None,cognome=None,numero=None,anno_nascita=None,luogo_nascita=None,via=None):
        self.nome=nome
        self.cognome=cognome
        self.numero=numero
        self.anno_nascita=anno_nascita
        self.luogo_nascita=luogo_nascita
        self.via=via
    def modify_nome(self,nome_nuovo):
        self.nome=nome_nuovo
    def modify_numero(self,numero_nuovo):
        self.numero=numero_nuovo
    def modify_cognome(self,cognome_nuovo):
        self.cognome=cognome_nuovo
    def modify_anno(self,anno_nuovo):
        self.anno_nascita=anno_nuovo
    def modify_luogo(self,luogo_nuovo):
        self.luogo_nascita=luogo_nuovo
    def modify_via(self,via_nuovo):
        self.via=via_nuovo
    def print_contatto(self):
        print self.nome,self.cognome,self.numero,self.anno_nascita,self.luogo_nascita,self.via
class rubrica:
    def __init__(self,l):
        self.l=l
    def aggiungi(self,nome,cognome,numero,anno_nascita,luogo_nascita,via):
        self.l.append(contatto(nome,cognome,numero,anno_nascita,luogo_nascita,via))
    def togli(self,nome,cognome=None):
        contatti=[p for p in self.l if p.nome==nome]
        if cognome!=None:
            contatti=[p for p in contatti if p.cognome==cognome]
        for i in range(0,len(contatti)):
            for j in range(i+1,len(contatti)):
                if str(contatti[i].nome)+" "+str(contatti[i].cognome)>str(contatti[j].nome)+" "+str(contatti[j].cognome):
                    contatti[i],contatti[j]=contatti[j],contatti[i]
        if len(contatti)==1:
            self.l.remove(contatti[0])
        else:
            for k in contatti:
                k.print_contatto()
            decisione=int(raw_input("Inserire la posizione del contatto che si vuole cancellare: "))
            self.l.remove(contatti[decisione-1])
    def modifica_contatto(self,nome,cognome=None):
        contatti=[p for p in self.l if p.nome==nome]
        if cognome!=None:
            contatti=[p for p in contatti if p.cognome==cognome]
        for i in range(0,len(contatti)):
            for j in range(i+1,len(contatti)):
                if str(contatti[i].nome)+" "+str(contatti[i].cognome)>str(contatti[j].nome)+" "+str(contatti[j].cognome):
                    contatti[i],contatti[j]=contatti[j],contatti[i]
        if len(contatti)==2:
            dec=int(raw_input("Inserire la posizione del contatto che si vuole modificare: "))
            dec-=1
        if len(contatti)==1:
            dec=0
        d=str(raw_input("Cosa si desidera modificare?:"))
        if d.lower()=="none":
            pass
        else:
            d_nuovo=raw_input("Inserire la nuova informazione: ")
            if d.lower()=="numero":
                contatti[dec].modify_numero(int(d_nuovo))
            if d.lower()=="nome":
                contatti[dec].modify_nome(d_nuovo)
            if d.lower()=="cognome":
                contatti[dec].modify_cognome(d_nuovo)
            if d.lower()=="anno di nascita":
                contatti[dec].modify_anno(int(d_nuovo))
            if d.lower()=="luogo di nascita":
                contatti[dec].modify_luogo(d_nuovo)
            if d.lower()=="via" or d.lower()=="via di abitazione":
                contatti[dec].modify_via(d_nuovo)
    def print_contatti(self):
        contatti=[str(p.nome)+" "+str(p.cognome) if p.cognome!=None else str(p.nome) for p in self.l]
        for i in range(0,len(contatti)):
            for j in range(i+1,len(contatti)):
                if contatti[i]>contatti[j]:
                    contatti[i],contatti[j]=contatti[j],contatti[i]
        for p in contatti:
            print p

    def print_numeri(self):
        s=[p for p in self.l]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                if str(s[i].nome)+" "+str(s[i].cognome)>str(s[j].nome)+" "+str(s[j].cognome):
                    s[i],s[j]=s[j],s[i]
        for p in s:
            print (str(p.nome)+" "+str(p.cognome) if p.cognome!=None else str(p.nome), p.numero)

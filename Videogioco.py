class Stregone:
    def __init__(self,player,life=310,power=120,mana=200,defence=50,arcane=225,resistance=250):
        self.player=player
        self.life=life
        self.power=power
        self.mana=mana
        self.defence=defence
        self.arcane=arcane
        self.resistance=resistance

    def AttaccoFisico(self,other):
        other.life = other.life +((self.power)/10)*(float(other.defence)/600-1)
            
class Demone:
    def __init__(self,player,life=250,power=170,mana=210,defence=100,arcane=175,resistance=150):
        self.player=player
        self.life=life
        self.power=power
        self.mana=mana
        self.defence=defence
        self.arcane=arcane
        self.resistance=resistance
class Guerriero:
    def __init__(self,player,life=210,power=270,mana=60,defence=300,arcane=90,resistance=150):
        self.player=player
        self.life=life
        self.power=power
        self.mana=mana
        self.defence=defence
        self.arcane=arcane
        self.resistance=resistance
class Elfo:
    def __init__(self,player,life=350,power=190,mana=150,defence=70,arcane=175,resistance=180):
        self.player=player
        self.life=life
        self.power=power
        self.mana=mana
        self.defence=defence
        self.arcane=arcane
        self.resistance=resistance
class Nano:
    def __init__(self,player,life=230,power=250,mana=70,defence=300,arcane=100,resistance=130):
        self.player=player
        self.life=life
        self.power=power
        self.mana=mana
        self.defence=defence
        self.arcane=arcane
        self.resistance=resistance
class Angelo:
    def __init__(self,player,life=400,power=250,mana=80,defence=100,arcane=110,resistance=110):
        self.player=player
        self.life=life
        self.power=power
        self.mana=mana
        self.defence=defence
        self.arcane=arcane
        self.resistance=resistance
class Nephilim:
    def __init__(self,player,life=310,power=220,mana=150,defence=90,arcane=130,resistance=130):
        self.player=player
        self.life=life
        self.power=power
        self.mana=mana
        self.defence=defence
        self.arcane=arcane
        self.resistance=resistance
class PANZONE:
    def __init__(self,player,life=50,power=60,mana=10,defence=500,arcane=10,resistance=30):
        self.player=player
        self.life=life
        self.power=power
        self.mana=mana
        self.defence=defence
        self.arcane=arcane
        self.resistance=resistance
        
        
            
        
    
            
            
    

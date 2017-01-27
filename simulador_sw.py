import json
class Unit(object):
    def __init__(self,name,speed,side):
        self.name = name
        self.speed = speed
        self.attack_bar = 0
        self.side = side

    def move(self):
        self.attack_bar += self.speed*7/100

    def add_attack_bar(self,bar):
        self.attack_bar +=bar
        
    def reduce_attack_bar(self,bar):
        self.attack_bar -=bar

    def attack(self):
        self.attack_bar = 0
        print(self.name+" atacou")

    def __repr__(self):
        return json.dumps({"name":self.name,"speed":self.speed,"attack_bar":self.attack_bar})

class Verde(Unit):
    def attack(self):
        self.attack_bar = 0
        print ("verdehile atacou")
        print ("attackbar +20")
        print ("attackbar +20")
        return Action("add_attack_bar",40,"ally")

class Action(object):
    def __init__(self,effect,value,side):
        self.effect= effect
        self.value = value
        self.side = side

    def make(self,units):
        if(self.effect == "add_attack_bar" and self.side == "ally"):
            self.add_attack_bar(self.choose_allies(units),self.value)
        if(self.effect == "reduce_attack_bar" and self.side == "enemy"):
            self.reduce_attack_bar(self.choose_enemies(units),self.value)

    def choose_allies(self,units):
        return [unit for unit in units if unit.side == "ally"]


    def choose_enemies(self,units):
        return [unit for unit in units if unit.side == "enemy"]
    
    def reduce_attack_bar(self,units,bar):
        for unit in units:
            unit.reduce_attack_bar(bar)
    
    def add_attack_bar(self,units,bar):
        for unit in units:
            unit.add_attack_bar(bar)
    

class Game(object):
    def __init__(self,list_units):
        self.list_units = list_units

    def run(self):
        for tick in range(1,24):
            print("tick "+str(tick))
            self.run_tick()

    def run_tick(self):
        for unit in self.list_units:
            unit.move()
        unit_choosed = self.choose_first()
        if(unit_choosed != None):
            action = unit_choosed.attack()
            if(action != None):
                action.make(self.list_units)

    def choose_first(self):
        units_choosed = []
        for unit in self.list_units:
            if unit.attack_bar >= 100:
                units_choosed.append(unit)
        if len(units_choosed) == 0:
            return None
        if len(units_choosed) == 1:
            return units_choosed[0]
        else:
            choosed = units_choosed[0]
            for unit in units_choosed:
                if(unit.attack_bar > choosed.attack_bar):
                    choosed = unit
            return choosed
    

verde = Verde("verdehile",260,"ally")
spectra = Unit("spectra",249.18,"ally")
galleon = Unit("galleon",237.44,"ally")
tarq = Unit("tarq",235,"ally")
perna = Unit("perna",197,"ally")



dragao = Unit("dragon",135,"enemy")
cristal_direito = Unit("cristal_imune",99,"enemy")
cristal_esquerdo = Unit("cristal_dot",135,"enemy")
game = Game([verde,spectra,galleon,tarq,perna,cristal_esquerdo,dragao,cristal_direito])
game.run()

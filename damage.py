class Damage(object):
    def total(attack,multiplier,critdmg,up):
        return attack*multiplier*(1+up+critdmg)

class Defense(object):
    def factor(defense):
        return 1000/(1000+(defense*3))

class Unit(object):
    def __init__(self,hp,defense,attack,skill_multi):
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.skill_multi = skill_multi 

    def receive_damage(self,damage):
        return self.defense.factor()*damage.total()

dmg = Damage.total(1800,5,0.50,0.40)
defense = Defense.factor(2500*0.25)
print(str(dmg))
print(str(defense))
print("received damage:"+str(dmg*(defense)))

for i in range(20):
    print(str(i*100)+" "+str(Defense.factor(i*100)))

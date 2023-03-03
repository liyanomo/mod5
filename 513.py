class war: 
    
    def _init_(self, name, hp, damage, endurance, armor ):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.endurance = endurance
        self.armor = armor
        
    def hit (self, war):
        
        if self.endurance > 10:
            self.damage = 10
        if war.armor > 10:
            war.armor -= 10 
            war.hp -= self.damage
        else:    
            if war.hp < 0:
                print ('{self.name} убил {war.name}')
            else:
                print ('{self.name} атаковал {war.name}')
        return (war.hp, self.endurance)
    
    def protetion (self,war):
        if war.hp -= self.damage:
            war.armor -= 10
        else:
            war.hp -= 0 

from random import randint as rnd
 
war1 = war('каратист', 100, 20, 100,100)
war2 = war('дзюдоист', 100, 20, 100, 100)
wars = [war1, war2]
 
while True:
    if target_hp == 0:
        print(f'"{wars[attack_index].name}" Победил!')
        break
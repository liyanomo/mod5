class war: 
    
    def _init_(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def hit (self, war):
        war.hp -= self.damage
        if war.hp < 0:
            print ('{self.name} убил {war.name}')
        else:
            print ('{self.name} атаковал {war.name}')
        return war.hp
        
from random import randint as rnd
 
war1 = war('каратист', 100, 20)
war2 = war('дзюдоист', 100, 20)
wars = [war1, war2]
 
while True:
    attack_index = rnd(0, 1) #Кто атакует
    target_index = (attack_index + 1)%2 #Кого атакует
    target_hp = wars[attack_index].hit(wars[target_index])
    if target_hp == 0:
        print(f'"{wars[attack_index].name}" Победил!')
        break
        
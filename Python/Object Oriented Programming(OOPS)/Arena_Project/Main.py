from Enemy import Enemy
from Zombie import *
from Orge import *

def battle(e:Enemy):
    e.talk()
    e.attack()


enemy1 = Enemy("ZOmbie")
enemy2 = Zombie(10,20)
enemy3 = Ogre(23,45)
enemy1.type_of_enemy = 'Zombie'

enemy2.talk()

 
enemy2.talk()


# print(f'{enemy2.__type_of_enemy} has {enemy2.__health} health points And can do attack of {enemy2.__damage}')

zombie = Enemy("Zombie",10,1)
zombie.__type_of_enemy = "Zombie"

ogre = Ogre(23,45)
ogre.__type_of_enemy = "Ogre"

print("#####-------------------#####")
print(zombie.get_type_of_enemy())
print(zombie.talk())
battle(zombie)

print("#####-------------------#####")
print(ogre.get_type_of_enemy())
print(ogre.talk())
battle(ogre)


def battle (e1:Enemy, e2:Enemy):
    e1.talk()
    e2.talk()

    while e1.__health_points >0 and e2.__health_points >0:
        e1.special_attack()
        e2.special_attack()
        e2.attack()
        e2.__health_points -= e2.__attack_damage
        e1.attack()

    if e1.__health_points >0:
        print('Enemy 1 WINS!')
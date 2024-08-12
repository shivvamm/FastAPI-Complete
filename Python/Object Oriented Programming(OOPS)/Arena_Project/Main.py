from Enemy import Enemy
from Zombie import *
from Orge import *
from Hero import *
from Weapon import *


def battle(e:Enemy):
    e.talk()
    e.attack()



enemy2 = Zombie(10,20)
enemy3 = Ogre(23,45)

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

    while e1.health_points >0 and e2.health_points >0:
        print("------------")
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP Left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP Left')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage
    print("--------")
 
    if e1.health_points >0:
        print(f'{e1.get_type_of_enemy()} WINS!')
    else:
        print(f'{e2.get_type_of_enemy()} WINS!')

def hero_battle (hero:Hero, enemy:Enemy):

    while hero.health_points >0 and enemy.health_points >0:
        print("------------")
        enemy.special_attack()
        print(f'Hero: {hero.health_points} HP Left')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP Left')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage
    print("--------")
 
    if hero.health_points >0:
        print('Hero WINS!')
    else:
        print(f'{enemy.get_type_of_enemy()} WINS!')





zombie = Zombie(10,2)
ogre = Ogre(20,3)
hero  =Hero(10,1)
weapon = Weapon("Sword", 15)
hero.weapon = weapon
hero.equip_weapon()

battle(zombie,ogre)

print("====== Hero and enemy battle =======")

hero_battle(hero,ogre)
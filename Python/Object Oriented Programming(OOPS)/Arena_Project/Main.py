from Enemy import Enemy

enemy1 = Enemy("ZOmbie")
enemy2 = Enemy("orge",20,5)
enemy1.type_of_enemy = 'Zombie'

enemy1.talk()

enemy1.walk_forward()

enemy1.attack()

print(f'{enemy1.type_of_enemy} has {enemy1.health} health points And can do attack of {enemy1.damage}')
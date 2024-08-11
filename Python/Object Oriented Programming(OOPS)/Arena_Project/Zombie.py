from Enemy import *
import random

class Zombie(Enemy):

    def __init__(self,health_points,attack_damage):

        super().__init__(type_of_enemy='Zombie',health_points=health_points,attack_damage=attack_damage)

        def talk(self):
            print('*Grumbling...*') # Method Overriding
        
        def spread_disease(self):
            print("THe zombie is trying to spread infection")
            #New Zombieonly Mehtod

        def special_attack(self):
            did_special_attack_work = random.random() < 0.50
            if did_special_attack_work:
                self.health_points +=2
                print("ZOmbie regenrated 2 HP! ")
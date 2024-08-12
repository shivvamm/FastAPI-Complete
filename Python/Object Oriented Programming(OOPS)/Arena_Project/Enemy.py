class Enemy:
    def __init__(self,type_of_enemy,health_points,attack_damage):
        # Encapsulation using __ to make the data memebers private as it is public 
        # By default 
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print("I am an Enemy")
    
    def attack(self):
        print(f'{self.__type_of_enemy} attacks you for {self.attack_damage} damage')

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you')

    def special_attack(self):
        print('Enemy has not special attack')








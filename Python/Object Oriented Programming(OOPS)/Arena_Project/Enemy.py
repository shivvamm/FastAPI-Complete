class Enemy:
    def __init__(self,type_of_enemy,health=10,damage=1):
        self.type_of_enemy = type
        self.health = health
        self.damage = damage

    def talk(self):
        print("I am an enemy")

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you')
    
    def attack(self):
        print(f'{self.type_of_enemy} attacks you for {self.damage} damage')
class Player:
    def __init__(self, health = 100, energy = 100): # constructor
        self.health = health
        self.energy = energy
        print("Player created")

    def attack(self, monster, damage = 40):
        monster.health -= damage
        self.energy -= damage
        print(f"Player attack to monster, damage = {damage}")
        if monster.is_attacked():
            self.health -= monster.damage

    def show_info(self):
        print(f"Health player = {self.health}")
        print(f"Energy Player = {self.energy}")

class Monster:
    def __init__(self, health = 100):
        self.health = health
        self.init_health = self.health
        self.damage = 10
        print("Monster Created!")

    def is_attacked(self):
        print(f"Monster attack to player, damage = {self.damage}")
        return self.health < self.init_health

    def show_info(self):
        print(f"Health Monster = {self.health}")

player = Player()
monster = Monster()

player.attack(monster)
player.attack(monster, damage = 20)
player.attack(monster, damage = 10)
player.attack(monster, damage = 15)

monster.show_info()
player.show_info()
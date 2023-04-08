class Character(object):
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage, hp):
        damage_taken = hp - damage
        return damage_taken

class Enemy(Character):
    def __init__(self, encounter_message):
        self.encounter_message = encounter_message
        super().__init__(self)

player_name = "Onye" # Var for now, it will be prompted for Name from user.

player = Character(player_name, 100, 10)

enemies = []

enemy1 = Enemy("Slime", 40, 2, "encounter message")

#enemy2 = Enemy("Skeleton", 60, 10)
#enemy3 = Enemy("Zombie", 80, 15)

#enemies.append(enemy1)
#enemies.append(enemy2)
#enemies.append(enemy3)

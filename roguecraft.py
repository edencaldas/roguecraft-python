import random


class Character:
    def __init__(self, name, health, power, attack1_name, attack2_name, attack3_name,
                 attack1_damage, attack2_damage, attack3_damage,
                 is_alive, attack1_message, attack2_message, attack3_message):
        self.name = name
        self.health = health
        self.power = power
        self.attack1_name = attack1_name
        self.attack2_name = attack2_name
        self.attack3_name = attack3_name
        self.attack1_damage = attack1_damage
        self.attack2_damage = attack2_damage
        self.attack3_damage = attack3_damage
        self.is_alive = is_alive
        self.attack1_message = attack1_message
        self.attack2_message = attack2_message
        self.attack3_message = attack3_message

    def attack(self, target_health, target_name, random_attack_selection):
        attack_messages = [self.attack1_message, self.attack2_message, self.attack3_message]
        attack_damages = [self.attack1_damage, self.attack2_damage, self.attack3_damage]
        attack_names = [self.attack1_name, self.attack2_name, self.attack3_name]
        attack = random_attack_selection  # select the attack
        damage = self.power + attack_damages[attack]
        health_left = target_health - damage

        print(f"{self.name} {attack_messages[attack]} for {damage} damage!")
        if health_left > 0:
            print(f"{target_name} has {health_left} health left!")

        print("")
        return health_left


player_name = input("Hi. Welcome to the adventures of roguecraft. May I please know your name?: ")
print("")
print("=== Game Start ===")
print("")

player = Character(player_name, 100, 5, "Punch", "Wooden Axe", "Diamond Sword", 10, 20, 30, True, "punches",
                   "attacks with a wooden axe, chop chop", "gracefully attacks with a Diamond Sword")

zombie = Character("Zombie", 100, 5, "Slash", "Puke", "Bite", 5, 8, 25, True, "slashes at you", "pukes acid on you",
                   "bites you, delish")

skeleton = Character("Skeleton", 100, 5, "Kick", "club", "throw", 5, 8, 25, True, "kicks you on the private parts",
                     "hits you with a club", "throws club at you")

battle_message = [
    "You stumble upon",
    "It's a trap! You are surprised by",
    "You encounter",
    "While bing chilling, you are suddenly attacked by",
    "You spot an enemy, you get closer and find",
    "You feel something is following you. You turn around and see",
    "An enemy appears! It's a"]

characters = [zombie, skeleton]

player1 = player

for enemies in characters:
    enemy = enemies
    random_index = random.randint(0, 6)
    print(f"{battle_message[random_index]} {enemy.name}!")

    while True:
        random_attack = random.randint(0, 2)
        enemy.health = player1.attack(enemy.health, enemy.name, random_attack)
        if enemy.health <= 0:
            print(f"{player1.name} defeats {enemy.name}!\n")
            break

        player1.health = enemy.attack(player1.health, player1.name, random_attack)
        if player1.health <= 0:
            print("You have no health left.")
            print(f"{enemy.name} has defeated you! Game Over!")
            break

if (player1.health > 0):
    print("Congratulations! You've defeated all enemies!")
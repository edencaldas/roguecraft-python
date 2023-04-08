import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0

class Enemy(Character):
    def __init__(self, name, health, attack, next_enemy=None):
        super().__init__(name, health, attack)
        self.next_enemy = next_enemy

# Initialize player and enemy characters
player = Character("Player", 100, 20)

enemy1 = Enemy("Goblin", 110, 22)
enemy2 = Enemy("Orc", 120, 24)
enemy3 = Enemy("Troll", 130, 26)
enemy4 = Enemy("Ogre", 140, 28)
enemy5 = Enemy("Giant", 150, 30)
enemy6 = Enemy("Dragon", 160, 32)
enemy7 = Enemy("Demon", 170, 34)
enemy8 = Enemy("Chimera", 180, 36)
enemy9 = Enemy("Hydra", 190, 38)
enemy10 = Enemy("Behemoth", 200, 40)

# Link enemies together
enemies = enemy1
enemies.next_enemy = enemy2
enemy2.next_enemy = enemy3
enemy3.next_enemy = enemy4
enemy4.next_enemy = enemy5
enemy5.next_enemy = enemy6
enemy6.next_enemy = enemy7
enemy7.next_enemy = enemy8
enemy8.next_enemy = enemy9
enemy9.next_enemy = enemy10

def battle(player, enemy):
    while not player.is_dead() and not enemy.is_dead():
        # Player's turn
        enemy.take_damage(player.attack)
        print(f"{player.name} attacked {enemy.name} for {player.attack} damage! {enemy.name}'s remaining health: {enemy.health}")

        if enemy.is_dead():
            print(f"{enemy.name} has been defeated!")
            break

        # Enemy's turn
        player.take_damage(enemy.attack)
        print(f"{enemy.name} attacked {player.name} for {enemy.attack} damage! {player.name}'s remaining health: {player.health}")

        if player.is_dead():
            print(f"{player.name} has been defeated!")
            break

# Main game loop
current_enemy = enemies
battle_number = 1
while current_enemy is not None:
    if player.is_dead():
        break

    print(f"nBattle {battle_number}: {player.name} vs {current_enemy.name}")
    battle(player, current_enemy)
    current_enemy = current_enemy.next_enemy
    battle_number += 1

if player.is_dead():
    print("nYou have been defeated! Better luck next time.")
else:
    print("nCongratulations! You have defeated all enemies!")
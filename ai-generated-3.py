# Define the player character class
class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    # Define the attack method for the player character
    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.health -= damage
            print(f"{self.name} attacked {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack had no effect on {enemy.name}!")

    # Define the defend method for the player character
    def defend(self):
        print(f"{self.name} is defending and takes reduced damage!")
        self.defense += 5

# Define the enemy character class
class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    # Define the attack method for the enemy character
    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage > 0:
            player.health -= damage
            print(f"{self.name} attacked {player.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack had no effect on {player.name}!")

# Define the combat function that will be called for each enemy encounter
def combat(player, enemy):
    # Print the current status of the player and enemy
    print(f"{player.name}: {player.health} HP | {enemy.name}: {enemy.health} HP")

    # Ask the player what action they want to take (attack or defend)
    action = input("What do you want to do? (attack/defend) ").lower()

    # If the player chooses to attack, call the attack method for the player and enemy
    if action == "attack":
        player.attack_enemy(enemy)
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            return True
        enemy.attack_player(player)
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            return False

    # If the player chooses to defend, call the defend method for the player and skip the enemy's turn
    elif action == "defend":
        player.defend()
        enemy.attack_player(player)
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            return False

    # If the player enters an invalid action, prompt them to try again
    else:
        print("Invalid action. Try again.")
        combat(player, enemy)

    # If neither the player nor the enemy has been defeated, call the combat function again for the next round
    combat(player, enemy)

# Define the main function that will run the game
def main():
    # Create a player character and a list of enemy characters
    player = Player("Player", 100, 20, 10)
    enemies = [
        Enemy("Enemy 1", 50, 10, 5),
        Enemy("Enemy 2", 75, 15, 7), Enemy("Enemy 3", 100, 20, 10),
        Enemy("Enemy 4", 125, 25, 12), Enemy("Enemy 5", 150, 30, 15), Enemy("Enemy 6", 175, 35, 17),
        Enemy("Enemy 7", 200, 40, 20), Enemy("Enemy 8", 225, 45, 22), Enemy("Enemy 9", 250, 50, 25),
        Enemy("Enemy 10", 300, 60, 30)]

    # Loop through each enemy in the list and call the combat function for each encounter
    for enemy in enemies:
        print(f"You are now facing {enemy.name}!")
        if combat(player, enemy):
            print(f"You have defeated {enemy.name}!")
        else:
            print("Game over.")
            break

# Call the main function to start the game
main()
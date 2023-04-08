class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_opponent(self, opponent):
        opponent.health -= self.attack

player = Character("Player", 100, 25)

# Create a list of 10 distinct enemy characters
enemies = [Character(f"Enemy{i + 1}", 100 + i * 10, 20 + i * 2) for i in range(10)]

# Loop through each enemy in the enemies list
for enemy in enemies:
    print(f"Starting battle with {enemy.name}")

    # Fight the current enemy until either player or enemy has no health remaining
    while player.health > 0 and enemy.health > 0:
        player.attack_opponent(enemy)
        print(f"{player.name} attacks {enemy.name}! {enemy.name} has {enemy.health} health remaining.")

        if enemy.health <= 0:
            print(f"{player.name} defeats {enemy.name}!")
            break

        enemy.attack_opponent(player)
        print(f"{enemy.name} attacks {player.name}! {player.name} has {player.health} health remaining.")

        if player.health <= 0:
            print(f"Game over. {enemy.name} wins!")
            break

    # If the player health is less than or equal to 0, stop the game
    if player.health <= 0:
        break

# If the player defeated all enemies, print a victory message
if player.health > 0:
    print("Congratulations! You've defeated all enemies!")
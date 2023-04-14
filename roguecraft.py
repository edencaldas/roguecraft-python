import my_ascii_art
import random
import os


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

    def attack(self, target_health, target_name):
        attack_messages = [self.attack1_message, self.attack2_message, self.attack3_message]
        attack_damages = [self.attack1_damage, self.attack2_damage, self.attack3_damage]
        attack_names = [self.attack1_name, self.attack2_name, self.attack3_name]
        attack = random.randint(0, 2)  # select the attack
        damage = self.power + attack_damages[attack]
        health_left = target_health - damage

        print(f"{self.name} {attack_messages[attack]} for {damage} damage!")
        if health_left > 0:
            print(f"{target_name} has {health_left} health left!")
        else:
            print("You have no health left.")

        print("")
        return health_left


class Player(Character):
    level = 1

    def attack(self, target_health, target_name):
        attack_messages = [self.attack1_message, self.attack2_message, self.attack3_message]
        attack_damages = [self.attack1_damage, self.attack2_damage, self.attack3_damage]
        attack_names = [self.attack1_name, self.attack2_name, self.attack3_name]
        # attack = random.randint(0, 2)  # select the attack

        number = 0
        for n in attack_names:
            number += 1
            print(number, n)

        attack_choice = ""

        while type(attack_choice) is not int:
            try:
                attack_choice = int(input("\nWhich skill will you choose to attack with? "))
            except ValueError:
                print("Inform the number of the skill.")
                continue
            # else:
            #     break

        if attack_choice not in range(1, 4):
            print(my_ascii_art.art_list[0])
            print("\nYou got confused when deciding on a skill to use, and farted instead. This effect has healed the "
                  "enemy!\n")
            return 100  # heals enemy
        else:
            damage = self.power + attack_damages[attack_choice - 1]
            health_left = target_health - damage
            print(f"\n{self.name} {attack_messages[attack_choice - 1]} for {damage} damage!")

            if health_left > 0:
                print(f"{target_name} has {health_left} health left!")

            print("")
            return health_left

    def levelup(self):
        self.health = self.health + (self.level * 10)
        self.power = self.power + (self.level * 2)

    def rest(self, starting_health):
        self.health = starting_health


def choose_at_bonfire():
    bonfire_choice = ""
    if encounter_number % 3 == 0:
        print(f"After the battle, {player_name} decides to make a boomfire and ponder about his next move.")
        print()
        print("1 - Reflect on your last battles.\n"
              "2 - Take this time to enjoy your hard earned rest.")
        choice = input(int("Choose: "))
        if choice == 1:
            bonfire_choice = "rest"
        elif choice == 2:
            bonfire_choice = "levelup"
        else:
            print(f"{player_name} did not choose what to do, fell asleep on the ground, skipping the opportunity.")
            bonfire_choice = "skip"

        return bonfire_choice



def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


try:
    player_name = input("Hi. Welcome to the adventures of roguecraft. May I please know your name?: ")
except KeyboardInterrupt:
    print("\n\nExiting...")
    exit(0)

print("")
print("=== Game Start ===")
print("")

player = Player(player_name, 500, 5, "Punch", "Wooden Axe", "Diamond Sword", 10, 20, 30, True, "punches",
                "attacks with a wooden axe, chop chop", "gracefully attacks with a Diamond Sword")

slime = Character("Slime", 60, 5, "Spit", "Bounce", "Explode", 5, 8, 25, True, "spits on you",
                  "bounces on top of your head", "explodes")

zombie = Character("Zombie", 100, 5, "Slash", "Puke", "Bite", 15, 20, 30, True, "slashes at you", "pukes acid on you",
                   "bites you, delish")

skeleton = Character("Skeleton", 110, 5, "Kick", "club", "throw", 20, 25, 35, True, "kicks you on the private parts",
                     "hits you with a club", "throws club at you")

fishman = Character("Fishman", 120, 5, "Poke", "Poison", "Impale", 20, 30, 40, True, "pokes you with the trident",
                    "casts poison cloud", "leaps at you and impales you from the back")

bear = Character("Bear", 200, 5, "Claw", "Maul", "Hug", 20, 30, 40, True, "claws your face",
                 "mauls you", "gives you a bear hug")

goblin_wizard = Character("Goblin Wizard", 120, 5, "Staff", "Lighting Bolt", "Rock Golem", 20, 30, 40, True,
                          "hits you with his staff", "casts Lighting bolt", "summons a Rock Golem, which hits you")

battle_message = [
    "You stumble upon",
    "It's a trap! You are surprised by",
    "You encounter",
    "While bing chilling, you are suddenly attacked by",
    "You spot an enemy, you get closer and find",
    "You feel something is following you. You turn around and see",
    "An enemy appears! It's a"]

characters = [slime, zombie, skeleton, fishman, bear, goblin_wizard]

player1 = player
game_over = False

for enemies in characters:

    if game_over:
        break

    enemy = enemies
    encounter_number = characters.index(enemy) + 1
    choose_at_bonfire()
    random_battle_message = random.choice(battle_message)

    clear()
    print(f"# {encounter_number}\n{random_battle_message} {enemy.name}!\n")
    print(my_ascii_art.art_list[encounter_number])

    while player1.health >= 1:

        try:
            enemy.health = player1.attack(enemy.health, enemy.name)
            if enemy.health <= 0:
                print(f"{player1.name} defeats {enemy.name}!\n")
                break

            player1.health = enemy.attack(player1.health, player1.name)
            if player1.health <= 0:
                print(f"{enemy.name} has defeated you!")
                game_over = True
                break

        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)

if player1.health > 0:
    clear()
    print("Congratulations! You have defeated all enemies from the Lands of Roguecraft!\nVictory has been achieved!")
    print()
    print(f"The great warrior {player1.name} will be forever remembered by the citizens of Nobutown.")

if player1.health <= 0:
    print("Game Over!")

exit(0)

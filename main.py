import random
import sys

# --- Character Classes ---
classes = {
    "Warrior": {"Strength": 8, "Agility": 5, "Magic": 2, "Health": 30},
    "Mage": {"Strength": 3, "Agility": 4, "Magic": 9, "Health": 20},
    "Rogue": {"Strength": 5, "Agility": 8, "Magic": 4, "Health": 25}
}

inventory = []

# --- Helper Functions ---
def safe_input(prompt, valid_choices):
    while True:
        choice = input(prompt).capitalize().strip()
        if choice in valid_choices:
            return choice
        else:
            print("That's not a valid command. Try again.")

def dice_roll():
    return random.randint(1, 6)

# --- Character Creation ---
print("Welcome to the Realm of Shadows!")
print("Choose your class:")
for c in classes:
    print(f"- {c}: {classes[c]}")

player_class = safe_input("Enter your class (Warrior/Mage/Rogue): ", classes.keys())
player_stats = classes[player_class].copy()
print(f"\nYou are a {player_class} with stats: {player_stats}\n")

# --- Story Progression ---
def haunted_forest():
    print("\n🌲 You enter the Haunted Forest. Mist surrounds you.")
    choice = safe_input("A shadow appears! Do you 'Attack' or 'Befriend' it? ", ["Attack", "Befriend"])

    if choice == "Attack":
        result = combat("Ghost", 15, 5)
        if result:
            inventory.append("Ghostly Amulet")
            print("You obtained a Ghostly Amulet!")
            enchanted_castle()
        else:
            bad_ending("The ghost drains your soul. You perish.")
    else:
        print("The ghost bows and grants you a protective blessing!")
        player_stats["Magic"] += 2
        enchanted_castle()

def enchanted_castle():
    print("\n🏰 You reach the Enchanted Castle. The air crackles with energy.")
    choice = safe_input("Do you 'Search' the library or 'Climb' the tower? ", ["Search", "Climb"])

    if choice == "Search":
        print("You find a dusty tome and learn a new spell!")
        inventory.append("Fireball Scroll")
        player_stats["Magic"] += 3
    else:
        print("A wyvern attacks from above!")
        result = combat("Wyvern", 20, 7)
        if not result:
            bad_ending("The wyvern burns you to ash.")
            return
        inventory.append("Wyvern Scale Shield")

    bandits_lair()

def bandits_lair():
    print("\n🏜️ You arrive at the Bandit’s Lair, the final stage of your journey.")
    choice = safe_input("Do you 'Sneak' in or 'Charge' in? ", ["Sneak", "Charge"])

    if choice == "Sneak":
        if "Ghostly Amulet" in inventory:
            good_ending("The ghost's blessing hides you! You steal the treasure unseen.")
        else:
            bad_ending("You trip an alarm and are captured by the bandits.")
    else:
        result = combat("Bandit King", 25, 8)
        if result:
            great_ending("You defeat the Bandit King and unite the realm!")
        else:
            bad_ending("The Bandit King strikes you down...")

# --- Combat System ---
def combat(enemy_name, enemy_health, enemy_attack):
    print(f"\n⚔️ Combat begins with {enemy_name}!")
    while enemy_health > 0 and player_stats["Health"] > 0:
        print(f"\nYour Health: {player_stats['Health']} | {enemy_name}'s Health: {enemy_health}")
        action = safe_input("Choose: Attack / Defend / Use Magic ", ["Attack", "Defend", "Use magic"])

        roll = dice_roll()
        if action == "Attack":
            dmg = player_stats["Strength"] + roll - 2
            print(f"You strike for {dmg} damage!")
            enemy_health -= dmg
        elif action == "Defend":
            print("You brace for impact, reducing incoming damage.")
            dmg = max(0, enemy_attack - (player_stats["Agility"] // 2))
            player_stats["Health"] -= dmg
            print(f"You take {dmg} damage.")
            continue
        elif action == "Use magic":
            if player_stats["Magic"] < 3:
                print("Your magic is too weak!")
            else:
                dmg = player_stats["Magic"] + roll
                print(f"You cast a spell for {dmg} damage!")
                enemy_health -= dmg
                player_stats["Magic"] -= 1

        # Enemy counterattack
        if enemy_health > 0:
            dmg = max(1, enemy_attack - (player_stats["Agility"] // 3))
            print(f"{enemy_name} attacks for {dmg} damage!")
            player_stats["Health"] -= dmg

    if player_stats["Health"] <= 0:
        return False
    print(f"{enemy_name} defeated!")
    return True

# --- Endings ---
def good_ending(text):
    print(f"\n✨ GOOD ENDING: {text}")
    print("You have restored peace to the land!")
    sys.exit()

def great_ending(text):
    print(f"\n🏆 GREAT ENDING: {text}")
    print("Legends will speak of your courage forever.")
    sys.exit()

def bad_ending(text):
    print(f"\n💀 BAD ENDING: {text}")
    print("Your journey ends here.")
    sys.exit()

# --- Start the Game ---
print("Your journey begins...\n")
haunted_forest()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

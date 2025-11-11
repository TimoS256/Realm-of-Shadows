import random
import sys

# --- Character Classes ---
classes = {
    "Warrior": {"Strength": 8, "Agility": 5, "Magic": 2, "Health": 30},
    "Mage": {"Strength": 3, "Agility": 4, "Magic": 9, "Health": 20},
    "Rogue": {"Strength": 5, "Agility": 8, "Magic": 4, "Health": 25},
    "Summoner": {"Strength": 4, "Agility": 4, "Magic": 8, "Health": 22, "Skeletons": 2}
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

player_class = safe_input("Enter your class (Warrior/Mage/Rogue/Summoner): ", classes.keys())
player_stats = classes[player_class].copy()
print(f"\nYou are a {player_class} with stats: {player_stats}\n")

# --- Story Progression ---
def haunted_forest():
    print("\n🌲 You enter the Haunted Forest. Mist surrounds you.")
    choice = safe_input("A shadow appears! Do you 'Attack' or 'Befriend' it? ", ["Attack", "Befriend"])

    if choice == "Attack":
        result = combat(["Ghost"])
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
        print("A pair of wyverns descend from the tower!")
        result = combat(["Wyvern", "Wyvern"])
        if not result:
            bad_ending("The wyverns tear you apart.")
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
        print("The Bandit King and his two guards step forward to fight!")
        result = combat(["Bandit King", "Bandit Guard", "Bandit Guard"])
        if result:
            great_ending("You defeat the Bandit King and unite the realm!")
        else:
            bad_ending("The Bandit King strikes you down...")

# --- Combat System (Multi-Enemy + Summoner Support) ---
def combat(enemies):
    print(f"\n⚔️ Combat begins! You face: {', '.join(enemies)}")

    # Initialize enemy stats dynamically
    enemy_data = []
    for e in enemies:
        base_health = random.randint(10, 20)
        base_attack = random.randint(4, 8)
        enemy_data.append({"Name": e, "Health": base_health, "Attack": base_attack})

    skeletons = player_stats.get("Skeletons", 0)
    skeleton_health = 10  # each skeleton's health

    while player_stats["Health"] > 0 and any(e["Health"] > 0 for e in enemy_data):
        print(f"\nYour Health: {player_stats['Health']}")
        if skeletons > 0:
            print(f"💀 Skeletons: {skeletons} (each {skeleton_health} HP)")
        print("Enemies:")
        for e in enemy_data:
            print(f"  - {e['Name']}: {max(e['Health'], 0)} HP")

        action = safe_input("Choose: Attack / Defend / Use Magic ", ["Attack", "Defend", "Use magic"])
        defend_bonus = 0
        roll = dice_roll()

        # --- Player Action ---
        if action == "Attack":
            alive_enemies = [e for e in enemy_data if e["Health"] > 0]
            if alive_enemies:
                target = random.choice(alive_enemies)
                dmg = player_stats["Strength"] + roll
                print(f"You strike {target['Name']} for {dmg} damage!")
                target["Health"] -= dmg
        elif action == "Defend":
            print("You brace for incoming attacks, reducing damage.")
            defend_bonus = player_stats["Agility"] // 2
        elif action == "Use magic":
            if player_class == "Summoner":
                print("You summon reanimated skeletons to fight!")
                skeletons += 1
            elif "Fireball Scroll" in inventory:
                print("🔥 You unleash a Fireball, burning all enemies!")
                for e in enemy_data:
                    dmg = player_stats["Magic"] + roll
                    e["Health"] -= dmg
                    print(f"{e['Name']} takes {dmg} damage!")
                inventory.remove("Fireball Scroll")
            elif player_stats["Magic"] < 3:
                print("Your magic is too weak!")
            else:
                alive_enemies = [e for e in enemy_data if e["Health"] > 0]
                if alive_enemies:
                    target = random.choice(alive_enemies)
                    dmg = player_stats["Magic"] + roll
                    print(f"You cast a spell for {dmg} damage on {target['Name']}!")
                    target["Health"] -= dmg
                    player_stats["Magic"] -= 1

        # --- Skeleton Attacks ---
        if skeletons > 0:
            for i in range(skeletons):
                alive_enemies = [e for e in enemy_data if e["Health"] > 0]
                if not alive_enemies:
                    break  # stop attacking if all enemies are dead
                target = random.choice(alive_enemies)
                dmg = random.randint(3, 6)
                print(f"💀 Skeleton attacks {target['Name']} for {dmg} damage!")
                target["Health"] -= dmg

        # --- Enemies Attack ---
        for e in enemy_data:
            if e["Health"] > 0:
                dmg = e["Attack"] - (player_stats["Agility"] // 4)
                if action == "Defend":
                    dmg = max(0, dmg - defend_bonus)

                # Skeletons may absorb hits
                if skeletons > 0 and random.random() < 0.4:
                    print(f"{e['Name']} attacks a skeleton instead!")
                    skeleton_health -= dmg
                    if skeleton_health <= 0:
                        skeletons -= 1
                        skeleton_health = 10
                        print("💀 A skeleton crumbles to dust!")
                else:
                    print(f"{e['Name']} attacks you for {dmg} damage!")
                    player_stats["Health"] -= dmg

        # Cleanup dead enemies (for clarity)
        enemy_data = [e for e in enemy_data if e["Health"] > 0 or e["Health"] <= 0]

    if player_stats["Health"] <= 0:
        return False
    print("You are victorious!")
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

# 🧙 Realm of Shadows — A Text-Based Role-Playing Game

**Realm of Shadows** is a text-based RPG adventure built in Python.  
Players create a character, explore dangerous lands, engage in **multi-enemy turn-based battles**, collect items, and shape their destiny through branching storylines and multiple endings.

---

## 🎮 Features

### ⚔️ Character Creation
- Choose from **Warrior**, **Mage**, **Rogue**, or the new **Summoner** class.
- Each class has unique stats and special mechanics that affect combat and story choices.
- Stats include: **Strength**, **Agility**, **Magic**, and **Health** (Summoner also uses **Skeletons**).

### 🌍 World and Story Progression
- Multi-stage storyline across three key locations:
  1. **Haunted Forest** 🌲  
  2. **Enchanted Castle** 🏰  
  3. **Bandit’s Lair** 🏜️  
- Each area features unique encounters, branching decisions, and rewards that influence your journey.

### ⚔️ Turn-Based Multi-Enemy Combat System
- Classic **turn-based** battle mechanics with random dice rolls.
- Players can now face **multiple enemies at once** (e.g., two Wyverns or a Bandit King with guards).
- Choose between **Attack**, **Defend**, or **Use Magic** actions.
- Enemies vary in difficulty, health, and attack power.
- Skeletons and summoned allies now join combat automatically.
- Random dice-roll mechanics ensure combat stays unpredictable and tense.

### 💀 Summoner Class (New!)
- A powerful new class specializing in **necromancy** and **summoning skeletons** to fight alongside you.
- Starts with **2 skeletons** that act as allies in battle.
- Can **summon additional skeletons** during combat using the “Use Magic” command.
- Skeletons attack enemies automatically and can absorb hits on the player’s behalf.
- Skeletons have their own HP and can crumble in battle if defeated.

### 🎒 Inventory and Items
- Collect items like **potions**, **magical scrolls**, and **artifacts**.
- Items like the *Fireball Scroll* can deal area damage to all enemies.
- Manage inventory to view, use, or discard items.

### 🌟 Branching Choices & Multiple Endings
- Your decisions shape the story and determine your fate.
- Example: Befriend the ghost or attack it — each leads to a unique outcome.
- Includes **three distinct endings** based on player performance:
  - 🏆 Great Ending  
  - ✨ Good Ending  
  - 💀 Bad Ending  

### ⚙️ Error Handling
- Gracefully manages invalid or unexpected inputs (e.g., `"That's not a valid command."`)
- Handles edge cases like empty inventory or zero health without breaking gameplay.

---

## 🧩 Requirements

- **Python 3.8+**  
- No external libraries required (uses only built-in modules like `random` and `sys`).

---

## 🚀 How to Play

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/realm-of-shadows.git
   cd realm-of-shadows
2. **Run the Command**
    python3 realm_of_shadows.py
3. **Follow on-screen instructions:**
    - Choose your class.
    - Make story-altering choices. 
    - Engage in multi-enemy battles. 
    - Survive, summon, and shape your destiny!
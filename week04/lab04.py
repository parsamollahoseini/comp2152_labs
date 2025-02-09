import random

# Step 1: Define Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Step 2: Roll for Monster's Magic Power
input("Press Enter to roll for the monster's magic power...")
selected_power = random.choice(list(monster_powers.keys()))
print(f"Monster rolled: {selected_power}")

# Step 3: Update Monster's Combat Strength
m_combat_strength = 3  # Initial combat strength (Example value)
m_combat_strength = min(m_combat_strength + monster_powers[selected_power], 6)
print(f"Updated Monster's Combat Strength: {m_combat_strength}")

# Step 4: Loot System
loot_options = ["Potion", "Dagger", "Shield", "Poison", "Magic Scroll"]
belt = []

good_loot_options = ["Potion", "Shield"]
bad_loot_options = ["Poison"]
health_points = 4  # Example initial health value

print("You have found a loot bag!")

# Function to collect loot
def collect_loot():
    input("Press Enter to roll for a loot item...")
    if loot_options:
        loot_item = random.choice(loot_options)
        loot_options.remove(loot_item)
        belt.append(loot_item)
        print(f"You received: {loot_item}")
        print(f"Current belt items: {belt}")
    else:
        print("No more loot available!")

# Collect first and second loot item
collect_loot()
collect_loot()

# Step 5: Organizing the Belt
print("Organizing the belt alphabetically...")
belt.sort()
print(f"Organized belt: {belt}")

# Step 6: Use First Loot Item
if belt:
    input("Press Enter to use the first item in your belt...")
    used_loot = belt.pop(0)
    print(f"You used: {used_loot}")

    # Step 7: Check the effect of the loot on health
    if used_loot in good_loot_options:
        health_points = min(health_points + 2, 6)
        print("The item helped you! Health increased.")
    elif used_loot in bad_loot_options:
        health_points = max(health_points - 2, 0)
        print("The item was harmful! Health decreased.")
    else:
        print("The item had no effect.")

    print(f"Player's updated health points: {health_points}")
else:
    print("No items in the belt to use.")

# Step 8: Fight Mechanics
# Import the random library to use for the dice later

# Hero's Attack Functions
def hero_attacks(combat_strength, m_health_points):
    print("Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("You have reduced the monster's health to " + str(m_health_points))
    return m_health_points

# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    print("Monster's Claw (" + str(m_combat_strength) + ") ---> Hero (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("You have killed the monster")
    else:
        health_points -= m_combat_strength
        print("The monster has reduced your health to " + str(health_points))
    return health_points

# Define The number of lives for the Hero and Monster
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Define the Dice
diceOptions = list(range(1, 7))
# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Print out the weapons using a for loop
for weapon in weapons:
    print(weapon)

# Define the number of stars awarded to the Player
num_stars = 0

# Use a While Loop to get valid input for Hero and Monster's Combat Strength
i = 0
while i in range(5):
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        print("One or more invalid inputs. Player needs to enter integer numbers for Combat Strength")
        i = i + 1
        continue

    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue
    else:
        break

combat_strength = int(combat_strength)
m_combat_strength = int(m_combat_strength)

input("Roll the dice for your weapon (Press enter)")
weaponRoll = random.choice(diceOptions)
combat_strength = min(6, (combat_strength + weaponRoll))
print("The hero's weapon is " + str(weapons[weaponRoll - 1]))

input("Analyze the Weapon roll (Press enter)")
if weaponRoll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

if weapons[weaponRoll - 1] != "Fist":
    print("--- Thank goodness you didn't roll the Fist...")

print("You meet the monster. FIGHT!!")
while m_health_points > 0 and health_points > 0:
    input("You strike first (Press Enter)")
    m_health_points = hero_attacks(combat_strength, m_health_points)
    if m_health_points == 0:
        num_stars = 3
    else:
        input("The monster strikes (Press Enter)")
        health_points = monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
        else:
            num_stars = 2

stars = "*" * num_stars
print("Hero gets <" + stars + "> stars")

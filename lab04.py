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

print("You have found a loot bag!")

# Collect first loot item
input("Press Enter to roll for your first loot item...")
first_loot = random.choice(loot_options)
loot_options.remove(first_loot)
belt.append(first_loot)
print(f"You received: {first_loot}")
print(f"Current belt items: {belt}")

# Collect second loot item
input("Press Enter to roll for your second loot item...")
second_loot = random.choice(loot_options)
loot_options.remove(second_loot)
belt.append(second_loot)
print(f"You received: {second_loot}")
print(f"Current belt items: {belt}")

# Step 5: Organizing the Belt
print("Organizing the belt alphabetically...")
belt.sort()
print(f"Organized belt: {belt}")

# Step 6: Use First Loot Item
input("Press Enter to use the first item in your belt...")
used_loot = belt.pop(0)
print(f"You used: {used_loot}")

# Step 7: Check the effect of the loot on health
health_points = 4  # Example initial health value
good_loot = ["Potion", "Shield"]
bad_loot = ["Poison"]

if used_loot in good_loot:
    health_points = min(health_points + 2, 6)
    print("The item helped you! Health increased.")
elif used_loot in bad_loot:
    health_points = max(health_points - 2, 0)
    print("The item was harmful! Health decreased.")
else:
    print("The item had no effect.")

print(f"Player's updated health points: {health_points}")

import random
import functions_lab05

# ---------------------
# RECURSION: inception_dream()
# ---------------------
def inception_dream():
    answer = input("Do you want to go deeper into the dream? (yes/no): ").strip().lower()
    if answer == "yes":
        # Recursive case: add 1 plus whatever deeper dreams return.
        return 1 + inception_dream()
    else:
        # Base case: return 2
        return 2

# ---------------------
# GAME FLOW
# ---------------------

# Define dice options
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i < 5:
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength_input = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength_input = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: both must be numeric
    if (not combat_strength_input.isdigit()) or (not m_combat_strength_input.isdigit()):
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i += 1
        continue

    combat_strength_val = int(combat_strength_input)
    m_combat_strength_val = int(m_combat_strength_input)

    if (combat_strength_val not in range(1, 7)) or (m_combat_strength_val not in range(1, 7)):
        print("    |    Enter a valid integer between 1 and 6 only")
        i += 1
        continue
    else:
        input_invalid = False
        break

if not input_invalid:
    combat_strength = combat_strength_val
    m_combat_strength = m_combat_strength_val

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image_weapon = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
    """
    print(ascii_image_weapon)
    weapon_roll = random.choice(small_dice_options)

    # Increase the combat strength by the weapon roll (capped at 6)
    combat_strength = min(6, combat_strength + weapon_roll)
    print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Monster rolled " + str(m_health_points) + " health points")

    # Collect Loot using the new function
    belt, loot_options = functions_lab05.collect_loot(belt, loot_options)

    # Use Loot using the new function
    belt, health_points = functions_lab05.use_loot(belt, health_points, good_loot_options, bad_loot_options)

    # Roll for Monster's Magic Power using the new function
    m_combat_strength = functions_lab05.roll_monster_power(m_combat_strength, monster_powers)

    # Determine who strikes first
    attack_roll = random.choice(small_dice_options)
    print("Attack roll is: " + str(attack_roll))
    print("You meet the monster. FIGHT!!")

    # Fight Sequence
    while m_health_points > 0 and health_points > 0:
        if attack_roll in [1, 3, 5]:
            input("You strike first (Press Enter)")
            m_health_points = functions_lab05.hero_attacks(combat_strength, m_health_points)
            if m_health_points <= 0:
                num_stars = 3
                break
            input("The monster strikes (Press Enter)")
            health_points = functions_lab05.monster_attacks(m_combat_strength, health_points)
            if health_points <= 0:
                num_stars = 1
                break
            else:
                num_stars = 2
        else:
            input("The monster strikes first (Press Enter)")
            health_points = functions_lab05.monster_attacks(m_combat_strength, health_points)
            if health_points <= 0:
                num_stars = 1
                break
            input("You strike (Press Enter)")
            m_health_points = functions_lab05.hero_attacks(combat_strength, m_health_points)
            if m_health_points <= 0:
                num_stars = 3
                break
            else:
                num_stars = 2

    # After the battle: Get the Hero's name
    while True:
        hero_name = input("Enter your Hero's name (in two words): ").strip()
        name_parts = hero_name.split()
        if len(name_parts) != 2:
            print("Please enter exactly two words for your Hero's name.")
            continue
        if not (name_parts[0].isalpha() and name_parts[1].isalpha()):
            print("Both parts of the name must be alphabetical.")
            continue
        break

    # Create a short name: first 2 letters of first word + first letter of second word
    short_name = name_parts[0][:2] + name_parts[1][0]

    # Recursive Dream Event
    crazy_level = inception_dream()
    # After the dream, reduce health by 1 and boost combat strength by crazy_level
    health_points = max(0, health_points - 1)
    combat_strength += crazy_level
    print(f"After a deep dream, your health is now {health_points} and your combat strength increased to {combat_strength}.")

    # Final Star Award Print Statement using short_name
    stars = "*" * num_stars
    print("Hero " + short_name + " gets " + stars + " stars")

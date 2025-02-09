import random

def hero_attacks(combat_strength, m_health_points):
    # (Your actual attack logic might be more sophisticated.)
    attack_value = random.randint(1, combat_strength)
    print(f"Hero attacks with a strength of {attack_value}")
    m_health_points = max(0, m_health_points - attack_value)
    print(f"Monster's health is now {m_health_points}")
    return m_health_points

def monster_attacks(m_combat_strength, health_points):
    # (Your actual attack logic might be more sophisticated.)
    attack_value = random.randint(1, m_combat_strength)
    print(f"Monster attacks with a strength of {attack_value}")
    health_points = max(0, health_points - attack_value)
    print(f"Hero's health is now {health_points}")
    return health_points

def collect_loot(belt, loot_options):
    print("!!You find a loot bag!! You look inside to find 2 items:")

    input("Roll for first item (Press enter)")
    if len(loot_options) > 0:
        lootRoll = random.choice(range(1, len(loot_options) + 1))
        loot = loot_options.pop(lootRoll - 1)
        belt.append(loot)
        print("Your belt: ", belt)
    else:
        print("No more loot available for first item.")

    input("Roll for second item (Press enter)")
    if len(loot_options) > 0:
        lootRoll = random.choice(range(1, len(loot_options) + 1))
        loot = loot_options.pop(lootRoll - 1)
        belt.append(loot)
        print("Your belt: ", belt)
    else:
        print("No more loot available for second item.")

    print("You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("Your belt: ", belt)

    return belt, loot_options

def use_loot(belt, health_points, good_loot_options, bad_loot_options):
    if belt:
        print("!!You see a monster in the distance! So you quickly use your first item:")
        first_item = belt.pop(0)
        if first_item in good_loot_options:
            health_points = min(6, (health_points + 2))
            print("You used " + first_item + " to up your health to " + str(health_points))
        elif first_item in bad_loot_options:
            health_points = max(0, (health_points - 2))
            print("You used " + first_item + " to hurt your health to " + str(health_points))
        else:
            print("You used " + first_item + " but it's not helpful")
    else:
        print("No loot to use.")
    return belt, health_points

import random

# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points

# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
    """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Collect Loot Function
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

# Use Loot Function
def use_loot(belt, health_points, good_loot_options, bad_loot_options):
    if belt:
        print("!!You see a monster in the distance! So you quickly use your first item:")
        first_item = belt.pop(0)
        if first_item in good_loot_options:
            health_points = min(6, health_points + 2)
            print("You used " + first_item + " to up your health to " + str(health_points))
        elif first_item in bad_loot_options:
            health_points = max(0, health_points - 2)
            print("You used " + first_item + " to hurt your health to " + str(health_points))
        else:
            print("You used " + first_item + " but it's not helpful")
    else:
        print("No loot to use.")
    return belt, health_points

# Roll Monster's Magic Power Function
def roll_monster_power(m_combat_strength, monster_powers):
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
            @%   @                      
     @     @                        
         &                          
  @      .                          
     
 @       @                    @     
          @                  @      
  @         @              @  @     
   @            ,@@@@@@@     @      
     @                     @        
        @               @           
             @@@@@@@                
    """
    print(ascii_image4)
    power_roll = random.choice(list(monster_powers.keys()))
    m_combat_strength += min(6, monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(m_combat_strength) +
          " using the " + power_roll + " magic power")
    return m_combat_strength

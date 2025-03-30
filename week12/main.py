from mammal import Mammal
from person import Person
from puma import Puma
from tick import Tick

def main():
    print("\n----- Testing Mammal Class -----")
    # Create a generic mammal
    generic_mammal = Mammal(5)
    print(f"Created: {generic_mammal}")
    generic_mammal.speak()
    print(f"Mammal's heart: {generic_mammal.heart}")
    print("Mammal's heart beats:")
    generic_mammal.heart.beat()
    print(f"Updated heart rate: {generic_mammal.heart}")

    print("\n----- Testing Person Class -----")
    # Create a person
    alice = Person("Alice", 30, 170)
    print(f"Created: {alice}")
    alice.speak()
    print("Alice's heart beats:")
    alice.heart.beat()
    print(f"Updated heart rate: {alice.heart}")

    print("\n----- Testing Tick Class -----")
    # Create a tick
    deer_tick = Tick("Deer Tick")
    print(f"Created: {deer_tick}")
    deer_tick.suck_blood()  # No host specified

    print("\n----- Testing Puma Class -----")
    # Create a puma without a tick
    mountain_lion = Puma(8)
    print(f"Created: {mountain_lion}")
    mountain_lion.speak()
    mountain_lion.hunt()
    print(f"After hunting, heart rate: {mountain_lion.heart}")

    print("\n----- Testing Puma with Tick (Aggregation) -----")
    # Create a puma with a tick (aggregation)
    wood_tick = Tick("Wood Tick")
    mountain_lion_with_tick = Puma(6, wood_tick)
    print(f"Created: {mountain_lion_with_tick}")

    # Tick sucks blood from the puma
    if mountain_lion_with_tick.tick:
        mountain_lion_with_tick.tick.suck_blood(mountain_lion_with_tick)
        print(f"Puma's heart rate after tick bite: {mountain_lion_with_tick.heart}")
        print(f"Tick status: {mountain_lion_with_tick.tick}")

if __name__ == "__main__":
    main()
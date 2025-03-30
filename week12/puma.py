from mammal import Mammal

class Puma(Mammal):
    """A class representing a puma, inheriting from Mammal with tick aggregation."""

    def __init__(self, age, tick=None):
        """Initialize a puma with age and an optional tick (aggregation)."""
        # Call the parent class constructor
        super().__init__(age)
        # Set the puma's heart to have a faster bpm
        self.heart.bpm = 120
        # Aggregation: a puma might have a tick
        self.tick = tick

    def speak(self):
        """Override the speak method to make a puma sound."""
        print("Roar! Hiss!")

    def hunt(self):
        """A method specific to pumas."""
        print("The puma is hunting prey...")
        # Hunting increases heart rate
        self.heart.bpm += 10

    def __str__(self):
        """Return a string representation of the puma."""
        tick_info = f" with {self.tick}" if self.tick else " with no ticks"
        return f"A {self.age}-year-old puma with {self.heart}{tick_info}"
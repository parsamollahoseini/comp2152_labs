from heart import Heart

class Mammal:
    """Base class for all mammals demonstrating composition with Heart."""

    def __init__(self, age):
        """Initialize a mammal with age and a heart (composition)."""
        self.age = age
        self.heart = Heart()  # Composition: a mammal has a heart

    def speak(self):
        """Generic mammal sound."""
        print("Generic mammal sound")

    def __str__(self):
        """Return a string representation of the mammal."""
        return f"A {self.age}-year-old mammal with {self.heart}"
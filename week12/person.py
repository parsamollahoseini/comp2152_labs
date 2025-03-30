from mammal import Mammal

class Person(Mammal):
    """A class representing a person, inheriting from Mammal."""

    def __init__(self, name, age, height):
        """Initialize a person with name, age, and height."""
        # Call the parent class constructor
        super().__init__(age)
        self.name = name
        self.height = height

    def speak(self):
        """Override the speak method to say hello."""
        print(f"Hello, my name is {self.name}!")

    def __str__(self):
        """Return a string representation of the person."""
        return f"{self.name}, {self.age} years old, {self.height}cm tall with {self.heart}"
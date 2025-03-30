class Tick:
    """A class representing a tick parasite that can suck blood."""

    def __init__(self, name="Common Tick"):
        """Initialize a tick with a name."""
        self.name = name
        self.blood_amount = 0

    def suck_blood(self, host=None):
        """Suck blood from the host and increase blood amount."""
        if host:
            print(f"The {self.name} is sucking blood from the {type(host).__name__}!")
            # Increase blood count
            self.blood_amount += 1
            # Increase host heart rate due to stress
            if hasattr(host, 'heart'):
                host.heart.bpm += 5
        else:
            print(f"The {self.name} is looking for a host to feed on...")

    def __str__(self):
        """Return a string representation of the tick."""
        return f"{self.name} (blood amount: {self.blood_amount})"
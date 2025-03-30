class Heart:
    """A class representing a heart that can beat."""

    def __init__(self, bpm=72):
        """Initialize a heart with a default beats per minute rate."""
        self.bpm = bpm

    def beat(self):
        """Simulate a heartbeat and slightly increase heart rate."""
        print("Lub-dub")
        # Heart rate slightly increases when beating
        self.bpm += 1

    def __str__(self):
        """Return a string representation of the heart's bpm."""
        return f"Heart rate: {self.bpm} bpm"
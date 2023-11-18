"""CP1404 Practical - Band class code"""

class Band:
    """Represent a Band Instance."""

    def __init__(self, band):
        """Initialise a Band instance."""
        self.band = band
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band instance."""
        return f"{self.band} ({', '.join(str(musician) for musician in self.musicians)}"

    def add(self, musician):
        """Add a musician instance to a Band instance."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of a musician and their instruments."""
        return '\n'.join(musician.play() for musician in self.musicians)

"""CP1404 Practical - Car class example.
Estimation: 15 minutes
Actual: 12 minutes
"""

CURRENT_YEAR = 2023
AGE_THRESHOLD = 50


class Guitar:
    """Class for storing guitar details."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a guitar instance."""
        return f"{self.name} ({self.year})/{self.get_age} years old, vintage = {self.is_vintage()} : ${self.cost:,.2f}"

    def get_age(self):
        """Get a guitar's age based on the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is considered vintage or not based on age."""
        return self.get_age() >= AGE_THRESHOLD

"""CP1404 Practical - ProgrammingLanguage class."""


class ProgrammingLanguage:
    """Display information regarding programming languages."""

    def __init__(self, language_name="", typing=False, reflection=False, year=0):
        """Initialise a ProgrammingLanguage from the given language values."""
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string represenation of a ProgrammingLanguage"""
        return f"{self.language_name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if ProgrammingLanguage is dynamically typped."""
        return self.typing == "Dynamic"

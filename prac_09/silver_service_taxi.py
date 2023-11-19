"""CP1404 Practical - SilverServiceTaxi class code."""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fanciness."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Car but with flagwall cost."""
        return f"{super().__str__()} plus flagwall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

"""CP1404 Practical - UnreliableCar class code."""

from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that may not drive."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an instance of a UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent car but only when random number > reliability."""
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
